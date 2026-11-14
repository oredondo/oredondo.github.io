---
title: "Caso de Estudio: Plataforma IaaS Orion y Pipeline por Drivers"
description: >-
  Arquitectura de alto nivel de la plataforma IaaS central de BBVA — un plano de control en Python/Django que gobierna decenas de miles de nodos en AWS, OpenStack, OpenShift y bare-metal.
---

# Orion: Plataforma IaaS Central y Pipeline Universal por Drivers

| Dimensión | Detalles |
| :--- | :--- |
| **Rol** | Arquitecto Único y Responsable de Plataforma |
| **Organización** | BBVA Technology (Infraestructura Core Banking) · 2017 – Presente |
| **Escala** | 30.000+ máquinas gobernadas · 40.000+ operaciones diarias · 500+ ingenieros |
| **Stack** | Python, Django, DRF, Celery, PostgreSQL, MongoDB, Redis, AWS, OpenStack, OpenShift, F5, Infoblox |

!!! abstract "Resumen de arquitectura"

    Orion es el plano de control central para el gobierno, auditoría y despliegue en autoservicio de infraestructura en la nube híbrida de BBVA. Abstrae cuatro sustratos tecnológicos distintos (**AWS, OpenStack, OpenShift y servidores físicos bare-metal**) tras una única interfaz REST documentada con OpenAPI, combinando un **pipeline universal de despliegue por drivers**, una **capa híbrida de persistencia relacional y documental** y **canalizaciones automáticas de exportación para auditoría**.

---

## 1. La Evolución de Orion: De CMDB e Inventario a Dispatcher de Alta Disponibilidad

Orion no nació como un producto monolítico estático, sino como una respuesta arquitectónica evolutiva a los cuellos de botella reales de escala en **BBVA Technology** — gobernando **más de 30.000 máquinas** en **AWS, OpenStack, OpenShift y bare-metal** y procesando **más de 40.000 operaciones diarias** para **más de 500 ingenieros**:

```mermaid
flowchart TD
    subgraph Origen["1. Origen: CMDB, Inventario y Catálogo Apificado"]
        direction TB
        CMDB["Plano de Control Orion<br/>• Inventario multi-cloud (AWS · OpenStack · OpenShift · Bare-metal)<br/>• Persistencia híbrida (PostgreSQL + MongoDB + Redis)<br/>• Catálogo de operaciones REST (OpenAPI / RBAC)<br/>• Canalizaciones automáticas de auditoría"]
    end

    subgraph Sustitucion["2. Sustitución Estratégica de Jenkins"]
        direction LR
        JNK["Jenkins Legacy<br/>❌ Sin Alta Disponibilidad (SPOF crítico)<br/>❌ UI rígida e inadecuada para operaciones<br/>❌ Muy complejo de mantener, escalar y extender"] -.->|"Sustituido por"| DISP["Dispatcher HA Integrado en Orion<br/>(Django + Celery + Workers en Kubernetes Jobs)<br/>✅ Alta Disponibilidad nativa (HA)<br/>✅ API REST y UI orientada a operaciones<br/>✅ Fácil integración de nuevas funcionalidades"]
    end

    subgraph Expansion["3. Ecosistema Declarativo e IA"]
        direction LR
        BP["Blueprint<br/>(Motor declarativo en YAML, olas DAG y teardown idempotente)"]
        AI["Orion AI (PoC Validada)<br/>(Diagnóstico multi-agente de CI/CD con LangGraph)"]
    end

    CMDB -->|"Evolucionó integrando"| DISP
    DISP --> BP & AI
```

