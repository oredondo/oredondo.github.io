---
title: "Caso de Estudio: Plataforma IaaS Orion y Pipeline por Drivers"
description: >-
  Arquitectura del plano de control IaaS central de BBVA — un sistema en Python/Django que gobierna 30.000+ máquinas en AWS, OpenStack, OpenShift y bare-metal con auditoría integral, Ansible en capas (Ground + Usuario) y automatización apificada y programada.
---

# Orion: Plataforma IaaS Central y Pipeline Universal por Drivers

| Dimensión | Detalles |
| :--- | :--- |
| **Rol** | Arquitecto y Responsable de Plataforma |
| **Organización** | BBVA (Infraestructura Core Banking) |
| **Escala** | 30.000+ máquinas gobernadas · 40.000+ operaciones diarias · 500+ ingenieros |
| **Stack** | Python, Django, DRF, Celery, PostgreSQL, MongoDB, Redis, Ansible, AWS, OpenStack, OpenShift, Infoblox |

!!! abstract "Resumen de arquitectura"

    Orion es el plano de control central para el gobierno, auditoría integral y despliegue en autoservicio de infraestructura en la nube híbrida de BBVA. Abstrae cuatro sustratos tecnológicos (**AWS, OpenStack, OpenShift y servidores físicos**) tras una interfaz REST documentada con OpenAPI, formularios web y un subsistema de **Schedulers programados**, combinando un **pipeline de despliegue por drivers**, ejecución de **Ansible en dos capas (Ground corporativo y Usuario)** y un **motor de auditoría forense y trazabilidad de máquinas**.

---

## 1. La Evolución de Orion: De CMDB a Dispatcher de Alta Disponibilidad

Orion no nació como un producto monolítico estático, sino como una respuesta evolutiva a los cuellos de botella de escala en **BBVA**:

- **Fase 1 · Origen (CMDB e Inventario Apificado):** Plano de control para gobernar activos heterogéneos multi-cloud mediante persistencia híbrida (PostgreSQL + MongoDB + Redis) y catálogo REST con permisos RBAC.
- **Fase 2 · El Cuello de Botella de Jenkins:** La ejecución dependía de un clúster central de Jenkins que carecía de alta disponibilidad (SPOF crítico), ofrecía una UI rígida para operaciones y presentaba alta complejidad de mantenimiento.
- **Fase 3 · Nacimiento del Dispatcher HA Integrado:** Orion absorbió el plano de ejecución con un **Dispatcher HA propio (Django + Celery + Kubernetes Jobs)**, desacoplando variables en runtime y estructurando la provisión en drivers cloud y Ansible en capas.
- **Fase 4 · Extensión Declarativa e IA (Blueprint & Orion AI):** Unificación de la orquestación declarativa con **Blueprint** (motor YAML con DAGs) y el diagnóstico agéntico de fallos de CI/CD con **Orion AI** (LangGraph).

---

## 2. Contexto y Problema de Ingeniería

Operar decenas de miles de activos bancarios entre nube pública, nube privada y centros de datos físicos generaba tres desafíos críticos:

1. **Aprovisionamiento en silos:** Cada entorno destino requería herramientas y credenciales aisladas, convirtiendo peticiones sencillas en traspasos manuales de varios días.
2. **Ceguera de auditoría y dispersión de datos:** Exigencia regulatoria bancaria estricta (marcos de resiliencia como **DORA** y directrices BCE/EBA) de conocer en cualquier instante qué usuario autorizó un recurso, qué software exacto tiene instalado y qué eventos han ocurrido a lo largo de su vida útil.
3. **Deriva de configuración y brechas de seguridad:** Sin una separación forzosa entre la línea base del banco (seguridad, monitorización) y las aplicaciones, proliferaban máquinas desalineadas con la normativa corporativa.

---

## 3. Topología Abstracta del Sistema: Ciclo de Vida de una Operación

Orion centraliza el ciclo de vida de la infraestructura bancaria mediante un flujo secuencial estricto:

```mermaid
flowchart LR
    Trig["Disparo<br/><b>(Frontal Web · API · Scheduler)</b>"] --> Disp["Dispatcher HA<br/><b>(RBAC & Celery)</b>"]
    Disp --> Prov["1. Provisión<br/><b>(Drivers Cloud)</b>"]
    Prov --> Conf["2. Configuración<br/><b>(Ansible Ground + Usuario)</b>"]
    Conf --> Audit[("3. Auditoría<br/><b>(Software & Histórico)</b>")]
```

### Pipeline de Ejecución Paso a Paso

| Fase | Componente Responsable | Qué se ejecuta exactamente | Garantía de Ingeniería |
| :--- | :--- | :--- | :--- |
| **1. Disparo** | Frontal Web / API REST / Schedulers (Celery Beat) | Formulario de autoservicio en UI web, llamada directa a la API REST o ejecución periódica programada. | Ingesta asíncrona desacoplada con respuesta inmediata. |
| **2. Autorización** | Motor RBAC & PostgreSQL | Comprobación estricta de permisos del usuario, cuotas y registro inmutable de la solicitud. | Cero peticiones anónimas o sin trazabilidad de cambio. |
| **3. Provisión** | Capa de Drivers Multi-Cloud | Llamada al proveedor correspondiente (**AWS, OpenStack, OpenShift o Bare-Metal**) para crear el cómputo y asignar IP/DNS. | Abstracción homogénea sin acoplamiento a APIs propietarias. |
| **4. Ground Ops** | Ansible Core (Línea Base Bancaria) | **Fase obligatoria y previa al usuario:** bastionado CIS del SO, certificados TLS corporativos y agentes de observabilidad. | **100% compliance obligatorio:** si Ground falla, el despliegue se aborta de inmediato. |
| **5. User Ops** | Ansible Runner (Carga de Usuario) | Inyección dinámica de variables y ejecución de playbooks del usuario (middleware, bases de datos, aplicaciones). | Aislamiento entre la línea base del banco y la lógica de la app. |
| **6. Auditoría** | Motor de Auditoría (PostgreSQL + MongoDB) | Recolección de telemetría final: versiones exactas de todos los paquetes instalados en el nodo y log de eventos. | Informes forenses inmediatos para auditores y reguladores. |

