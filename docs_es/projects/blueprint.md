---
title: "Caso de Estudio: Motor Declarativo Blueprint"
description: >-
  Motor de orquestación asíncrono en Python guiado por planos YAML versionados — llevando la filosofía declarativa estilo Terraform y desmontajes idempotentes a la nube interna de BBVA.
---

# Blueprint: Motor Asíncrono de Ciclo de Vida Declarativo

| Dimensión | Detalles |
| :--- | :--- |
| **Rol** | Arquitecto y Responsable de Plataforma |
| **Organización** | BBVA (Infraestructura Core Banking) |
| **Resultado** | Eliminación de licencias comerciales de orquestación (Red Hat Automation Platform); GitOps declarativo y desmontajes reanudables sobre Orion |
| **Stack** | Python, AsyncIO, DSL Declarativo en YAML, JSON Schema, GitOps, API REST de Orion |

!!! abstract "Resumen de arquitectura"

    Blueprint es un motor interno de orquestación asíncrona en Python — conceptualmente análogo a Terraform y diseñado específicamente sobre la plataforma **Orion** de BBVA. Los equipos de ingeniería declaran el estado deseado de sus entornos completos en planos YAML versionados; el motor resuelve el grafo de dependencias, ejecuta operaciones independientes en paralelo, genera un informe estructurado con trazabilidad completa de trabajos en Orion para auditoría y soporta **operaciones de destrucción idempotentes** que reanudan desmontajes parciales sin reprocesar pasos ya completados.

---

## 1. Contexto y Por Qué No Encajaban las Suites Comerciales

Una vez que **Orion** expuso una API REST unificada sobre AWS, OpenStack, OpenShift y bare-metal, los equipos necesitaban orquestar entornos completos (redes, balanceadores, grupos de cómputo, middleware) como una sola unidad en lugar de invocar endpoints aislados.

Depender de suites comerciales de orquestación como **Red Hat Automation Platform (Ansible Tower)** presentaba tres problemas estructurales:

1. **Coste de licenciamiento por nodo:** Las licencias comerciales escalan según el número de servidores gestionados, penalizando el crecimiento sobre decenas de miles de nodos.
2. **Opacidad ante fallos a mitad de ejecución:** Cuando una secuencia procedimental de 40 pasos falla en el paso 27 por un corte transitorio de red, reconstruir el estado exacto para auditoría o desmontar de forma segura el entorno parcial exigía intervención manual.
3. **Desajuste con la arquitectura de Orion:** Ya éramos propietarios de la fuente única de verdad (Orion). Necesitábamos un orquestador que hablara de forma nativa el modelo de identificadores de trabajo (Job IDs), sondeo asíncrono, permisos RBAC y reportes de cumplimiento de Orion.

---

## 2. Topología Abstracta del Sistema: Ciclo de Vida de una Orquestación

Blueprint procesa planos declarativos mediante un pipeline asíncrono estricto: desde la validación estática del manifiesto YAML, pasando por la resolución del grafo DAG y la ejecución concurrente sobre Orion, hasta la emisión del informe inmutable de auditoría.

```mermaid
flowchart LR
    Plan["1. Plano Declarativo<br/><b>(Manifiesto YAML en Git)</b>"] --> DAG["2. Motor Blueprint<br/><b>(Validación & Olas DAG)</b>"]
    DAG --> Orion["3. API Orion IaaS<br/><b>(Ejecución AsyncIO)</b>"]
    Orion --> Teardown["4. Ciclo de Vida<br/><b>(Desmontaje Idempotente)</b>"]
    Teardown --> Audit[("5. Auditoría<br/><b>(Trazabilidad por Job ID)</b>")]
```

### Pipeline de Ejecución Paso a Paso

| Fase | Componente Responsable | Qué se ejecuta exactamente | Garantía de Ingeniería |
| :--- | :--- | :--- | :--- |
| **1. Validación Pre-Flight** | Validador JSON Schema (Python) | Comprobación de tipos, restricciones de sintaxis y detección de dependencias circulares en el YAML antes de tocar producción. | Rechazo inmediato de manifiestos erróneos sin llamadas a la API. |
| **2. Construcción del DAG** | Programador de Dependencias | Cálculo del árbol dirigido acíclico y partición de tareas en olas concurrentes (*waves*). En destrucciones, invierte el orden automáticamente. | Paralelismo máximo respetando la topología de red y servicios. |
| **3. Inspección en Vivo** | Conector REST con Orion | Consulta del estado real de los recursos contra el inventario vivo de Orion para calcular el diferencial (*delta*). | Omisión limpia de pasos ya satisfechos (NO-OP), evitando re-trabajo. |
| **4. Ejecución Asíncrona** | Motor AsyncIO | Despacho de llamadas concurrentes contra Orion para todos los recursos de la ola actual, monitorizando cada Job ID devuelto. | Alta concurrencia sin bloqueo de hilos y huella mínima de memoria. |
| **5. Informe de Auditoría** | Generador de Trazas Forenses | Emisión de un documento estructurado que asocia cada recurso declarado con sus Job IDs exactos, marcas de tiempo y transiciones de estado. | Trazabilidad inmutable 100% auditable ante organismos reguladores. |

---

## 3. Decisiones Clave de Arquitectura

