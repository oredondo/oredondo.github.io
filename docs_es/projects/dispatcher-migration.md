---
title: "Caso de Estudio: De Jenkins a Dispatcher HA y Ejecución K8s"
description: >-
  Cómo evolucionamos desde Jenkins Shared Libraries hacia un Dispatcher de Operaciones en Alta Disponibilidad con Django/Celery, inyección dinámica de configuración y ejecución efímera en Kubernetes Jobs.
---

# Dejar Jenkins Atrás a Gran Escala: Dispatcher HA, Configuración en Runtime y Ejecución en K8s

| Dimensión | Detalles |
| :--- | :--- |
| **Rol** | Arquitecto Principal de Plataforma |
| **Organización** | BBVA (Infraestructura Core Banking) |
| **Alcance** | Sustitución de Jenkins como motor de ejecución de infraestructura; unificación de gestión de configuración y ejecución efímera en Kubernetes |
| **Stack** | Python, Django, DRF, Celery, Redis, PostgreSQL, Kubernetes Jobs, Ansible, Groovy |

!!! abstract "Resumen de arquitectura"

    Antes de que una plataforma interna pueda escalar a decenas de miles de operaciones diarias, su plano de ejecución debe ser fiable, gobernado por API y sin estado (*stateless*) en los nodos trabajadores. Este caso de estudio aborda una evolución arquitectónica en cuatro etapas: estandarizar pipelines con **Jenkins Shared Libraries**, superar los límites de Jenkins migrando a un **Dispatcher de Operaciones en Alta Disponibilidad (Django + Celery)**, desacoplar las variables de entorno mediante un **Sistema Centralizado de Gestión de Configuración** y aislar la ejecución en **Kubernetes Jobs**.

---

## 1. La Evolución: Por Qué Fueron Necesarias las Jenkins Shared Libraries — y Por Qué las Superamos

### Etapa 1: Estandarización con Jenkins Shared Libraries
Inicialmente, distintos equipos de infraestructura mantenían `Jenkinsfiles` duplicados y heterogéneos en múltiples repositorios. Diseñé un **framework modular de Jenkins Shared Libraries en Groovy** que se convirtió en el estándar CI/CD de varios equipos de infraestructura — reduciendo drásticamente la duplicación de código y el tiempo de incorporación de ingenieros.

Sin embargo, unificar la ejecución sobre un framework común también nos dio la visibilidad necesaria para detectar **dónde el propio Jenkins se convertía en el cuello de botella** al utilizarse como orquestador de operaciones de infraestructura a escala bancaria:

- **Fragilidad del controlador central:** Las ejecuciones masivas en paralelo saturaban el controlador central de Jenkins y la serialización de estado CPS en Groovy.
- **Control programático limitado:** Lanzar, reintentar y auditar miles de operaciones diarias a través de la API de Jenkins carecía de un modelo de estado relacional limpio y de mecanismos granulares de contrapresión (*back-pressure*).
- **Deriva en nodos estáticos:** Los agentes de ejecución permanentes acumulaban estado residual y conflictos de dependencias entre trabajos.

---

## 2. Arquitectura Objetivo: Dispatcher HA + Gestión de Configuración + Kubernetes Jobs

Para eliminar a Jenkins como cuello de botella operativo, separamos **planificación y estado** (Dispatcher HA), **variables de entorno** (Sistema de Gestión de Configuración) y **aislamiento de cómputo** (Motor de Ejecución sobre Kubernetes Jobs):

```mermaid
flowchart LR
    subgraph Callers["Consumidores de Plataforma"]
        Orion["Plano de Control Orion"]
        BP["Orquestador Blueprint"]
        Engineers["CI/CD e Ingenieros"]
    end

    subgraph Dispatcher["Dispatcher HA de Operaciones (Django + Celery)"]
        API["Interfaz REST OpenAPI"]
        State[("Estado Duradero de Operaciones<br/>(PostgreSQL + Redis)")]
        Sched["Pools de Workers HA y Motor de Reintentos"]
        API --> State --> Sched
    end

    subgraph Config["Gestión Centralizada de Configuración"]
        VarStore["Almacén de Variables por Entorno<br/>(Dev · Staging · Prod)"]
        Injector["Resolvedor Dinámico en Runtime"]
        VarStore --> Injector
    end

    subgraph Execution["Plano de Ejecución Efímera"]
        K8s["Motor de Ejecución en Kubernetes Jobs<br/>(Pods efímeros aislados)"]
        Ansible["Roles Ansible Agnósticos de Entorno<br/>(GitLab · Artifactory · Servicios Core)"]
    end

    Callers -->|"Disparo programático y consulta"| API
    Sched -->|"Despacha operación"| K8s
    Injector -->|"Inyecta variables del entorno en runtime"| K8s
    K8s -->|"Ejecuta carga inmutable"| Ansible
    K8s -.->|"Transmite logs y estado final"| State
```