1. **Fase 1 — El Origen: CMDB, Inventario Multi-Cloud y Catálogo Apificado:** Orion nació como un plano de control central para inventariar y catalogar activos heterogéneos sobre AWS, OpenStack, OpenShift y servidores físicos, combinando una base de datos híbrida (PostgreSQL, MongoDB, Redis), permisos RBAC y canalizaciones automáticas de auditoría consumidas directamente por los auditores del banco.
2. **Fase 2 — El Cuello de Botella de Jenkins:** Inicialmente, el disparo de operaciones del catálogo dependía de Jenkins. Sin embargo, Jenkins carecía de Alta Disponibilidad nativa (siendo un punto único de fallo crítico para el banco), su interfaz web estaba diseñada para builds de compilación y no para operaciones de infraestructura, y resultaba muy complejo de operar, escalar e integrar con nuevas funcionalidades y servicios bancarios.
3. **Fase 3 — La Evolución a Dispatcher HA Integrado:** Orion evolucionó absorbiendo el plano de ejecución con un **Dispatcher de Operaciones en Alta Disponibilidad propio (Django + Celery + Kubernetes Jobs)**. Esta migración reemplazó por completo a Jenkins para operaciones de infraestructura, desacopló las variables en runtime (evitando deriva de configuración) y garantizó una arquitectura API-first con ejecución en contenedores efímeros aislados.
4. **Fase 4 — Extensión Declarativa (Blueprint) e IA Operativa (Orion AI):** Con la CMDB y el dispatcher unificados bajo la misma arquitectura, Orion se extendió hacia la orquestación declarativa con **Blueprint** (motor en YAML con dependencias DAG y desmontajes idempotentes sin suites comerciales como Red Hat Automation Platform) y el auto-diagnóstico agéntico con **Orion AI** (LangGraph).

---

## 2. Contexto y Problema de Ingeniería

Operar infraestructura a escala bancaria entre nube pública, nube privada, plataformas de contenedores y centros de datos propios generaba tres cuellos de botella estructurales:

1. **Aprovisionamiento en silos:** Cada entorno destino (AWS, OpenStack, OpenShift, hardware físico) requería sus propias herramientas, credenciales y traspasos manuales por tickets — convirtiendo peticiones sencillas en esperas de varios días.
2. **Auditoría sobre activos heterogéneos:** Los equipos de auditoría interna y cumplimiento normativo exigen instantáneas continuas y verificables de titularidad, líneas base de seguridad y estado de máquinas sobre decenas de miles de activos cuyos esquemas de metadatos son completamente dispares.
3. **Fragilidad ante deprecaciones de fabricantes:** Las plataformas de infraestructura dependen de integraciones oficiales entre proveedores (como los balanceadores F5 con OpenStack) que pueden quedar deprecadas a mitad de ciclo de vida.

---

## 3. Topología Abstracta del Sistema

Orion fue diseñado desde cero para hacer que el proveedor subyacente resulte transparente para los más de 500 ingenieros que lo consumen, centralizando permisos, catálogos de productos, flujos de remediación y trazas de auditoría.

```mermaid
flowchart TD
    subgraph Consumers["Consumidores de Plataforma (500+ Ingenieros)"]
        Portal["Portal de Autoservicio y CLI"]
        BP["Motor Declarativo Blueprint"]
        Systems["Sistemas Core del Banco y CI/CD"]
    end

    subgraph ControlPlane["Plano de Control Orion (Python / Django / DRF)"]
        API["Pasarela REST OpenAPI / Swagger"]
        RBAC["RBAC Centralizado y Catálogo de Productos"]
        Audit["Pipelines Automáticos de Auditoría (CSV / Informes)"]
        Coord["Coordinador Asíncrono de Operaciones (Celery)"]
        API --> RBAC --> Coord
        RBAC --> Audit
    end

    subgraph DataTier["Capa Híbrida de Persistencia y Mensajería"]
        PG[("PostgreSQL<br/>Estado transaccional, RBAC y pista inmutable de auditoría")]
        Mongo[("MongoDB<br/>Inventario polimórfico multi-cloud de activos")]
        Redis[("Redis<br/>Caché rápida de consultas y broker Celery")]
    end

    subgraph DriverLayer["Pipeline Universal de Despliegue por Drivers"]
        AWS_D["Driver AWS"]
        OS_D["Driver OpenStack"]
        F5_B["Puente REST a medida F5 ↔ OpenStack"]
        OSH_D["Driver OpenShift"]
        BM_D["Driver Bare-Metal / On-Prem"]
    end

    Consumers --> API
    Coord <--> PG & Mongo & Redis
    Audit <-- "Consultas analíticas de alto volumen" --- PG & Mongo
    Coord --> AWS_D & OS_D & OSH_D & BM_D
    OS_D <--> F5_B
```

---

