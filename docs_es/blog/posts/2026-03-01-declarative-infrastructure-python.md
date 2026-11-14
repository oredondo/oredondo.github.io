---
draft: false
description: >-
  Reflexiones tras nueve años construyendo una plataforma cloud interna: por qué ser propietarios del plano de control cambió nuestra decisión de construir frente a comprar, y por qué el desmontaje idempotente es la verdadera prueba de fuego.
slug: declarative-yaml-engine-python
date: 2026-03-01
authors:
  - oredondo
categories:
  - Platform Engineering
  - Python
  - Architecture
tags:
  - IaC
  - Python
  - AsyncIO
  - PlatformEngineering
---

# Nueve Años de Plataformas Cloud Internas: Por Qué el YAML Declarativo Sustituyó a Nuestro Orquestador Comercial

"No construyas tu propio orquestador" suele ser un buen consejo — hasta que analizas en detalle qué piezas ya son propiedad de tu organización y en qué se va realmente el presupuesto de las suites comerciales.

Cuando evaluamos cómo más de 500 ingenieros debían orquestar entornos completos de infraestructura sobre nuestra nube híbrida, la opción corporativa por defecto era una suite comercial como **Red Hat Automation Platform (Ansible Tower)**. En su lugar, diseñamos **Blueprint**: un motor asíncrono y declarativo de ciclo de vida en Python guiado por planos YAML versionados.

Este artículo explica por qué esa decisión tuvo sentido en nuestro contexto, qué decidimos *no* construir y por qué **el desmontaje** — no la creación — es la verdadera prueba de fuego de cualquier motor de infraestructura.

<!-- more -->

## 1. Ser Dueño del Plano de Control Cambia la Ecuación Build vs. Buy

La mayoría de las organizaciones adoptan grandes orquestadores externos porque carecen de una API unificada sobre su infraestructura subyacente.

Nosotros partíamos de un escenario distinto. Durante años habíamos construido **Orion**, nuestra plataforma IaaS central que gobierna decenas de miles de nodos en AWS, OpenStack, OpenShift y bare-metal tras una única API REST basada en drivers. Orion ya resolvía:

- Autenticación, control de acceso (RBAC) y políticas de cumplimiento.
- Traducción específica para cada proveedor cloud mediante drivers.
- Inventario multi-cloud en tiempo real sobre PostgreSQL y MongoDB.
- Trazabilidad de trabajos y pistas inmutables de auditoría.

Comprar una suite comercial de orquestación para colocarla delante de Orion implicaba pagar licencias por nodo sobre decenas de miles de máquinas únicamente para secuenciar llamadas HTTP contra una API que ya era nuestra — perdiendo además la trazabilidad nativa de los Job IDs de Orion cuando un despliegue de múltiples pasos fallaba a mitad de camino.

## 2. Por Qué Evitamos los Archivos Locales de Estado

Las herramientas inspiradas en Terraform suelen heredar su decisión de diseño operativamente más dolorosa: un archivo de estado separado (`tfstate`) que debe almacenarse, bloquearse y reconciliarse cada vez que alguien realiza un cambio fuera de banda.

Dado que **Blueprint** se diseñó específicamente sobre **Orion**, tomamos una decisión deliberada de arquitectura: **cero archivos locales de estado**.

```mermaid
flowchart LR
    Manifest["Plano YAML Versionado<br/>(Estado Deseado en Git)"] --> Engine["Motor Asíncrono Blueprint<br/>(Resolvedor DAG y Delta)"]
    Orion[("Plano de Control Orion<br/>(Estado Observado en Vivo)")] --> Engine
    Engine -->|"Ejecuta solo el diferencial<br/>(Olas concurrentes)"| Orion
    Engine --> Report["Informe Estructurado de Auditoría<br/>(Vinculado a Job IDs de Orion)"]
```

La base de datos híbrida de Orion *es* la fuente única de verdad en tiempo real. Antes de que Blueprint ejecute una ola de operaciones, consulta directamente a Orion el estado actual de los recursos declarados y actúa únicamente sobre el diferencial. No hay archivo de estado que corromper, ni bloqueos colgados tras la caída de un runner, ni divergencia entre "el estado del orquestador" y "el inventario de la plataforma".

## 3. Crear Es Fácil; el Desmontaje Idempotente Es la Prueba Real

Casi cualquier script puede aprovisionar un entorno desde cero cuando todas las APIs responden `200 OK`. Donde la automatización procedimental se desmorona es ante un **fallo parcial durante la destrucción**.

Imaginemos el desmontaje de un entorno de 25 recursos (grupos de cómputo, reglas de balanceo, volúmenes, subredes). El paso 14 sufre un timeout porque una API cloud externa experimenta una degradación puntual. ¿Qué ocurre cuando el ingeniero relanza el trabajo cinco minutos después?

- **En playbooks procedimentales:** El paso 1 intenta borrar un recurso que ya fue eliminado en el primer intento, recibe un `404 Not Found` y aborta toda la ejecución — obligando a comentar líneas a mano o limpiar recursos manualmente.
- **En Blueprint:** Cada paso de un desmontaje (con el grafo de dependencias invertido) consulta primero a Orion. Los pasos del 1 al 13 detectan que sus recursos ya no existen, registran un `NO-OP` limpio y el motor reanuda inmediatamente en el paso 14.

Hacer que la destrucción sea **segura de repetir** transformó el desmantelamiento de entornos de un ticket manual crítico a una operación rutinaria en autoservicio.

## 4. El Coste Honesto de Construir en Casa

Ser propietario del motor de orquestación elimina licencias comerciales y encaja como un guante con la auditoría interna, pero exige disciplina:

- **Asumes los casos límite:** La detección de ciclos en grafos de dependencias, el reporte de fallos parciales y la evolución del esquema pasan a ser responsabilidad directa de tu equipo.
- **La documentación es parte del producto:** Una herramienta comercial cuenta con respuestas en foros públicos; un DSL interno en YAML solo triunfa si sus mensajes de validación y plantillas de referencia se explican por sí solos.

Tras nueve años evolucionando esta arquitectura, la conclusión es clara: no reinventes los SDKs de los proveedores cloud — encapsúlalos tras drivers. Pero cuando la capa de orquestación se sitúa directamente entre tus ingenieros, tus auditores y tu plano de control, un motor ligero y bien acotado en Python puede superar a una suite comercial pesada tanto en fiabilidad como en coste.

---

*Descubre cómo se conectan ambos sistemas en los casos de estudio de [Orion IaaS](../../projects/orion-iaas.md) y [Blueprint](../../projects/blueprint.md).*