---

## 4. Decisiones Clave de Arquitectura

### A. Persistencia Híbrida: Integridad Relacional vs. Flexibilidad Documental
Un único motor de base de datos no resolvía simultáneamente el cumplimiento bancario estricto y el inventario multi-cloud:
- **PostgreSQL** custodia el núcleo relacional que exige integridad transaccional estricta (ACID): permisos RBAC, catálogo de productos, transiciones de estado de operaciones e histórico inmutable de auditoría.
- **MongoDB** ingiere y almacena documentos polimórficos de activos sobre decenas de miles de máquinas (donde una instancia AWS, una VM OpenStack o un servidor físico tienen esquemas de atributos totalmente dispares), indexando el árbol completo de software y paquetes instalados para consultas masivas.
- **Redis** actúa como caché rápida de inventario y broker de alta velocidad para las colas asíncronas de Celery.

### B. Separación de Responsabilidades: Pipeline Ansible en Dos Fases
Para erradicar la deriva de configuración sin frenar la autonomía de los equipos de desarrollo, la automatización se divide en dos capas secuenciales:
- **Capa Ground (Garantía Corporativa):** Bastionado CIS del sistema operativo, cortafuegos, certificados TLS corporativos y despliegue de agentes de observabilidad. Ninguna máquina pasa a disposición del usuario si la verificación Ground no concluye con éxito.
- **Capa de Usuario (Autonomía de Aplicación):** Inyección aislada de variables en tiempo de ejecución para desplegar middleware y lógica de negocio específica.

### C. Auditoría Integral y Trazabilidad del Ciclo de Vida
Orion no delega la auditoría en logs efímeros de pipelines. Registra de forma inmutable cada evento en la vida de cada nodo: qué usuario autorizó la creación, qué cambios se han aplicado a lo largo del tiempo, qué versiones exactas de librerías tiene instaladas y su historial completo de incidencias. Esto convierte a Orion en la pieza clave para responder a los mandatos de gestión de riesgos e inventario de activos TIC de **DORA** (Reglamento UE 2022/2554).

---

## 5. Trade-Offs de Arquitectura

| Decisión | Alternativa Evaluada | Justificación |
| :--- | :--- | :--- |
| **Ansible en dos capas (Ground + Usuario)** | Playbook monolítico gestionado por el usuario | Garantiza el 100% de cumplimiento en seguridad y monitorización corporativa sin depender de la disciplina de cada equipo. |
| **Auditoría centralizada en Orion** | Trazabilidad delegada en logs de pipelines | Permite responder a auditorías regulatorias bancarias en segundos con el historial forense de cada máquina y sus paquetes. |
| **Híbrido PostgreSQL + MongoDB** | Base relacional única con columnas JSONB | Mantiene integridad relacional estricta para RBAC con indexación de alta velocidad sobre metadatos e inventario heterogéneo. |
| **Abstracción por drivers en Python** | Herramientas y flujos independientes por nube | Unifica RBAC, catálogo de operaciones y auditoría en un solo plano de control agnóstico de proveedor. |

---

## 6. Impacto Operativo y de Negocio

- **Eficiencia de costes y soberanía tecnológica:** La consolidación de este plano de control propio y su motor de ejecución en alta disponibilidad permitió prescindir por completo de suites comerciales de automatización licenciadas por nodo (como Red Hat Ansible Automation Platform), generando un **ahorro acumulado estimado superior a 6 millones de euros** en licencias e intermediarios para la organización.
- **Auditoría y trazabilidad completa (Cumplimiento DORA):** Transformó la preparación de auditorías bancarias de semanas de recopilación manual a consultas automatizadas e instantáneas de cualquier máquina: quién la creó, qué paquetes tiene instalados y su histórico completo de eventos, respondiendo de forma nativa a las exigencias de inventario TIC de **DORA** y del Banco Central Europeo.
- **Seguridad y observabilidad garantizada (Ground):** El 100% de las más de **30.000 máquinas** cuentan con agentes de seguridad y monitorización desplegados y verificados automáticamente desde el momento de su aprovisionamiento.
- **Autoservicio y operaciones masivas:** Más de **500 ingenieros** gestionan su ciclo de vida de infraestructura de forma autónoma, procesando más de **40.000 operaciones diarias** mediante API REST, formularios web y Schedulers programados.
- **Adopción internacional:** Plataforma implantada y operativa en múltiples geografías del grupo bancario (**España, México y Turquía**).

---

[:octicons-arrow-right-24: Siguiente: Blueprint — Orquestación declarativa de ciclo de vida sobre Orion](blueprint.md)
