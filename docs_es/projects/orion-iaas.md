---
title: "Caso de Estudio: Plataforma IaaS Orion y Pipeline por Drivers"
description: >-
  Arquitectura del plano de control IaaS central de BBVA — un sistema en Python/Django que gobierna 30.000+ máquinas en AWS, OpenStack, OpenShift y bare-metal con auditoría integral, Ansible en capas (Ground + Usuario) y automatización apificada y programada.
---

# Orion: Plataforma IaaS Central y Pipeline Universal por Drivers

| Dimensión | Detalles |
| :--- | :--- |
| **Rol** | Arquitecto Único y Responsable de Plataforma |
| **Organización** | BBVA Technology (Infraestructura Core Banking) · 2017 – Presente |
| **Escala** | 30.000+ máquinas gobernadas · 40.000+ operaciones diarias · 500+ ingenieros |
| **Stack** | Python, Django, DRF, Celery, PostgreSQL, MongoDB, Redis, Ansible, AWS, OpenStack, OpenShift, Infoblox |

!!! abstract "Resumen de arquitectura"

    Orion es el plano de control central para el gobierno, auditoría integral y despliegue en autoservicio de infraestructura en la nube híbrida de BBVA. Abstrae cuatro sustratos tecnológicos (**AWS, OpenStack, OpenShift y servidores físicos bare-metal**) tras una interfaz REST documentada con OpenAPI y un subsistema de **Schedulers programados**, combinando un **pipeline universal de despliegue por drivers**, ejecución de **operaciones Ansible en dos capas (Ground corporativo y Usuario)**, una **capa híbrida de persistencia** y un **motor de auditoría integral y trazabilidad de máquinas**.

---

## 1. La Evolución de Orion: De CMDB e Inventario a Dispatcher de Alta Disponibilidad

Orion no nació como un producto monolítico estático, sino como una respuesta arquitectónica evolutiva a los cuellos de botella reales de escala en **BBVA Technology** — gobernando **más de 30.000 máquinas** en **AWS, OpenStack, OpenShift y bare-metal** y procesando **más de 40.000 operaciones diarias** para **más de 500 ingenieros**:

### Hitos de la Evolución Arquitectónica

- **Fase 1 · Origen: CMDB, Inventario Multi-Cloud y Catálogo Apificado**
    - *Contexto:* Orion nació como un plano de control central para inventariar y catalogar activos heterogéneos sobre AWS, OpenStack, OpenShift y servidores físicos.
    - *Solución:* Base de datos híbrida (PostgreSQL para transacciones, MongoDB para activos polimórficos, Redis para caché), catálogo OpenAPI y canalizaciones de auditoría para responder a las exigencias regulatorias del banco.

- **Fase 2 · El Cuello de Botella de Jenkins**
    - *Problema:* El disparo de operaciones dependía inicialmente de un clúster centralizado de Jenkins.
    - *Fricciones:* Jenkins carecía de Alta Disponibilidad nativa (constituyendo un punto único de fallo crítico para el banco), su interfaz estaba concebida para compilaciones de código en lugar de máquinas de estado de infraestructura, y el acoplamiento de plugins dificultaba integrar nuevas funcionalidades bancarias.

- **Fase 3 · Nacimiento del Dispatcher HA Integrado**
    - *Transformación:* Orion absorbió el plano de ejecución desarrollando un **Dispatcher de Operaciones en Alta Disponibilidad propio (Django + Celery + Kubernetes Jobs)**.
    - *Resultado:* Reemplazo del 100% de Jenkins para infraestructura, desacoplamiento dinámico de variables en runtime, soporte nativo de operaciones apificadas y vía schedulers, y estructuración de la provisión en dos fases: drivers cloud y pipeline Ansible en capas (Ground y Usuario).

- **Fase 4 · Extensión Declarativa (Blueprint) e IA Operativa (Orion AI)**
    - *Madurez:* Con la CMDB, el motor de auditoría y el dispatcher unificados bajo la misma arquitectura, Orion se extendió hacia la orquestación declarativa con **Blueprint** (motor en YAML con dependencias DAG y desmontajes idempotentes sin suites comerciales) y el auto-diagnóstico agéntico de fallos de CI/CD con **Orion AI** (LangGraph).

---

## 2. Contexto y Problema de Ingeniería

Operar infraestructura a escala bancaria entre nube pública, nube privada, plataformas de contenedores y centros de datos propios generaba tres cuellos de botella estructurales:

1. **Aprovisionamiento en silos y heterogeneidad:** Cada entorno destino (AWS, OpenStack, OpenShift, hardware físico) requería sus propias herramientas, credenciales y traspasos manuales por tickets — convirtiendo peticiones sencillas en esperas de varios días.
2. **Falta de auditoría centralizada y trazabilidad de activos:** En un entorno bancario altamente regulado, es imperativo conocer en cualquier momento qué usuario autorizó un recurso, quién tiene permisos sobre él, **qué software exacto tiene instalado cada máquina y qué eventos u operaciones han ocurrido en ella a lo largo de toda su vida útil**. La información dispersa en herramientas de proveedores impedía generar informes forenses y de cumplimiento fiables.
3. **Deriva de configuración y brechas de seguridad base:** Sin un estándar unificado de configuración, cada equipo desplegaba software con criterios dispares, provocando servidores sin agentes de monitorización obligatorios, políticas de bastionado desactualizadas o repositorios de paquetería no autorizados.

---

## 3. Topología Abstracta del Sistema: Ciclo de Vida de una Operación

Orion centraliza el ciclo de vida de la infraestructura bancaria: desde la llamada API o el scheduler programado, pasando por la capa de drivers y la configuración Ansible en capas, hasta el sellado inmutable de auditoría forense.

```mermaid
sequenceDiagram
    autonumber
    actor Trigger as Ingeniero (API REST) / Scheduler (Cron)
    participant Orion as Orion Control Plane & RBAC
    participant Disp as Dispatcher HA (Celery)
    participant Cloud as Driver Multi-Cloud (AWS / OpenStack / Bare-Metal)
    participant AnsG as Ansible: Ground (Seguridad & Mon)
    participant AnsU as Ansible: Carga de Usuario
    participant Audit as Motor de Auditoría (PostgreSQL + MongoDB)

    Trigger->>Orion: 1. Petición autenticada (API OpenAPI o Scheduler)
    Orion->>Audit: Registra solicitud, identidad y permisos (RBAC)
    Orion->>Disp: Encola ejecución asíncrona
    Disp->>Cloud: Aprovisiona nodo en el proveedor destino
    Cloud-->>Disp: Nodo activo e IP asignada
    Disp->>AnsG: Ejecuta Ground obligatorio (Bastionado, Mon, Repos)
    AnsG-->>Disp: Ground validado con éxito (100% compliance)
    Disp->>AnsU: Ejecuta playbooks de usuario (Apps, Middleware, DB)
    AnsU-->>Disp: Carga de trabajo desplegada correctamente
    Disp->>Audit: Sella software instalado, versiones de paquetes y eventos
```

---

## 4. Decisiones Clave de Arquitectura

### A. Auditoría Integral de la Plataforma: Permisos y Trazabilidad de Máquinas
Orion actúa como la **fuente de verdad indiscutible de auditoría** para toda la plataforma de infraestructura de BBVA:

- **Auditoría de Permisos y Autorizaciones:** Control de acceso basado en roles (RBAC) con trazabilidad estricta. Toda petición —sea invocada vía API REST por un ingeniero o generada automáticamente por un **Scheduler**— queda asociada unívocamente a su identidad, rol, aprobación y justificación operativa.
- **Trazabilidad Completa del Ciclo de Vida de la Máquina:** Cada nodo cuenta con una línea de tiempo inmutable desde su aprovisionamiento inicial hasta su baja definitiva. El sistema registra qué playbooks se han ejecutado, qué cambios de configuración se han aplicado, incidencias detectadas y quién intervino en cada etapa.
- **Informes Exhaustivos de Software y Eventos:** La plataforma permite extraer en cualquier instante informes detallados para auditoría interna y reguladores bancarios sobre **qué tiene instalado exactamente cualquier máquina** (versiones de paquetes, parches de seguridad, agentes) y **todo lo que ha sucedido en ella** a lo largo de su historia.

### B. Pipeline Universal de Despliegue por Drivers Multi-Cloud
En lugar de mantener canalizaciones heterogéneas por cada proveedor de infraestructura:

- **Un único contrato de ciclo de vida:** AWS, OpenStack, OpenShift y bare-metal implementan una interfaz abstracta común. El plano de control despacha cargas de trabajo normalizadas con independencia del backend tecnológico.
- **Desacoplamiento total del proveedor:** La lógica de negocio del banco y los sistemas consumidores interactúan con especificaciones abstractas, aislando a la organización de las peculiaridades de cada API de infraestructura.

### C. Pipeline de Configuración Ansible en Dos Capas: Ground y Operación de Usuario
Una vez aprovisionado el recurso computacional a través del driver correspondiente, Orion orquesta la configuración del sistema operativo mediante Ansible dividida en dos fases estrictas y secuenciales:

