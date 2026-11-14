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
| **Escala** | Decenas de miles de nodos · Operaciones diarias de alto rendimiento · 500+ ingenieros |
| **Stack** | Python, Django, DRF, Celery, PostgreSQL, MongoDB, Redis, AWS, OpenStack, OpenShift, F5, Infoblox |

!!! abstract "Resumen de arquitectura"

    Orion es el plano de control central para el gobierno, auditoría y despliegue en autoservicio de infraestructura en la nube híbrida de BBVA. Abstrae cuatro sustratos tecnológicos distintos (**AWS, OpenStack, OpenShift y servidores físicos bare-metal**) tras una única interfaz REST documentada con OpenAPI, combinando un **pipeline universal de despliegue por drivers**, una **capa híbrida de persistencia relacional y documental** y **canalizaciones automáticas de exportación para auditoría**.

---

## 1. Contexto y Problema de Ingeniería

Operar infraestructura a escala bancaria entre nube pública, nube privada, plataformas de contenedores y centros de datos propios generaba tres cuellos de botella estructurales:

1. **Aprovisionamiento en silos:** Cada entorno destino (AWS, OpenStack, OpenShift, hardware físico) requería sus propias herramientas, credenciales y traspasos manuales por tickets — convirtiendo peticiones sencillas en esperas de varios días.
2. **Auditoría sobre activos heterogéneos:** Los equipos de auditoría interna y cumplimiento normativo exigen instantáneas continuas y verificables de titularidad, líneas base de seguridad y estado de máquinas sobre decenas de miles de activos cuyos esquemas de metadatos son completamente dispares.
3. **Fragilidad ante deprecaciones de fabricantes:** Las plataformas de infraestructura dependen de integraciones oficiales entre proveedores (como los balanceadores F5 con OpenStack) que pueden quedar deprecadas a mitad de ciclo de vida.

---

## 2. Topología Abstracta del Sistema

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

## 3. Decisiones Clave de Arquitectura

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

## 4. Trade-Offs de Arquitectura

| Decisión | Alternativa Evaluada | Justificación |
| :--- | :--- | :--- |
| **Híbrido PostgreSQL + MongoDB** | Base de datos relacional única con JSONB | Mantuvo integridad relacional estricta para permisos y auditoría, permitiendo a la vez indexación de alta velocidad sobre esquemas de metadatos cloud muy heterogéneos. |
| **Abstracción por drivers en Python** | Pipelines independientes por proveedor cloud | Unificó RBAC, catálogo de productos y trazabilidad en un solo plano de control; añadir un entorno es modular y aditivo. |
| **Puente REST propio F5/OpenStack** | Migración completa de plataforma de balanceo | Preservó la continuidad operativa y evitó cualquier corte de servicio cuando el fabricante deprecó la integración nativa. |

---

## 5. Impacto Operativo

- **Autoservicio a gran escala:** Permitió a **más de 500 ingenieros** aprovisionar, gobernar y remediar infraestructura de forma autónoma sobre **decenas de miles de nodos**, reduciendo los tiempos de entrega de días de tickets manuales a minutos.
- **Auditoría continua:** Sustituyó la extracción manual de evidencias por canalizaciones automáticas y verificables consumidas directamente por los equipos de cumplimiento.
- **Adopción internacional:** Desplegado e integrado con equipos de ingeniería en **España, México y Turquía**, liderando sesiones de onboarding técnico y extensiones específicas para flujos regionales.

---

[:octicons-arrow-right-24: Siguiente: Blueprint — Orquestación declarativa de ciclo de vida sobre Orion](blueprint.md)