## 4. Decisiones Clave de Arquitectura

### A. Persistencia Híbrida (PostgreSQL + MongoDB + Redis)
Un único motor de base de datos no podía resolver simultáneamente el cumplimiento bancario estricto y las consultas masivas de inventario multi-cloud:

- **PostgreSQL** custodia las entidades relacionales que exigen integridad transaccional: permisos (RBAC), catálogos de productos, transiciones de estado de operaciones y registros inmutables de auditoría.
- **MongoDB** ingiere documentos polimórficos de activos sobre decenas de miles de máquinas (donde una instancia EC2 de AWS, una VM de OpenStack, un proyecto de OpenShift y un servidor físico tienen árboles de atributos totalmente distintos) y los indexa para consultas masivas de inventario.
- **Redis** acelera las lecturas frecuentes y respalda las colas de tareas asíncronas en Celery para que la API responda al instante mientras las operaciones pesadas se ejecutan en segundo plano.

### B. Pipeline Universal de Despliegue por Drivers
En lugar de mantener canalizaciones independientes por cada nube, el motor de despliegue se articula en torno a una **interfaz abstracta de drivers**:

- **Un único contrato, backends intercambiables:** Cada sabor de infraestructura (AWS, OpenStack, OpenShift, bare-metal) implementa una interfaz común de ciclo de vida. La plataforma despacha la misma carga útil normalizada sin importar el destino.
- **Estándares corporativos de despliegue:** Más allá del código, este diseño definió la filosofía estándar de despliegue en la organización — permitiendo a los equipos de desarrollo llevar artefactos a producción de forma autónoma sin intervención manual del equipo de infraestructura.

### C. Escudo frente a Deprecaciones de Fabricante sin Downtime (Puente F5 / OpenStack)
Cuando la integración nativa oficial entre los balanceadores **F5** y **OpenStack** fue deprecada, depender directamente de plugins de terceros habría obligado a una migración disruptiva en producción. Gracias a que la capa de drivers de Orion ya aislaba las llamadas externas, diseñé e implementé un **puente API RESTful a medida** entre F5 y OpenStack detrás del límite del driver — restaurando la interoperabilidad completa de balanceo automatizado con **cero tiempo de inactividad (zero downtime)**.

### D. Pipelines Automatizados de Auditoría y Cumplimiento
En vez de tratar las auditorías como una recopilación manual de datos previa a cada inspección, Orion ejecuta canalizaciones automáticas de exportación que agregan datos operativos de MongoDB y PostgreSQL en informes estructurados (pipelines CSV) consumidos directamente por auditores internos y responsables de gobierno.

---

## 5. Trade-Offs de Arquitectura

| Decisión | Alternativa Evaluada | Justificación |
| :--- | :--- | :--- |
| **Híbrido PostgreSQL + MongoDB** | Base de datos relacional única con JSONB | Mantuvo integridad relacional estricta para permisos y auditoría, permitiendo a la vez indexación de alta velocidad sobre esquemas de metadatos cloud muy heterogéneos. |
| **Abstracción por drivers en Python** | Pipelines independientes por proveedor cloud | Unificó RBAC, catálogo de productos y trazabilidad en un solo plano de control; añadir un entorno es modular y aditivo. |
| **Puente REST propio F5/OpenStack** | Migración completa de plataforma de balanceo | Preservó la continuidad operativa y evitó cualquier corte de servicio cuando el fabricante deprecó la integración nativa. |

---

## 6. Impacto Operativo

- **Autoservicio a gran escala:** Permitió a **más de 500 ingenieros** aprovisionar, gobernar y remediar infraestructura de forma autónoma sobre **decenas de miles de nodos**, reduciendo los tiempos de entrega de días de tickets manuales a minutos.
- **Auditoría continua:** Sustituyó la extracción manual de evidencias por canalizaciones automáticas y verificables consumidas directamente por los equipos de cumplimiento.
- **Adopción internacional:** Desplegado e integrado con equipos de ingeniería en **España, México y Turquía**, liderando sesiones de onboarding técnico y extensiones específicas para flujos regionales.

---

[:octicons-arrow-right-24: Siguiente: Blueprint — Orquestación declarativa de ciclo de vida sobre Orion](blueprint.md)