---

## 3. Pilares Técnicos Fundamentales

### A. Dispatcher de Operaciones en Alta Disponibilidad (Django + Celery)
Sustituimos por completo el modelo de ejecución basado en librerías de Jenkins por un **Dispatcher de Operaciones** propio desplegado en Alta Disponibilidad:

- **Diseño API-first (OpenAPI):** Cada operación se lanza, inspecciona y monitoriza mediante un contrato REST documentado con Swagger/OpenAPI en lugar de depender de trabajos orientados a interfaz web.
- **Control total del flujo y políticas de reintento:** Desacoplar la planificación de la ejecución permitió definir políticas de reintento a medida, priorización de colas y observabilidad granular paso a paso.
- **Migración sin cortes de servicio:** Al controlar ya la interfaz de las librerías compartidas que consumían los equipos, migramos las cargas progresivamente de Jenkins al dispatcher en Django/Celery sin interrumpir las operaciones del banco.

### B. Sistema Centralizado de Gestión de Configuración
Una fuente clásica de incidentes en infraestructura consiste en copiar playbooks entre ramas `dev`, `staging` y `prod` modificando variables manualmente.

- **Separación estricta entre lógica y configuración:** Construimos un Sistema Centralizado de Gestión de Configuración que desacopla por completo la administración de variables de la lógica de automatización.
- **Resolución dinámica en tiempo de despliegue:** Los ingenieros escriben **roles de Ansible 100% agnósticos del entorno** (incluyendo toda la automatización que gobierna los clusters internos de **GitLab, Artifactory y Jenkins** del banco). En el momento del despliegue, el sistema resuelve el entorno destino e inyecta automáticamente las variables correspondientes — eliminando repositorios duplicados y erradicando la deriva de configuración (*configuration drift*).

### C. Motor de Ejecución sobre Kubernetes Jobs
En lugar de ejecutar automatizaciones como procesos pesados sobre servidores estáticos compartidos, extendimos el pipeline de despliegue para ejecutar las operaciones mediante **Kubernetes Jobs**:

- **Aislamiento efímero:** Cada operación nace como un contenedor aislado de corta duración dentro del cluster con sus dependencias exactas y las variables de entorno inyectadas en runtime.
- **Ciclo de vida limpio:** En cuanto la operación concluye y envía su telemetría y traza de auditoría a la plataforma, el pod se destruye — garantizando cero estado residual entre ejecuciones.

---

## 4. Trade-Offs de Arquitectura

| Decisión | Alternativa Evaluada | Justificación |
| :--- | :--- | :--- |
| **Migrar de Jenkins a un Dispatcher HA propio en Django/Celery** | Escalar múltiples controladores de Jenkins | Eliminó los cuellos de botella del controlador JVM, los límites de serialización CPS en Groovy y la fragilidad de plugins; aportó control nativo por API en Python y estado relacional. |
| **Inyección de variables en runtime desde un servicio central** | Ramas Git o carpetas de inventario por entorno | Evitó duplicar configuraciones entre repositorios y garantizó que exactamente el mismo rol probado se ejecute en dev, staging y producción. |
| **Kubernetes Jobs efímeros por operación** | Máquinas virtuales trabajadoras estáticas | Eliminó la deriva de entorno, los conflictos de librerías y la contención de recursos entre ejecuciones concurrentes. |

---

[:octicons-arrow-left-24: Anterior: Motor Blueprint](blueprint.md) · [:octicons-arrow-right-24: Siguiente: Orion AI — Diagnóstico Agéntico CI/CD (PoC Validada)](orion-ai.md)