1. **Capa Ground (Línea Base Obligatoria del Banco):**
    - **Seguridad:** Bastionado del sistema operativo según estándares CIS bancarios, inyección de certificados corporativos, políticas de cortafuegos y gestión de accesos privilegiados.
    - **Monitorización:** Despliegue y configuración automática de agentes corporativos de observabilidad, métricas y recolección de logs.
    - **Paquetería Base:** Configuración de repositorios internos protegidos e instalación de dependencias y utilidades de sistema aprobadas.
    - *Garantía:* Ninguna máquina pasa a la siguiente fase sin que la capa Ground haya concluido con éxito.
2. **Capa de Usuario (Operación Específica):**
    - Ejecución de los playbooks y roles solicitados por el equipo solicitante: aprovisionamiento de middleware, bases de datos, microservicios o dependencias de la aplicación final.

### D. Operaciones Apificadas y Automatización vía Schedulers
La interacción operativa con Orion no depende de intervenciones manuales ni consolas aisladas:

- **Operaciones Apificadas (API-First):** Todo el catálogo de operaciones (creación, remediación, parada, escalado, decomiso, informes) está expuesto mediante una API REST OpenAPI/Swagger, permitiendo su invocación desatendida desde portales de autoservicio, pipelines de CI/CD y motores de orquestación como **Blueprint**.
- **Schedulers Programados:** Orion integra un planificador asíncrono para automatizar operaciones recurrentes: reconciliación periódica de inventario contra las nubes reales, auditorías nocturnas de cumplimiento de líneas base, rotación programada de credenciales y tareas de saneamiento periódico.

### E. Persistencia Híbrida (PostgreSQL + MongoDB + Redis)
- **PostgreSQL** custodia las entidades relacionales que requieren estricta integridad transaccional: permisos RBAC, catálogo de operaciones, estados de tareas y el histórico inmutable de auditoría.
- **MongoDB** almacena documentos polimórficos con el inventario detallado de activos multi-cloud, árboles heterogéneos de metadatos y el registro de paquetes y software instalado en cada nodo.
- **Redis** acelera consultas de lectura frecuentes sobre el inventario y actúa como broker de alta velocidad para las colas de trabajo en Celery.

---

## 5. Trade-Offs de Arquitectura

| Decisión | Alternativa Evaluada | Justificación |
| :--- | :--- | :--- |
| **Ansible en dos capas (Ground + Usuario)** | Playbook monolítico único gestionado por el usuario | Garantiza que el 100% de las máquinas cumplan las normativas de seguridad, bastionado y monitorización bancaria antes de entregar el control al usuario. |
| **Auditoría integral centralizada en Orion** | Trazabilidad delegada en logs efímeros de pipelines | Permite generar informes forenses y de cumplimiento en segundos con el histórico completo de lo instalado y acontecido en cada máquina. |
| **Operaciones apificadas y vía Schedulers** | Ejecuciones manuales por consola o scripts cron aislados | Centraliza permisos, trazabilidad y control de concurrencia bajo el mismo dispatcher HA sin dispersión de automatizaciones. |
| **Híbrido PostgreSQL + MongoDB** | Base de datos relacional única con columnas JSONB | Mantiene integridad relacional estricta para RBAC y auditoría transaccional, con indexación rápida de metadatos e inventario de paquetes heterogéneos. |
| **Abstracción por drivers en Python** | Herramientas y flujos independientes por nube | Unifica RBAC, catálogo de operaciones y auditoría en un solo plano de control agnóstico de proveedor. |

---

## 6. Impacto Operativo

- **Auditoría y trazabilidad completa:** Transformó la preparación de auditorías bancarias de semanas de recopilación manual a consultas automatizadas e instantáneas de cualquier máquina: quién la creó, qué paquetes tiene instalados y su histórico completo de eventos.
- **Seguridad y observabilidad garantizada (Ground):** El 100% de las más de **30.000 máquinas** cuentan con agentes de seguridad y monitorización desplegados y verificados automáticamente desde el momento de su aprovisionamiento.
- **Autoservicio y operaciones masivas:** Más de **500 ingenieros** gestionan su ciclo de vida de infraestructura de forma autónoma, procesando más de **40.000 operaciones diarias** mediante API REST y Schedulers programados.
- **Adopción internacional:** Plataforma implantada y operativa en múltiples geografías del grupo bancario (**España, México y Turquía**).

---

[:octicons-arrow-right-24: Siguiente: Blueprint — Orquestación declarativa de ciclo de vida sobre Orion](blueprint.md)