### A. Planos YAML Declarativos frente a Scripts Procedimentales
En lugar de mantener scripts imperativos que mezclan flujo de control con estado de infraestructura, los equipos versionan en Git un plano YAML declarativo que define **qué** topología debe existir y las dependencias entre componentes. La validación de esquema detecta errores estructurales y ciclos antes de realizar una sola llamada a Orion.

### B. Concurrencia Asíncrona por Olas (Waves)
El aprovisionamiento de infraestructura está limitado por I/O (esperas de red ante APIs cloud, hipervisores y balanceadores). Blueprint organiza el grafo de dependencias en **olas de ejecución**:

- Los recursos sin dependencias pendientes se ejecutan **de forma concurrente** sobre el bucle de eventos `AsyncIO` de Python.
- Los recursos dependientes esperan a que su ola predecesora finalice correctamente.
- Si un paso falla a mitad de una ola, el motor conserva el registro exacto de cada trabajo en vuelo dentro de Orion sin perder la trazabilidad de las operaciones hermanas.

### C. Destrucción Idempotente y Reanudación de Desmontajes Parciales
El desmantelamiento de entornos complejos es el punto donde suele romperse la automatización tradicional. Si una destrucción falla a mitad de camino, un script ingenuo aborta al relanzarse porque la primera mitad de los recursos ya no existe.

Blueprint gestiona el **ciclo de vida completo de la infraestructura**:

- En modo destrucción, el orden de dependencias se invierte para eliminar los servicios dependientes antes que las redes o el almacenamiento compartido.
- Antes de actuar sobre cualquier nodo, el motor verifica el estado en vivo en Orion. Los pasos ya completados en una ejecución previa interrumpida se omiten limpiamente, permitiendo relanzar el mismo plano hasta completar el desmontaje sin tocar la base de datos manualmente.

### D. Trazabilidad Extremo a Extremo por Job ID
En un entorno bancario regulado, que un pipeline termine en verde no basta como evidencia de auditoría. Cada ejecución de Blueprint genera un informe estructurado que vincula cada recurso del manifiesto YAML con los **Job IDs exactos de Orion**, marcas de tiempo y transiciones de estado ejecutadas — incluso cuando una ejecución se detiene a mitad de camino.

---

## 4. Modos de Fallo y Diseño de Resiliencia

```mermaid
flowchart LR
    Val["1. Validación DAG"] --> Wave["2. Olas de Ejecución"]
    Wave -->|"Fallo transitorio"| Res["3. Reanudación Segura<br/>(Pasos hechos = NO-OP)"]
    Res --> Done[("4. Estado Objetivo Consistente")]
```

| Escenario de Fallo | Playbook Procedimental Tradicional | Comportamiento del Motor Blueprint |
| :--- | :--- | :--- |
| **Dependencia circular en el manifiesto** | Se descubre a mitad del despliegue tras mutar producción | Rechazado en la validación previa del DAG antes de invocar ninguna API |
| **Timeout a mitad de un desmontaje de 20 nodos** | Al relanzar falla con "recurso no encontrado" en los nodos 1–10 | Al relanzar consulta Orion, omite los nodos 1–10 y reanuda en el nodo 11 |
| **Auditoría solicita evidencia de un cambio fallido** | Correlación manual entre múltiples logs de consola | Informe estructurado vincula cada paso con su Job ID inmutable en Orion |

---

## 5. Trade-Offs de Arquitectura

| Decisión | Alternativa Evaluada | Justificación |
| :--- | :--- | :--- |
| **Motor propio en Python** | Red Hat Automation Platform / Terraform | Eliminó costes recurrentes de licencias comerciales, se integró de forma nativa con el modelo de trabajos y auditoría de Orion y evitó bloqueos de archivos de estado externos. |
| **Orion como fuente única de verdad en vivo** | Archivos locales de estado (equivalente a `tfstate`) | Orion ya mantiene el inventario multi-cloud en tiempo real; consultar Orion evita deriva de estado (*drift*) y bloqueos concurrentes. |
| **Concurrencia con AsyncIO** | Ejecutores multi-hilo o multi-proceso | Alta concurrencia para cientos de esperas de API simultáneas con una huella de memoria mínima. |

---

## 6. Impacto Operativo y de Negocio

- **Eliminación de licencias comerciales:** Al diseñar un motor declarativo propio e integrado con Orion, se prescindió por completo de herramientas comerciales licenciadas por nodo (como Red Hat Ansible Automation Platform / Tower), contribuyendo decisivamente al ahorro acumulado superior a 6 millones de euros para la organización.
- **Desmontajes idempotentes y reanudables:** 100% de éxito en desmantelamientos parciales o reanudados tras incidencias, eliminando recursos huérfanos y mitigando cualquier riesgo de deriva manual.
- **Concurrencia asíncrona masiva:** Aceleró los tiempos de aprovisionamiento de entornos complejos en más de un 60% gracias a la resolución de dependencias por olas concurrentes sobre el bucle `AsyncIO` de Python.
- **Trazabilidad y auditoría por Job ID:** Evidencia inmutable generada automáticamente para cada despliegue, vinculando los manifiestos YAML con los identificadores de trabajo de Orion para auditorías regulatorias bancarias.

---

[:octicons-arrow-left-24: Anterior: Plataforma IaaS Orion](orion-iaas.md) · [:octicons-arrow-right-24: Siguiente: Dejar Jenkins Atrás — Dispatcher HA y Ejecución K8s](dispatcher-migration.md)
