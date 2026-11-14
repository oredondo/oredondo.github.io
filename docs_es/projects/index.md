---
title: Ecosistema de Plataforma y Casos de Estudio
description: >-
  Cómo encajan diez años de ingeniería de plataformas — desde almacenamiento en OpenStack/Ceph y librerías compartidas en Jenkins hasta dispatchers HA propios, pipelines por drivers, Orion, Blueprint e IA aplicada.
---

# Ecosistema de Plataforma y Casos de Estudio

Las grandes plataformas rara vez nacen en una pizarra en blanco en una sola tarde. Evolucionan **capa por capa** a medida que las herramientas existentes tocan su techo de escalabilidad, las integraciones de fabricantes quedan deprecadas y el gobierno manual deja de escalar.

Esta sección muestra cómo los sistemas que he diseñado durante la última década se conectan en una única trayectoria coherente de ingeniería — seguida de los casos de estudio en profundidad y mis proyectos open-source en GitHub.

---

## 1. La Evolución de Orion: De CMDB e Inventario a Dispatcher de Alta Disponibilidad

En **BBVA Technology** (2017 – Presente), **Orion** no nació como un producto estático, sino como una respuesta evolutiva a los cuellos de botella reales de escala bancaria — gobernando **más de 30.000 máquinas** en **AWS, OpenStack, OpenShift y bare-metal** y procesando **más de 40.000 operaciones diarias** para **más de 500 ingenieros**:

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
2. **Fase 2 — El Cuello de Botella de Jenkins:** Inicialmente, el disparo de operaciones del catálogo dependía de Jenkins. Sin embargo, Jenkins carecía de Alta Disponibilidad nativa (siendo un punto único de fallo crítico para el banco), su interfaz web estaba diseñada para builds de software y no para operaciones de infraestructura, y resultaba muy complejo de operar, escalar e integrar con nuevas funcionalidades y servicios bancarios.
3. **Fase 3 — La Evolución a Dispatcher HA Integrado:** Orion evolucionó absorbiendo el plano de ejecución con un **Dispatcher de Operaciones en Alta Disponibilidad propio (Django + Celery + Kubernetes Jobs)**. Esta migración reemplazó por completo a Jenkins para operaciones de infraestructura, desacopló las variables en runtime (evitando deriva de configuración) y garantizó una arquitectura API-first con ejecución en contenedores efímeros aislados.
4. **Fase 4 — Extensión Declarativa (Blueprint) e IA Operativa (Orion AI):** Con la CMDB y el dispatcher unificados bajo la misma arquitectura, Orion se extendió hacia la orquestación declarativa con **Blueprint** (motor en YAML con dependencias DAG y desmontajes idempotentes sin suites comerciales como Red Hat Automation Platform) y el auto-diagnóstico agéntico con **Orion AI** (LangGraph).

---

## 2. Casos de Estudio de Arquitectura Corporativa

<div class="grid cards two-col" markdown>

-   :material-cloud-cog-outline:{ .lg .middle } __[Orion — Plataforma IaaS Central y Pipeline por Drivers](orion-iaas.md)__

    ---

    Arquitecto único del plano de control IaaS y despliegue: una sola interfaz OpenAPI que gobierna 30.000+ máquinas en AWS, OpenStack, OpenShift y bare-metal (40.000+ operaciones diarias), respaldada por una capa híbrida PostgreSQL + MongoDB + Redis y canalizaciones automáticas de auditoría.

    [:octicons-arrow-right-24: Arquitectura y trade-offs](orion-iaas.md)

-   :material-file-tree-outline:{ .lg .middle } __[Blueprint — Motor Declarativo de Ciclo de Vida](blueprint.md)__

    ---

    Motor de orquestación asíncrono en Python guiado por planos YAML versionados. Calcula grafos DAG de ejecución, reconcilia contra el estado en vivo de Orion y reanuda destrucciones interrumpidas de forma idempotente — eliminando licencias comerciales.

    [:octicons-arrow-right-24: Arquitectura y trade-offs](blueprint.md)

-   :material-cached:{ .lg .middle } __[Dejar Jenkins Atrás — Dispatcher HA y Ejecución K8s](dispatcher-migration.md)__

    ---

    Cómo migramos desde los cuellos de botella de Jenkins hacia un Dispatcher de Operaciones en Alta Disponibilidad (Django + Celery), inyección dinámica de configuración en runtime y ejecución efímera en Kubernetes Jobs.

    [:octicons-arrow-right-24: Arquitectura y trade-offs](dispatcher-migration.md)

-   :material-radar:{ .lg .middle } __[Orion AI — Diagnóstico Agéntico CI/CD (PoC Validada)](orion-ai.md)__

    ---

    Prototipo multi-agente en LangGraph + ReAct que correlaciona logs de pipelines, runbooks indexados en Redis y diffs de GitLab bajo guardarraíles deterministas — junto con un análisis honesto de las barreras reales de paso a producción en banca.

    [:octicons-arrow-right-24: Arquitectura y lecciones de rollout](orion-ai.md)

</div>

---

## 3. Subsistemas de Plataforma y Proyectos Previos de Infraestructura

Además de los cuatro análisis en profundidad anteriores, estos subsistemas constituyeron piezas clave de la arquitectura:

<div class="grid cards two-col" markdown>

-   :material-swap-horizontal-bold:{ .lg .middle } __Puente API REST F5 / OpenStack (BBVA)__

    ---

    **Problema:** La integración nativa de balanceadores F5 con OpenStack fue deprecada oficialmente, amenazando la automatización del balanceo de tráfico en entornos bancarios.
    
    **Solución:** Diseñé e implementé un puente API RESTful a medida en Python que restauró la interoperabilidad completa entre F5 y OpenStack. Desplegado con **cero tiempo de inactividad (zero downtime)**, evitando una migración disruptiva de plataforma.

-   :material-tune-variant:{ .lg .middle } __Sistema Centralizado de Gestión de Configuración (BBVA)__

    ---

    **Problema:** Las variables específicas de entorno acopladas dentro de los playbooks de Ansible provocaban repositorios duplicados y deriva de configuración entre desarrollo, staging y producción.
    
    **Solución:** Construí un servicio centralizado que desacopla la gestión de variables de la lógica de los playbooks, resolviendo e inyectando dinámicamente las variables del entorno destino en tiempo de despliegue.

-   :material-dharmachakra:{ .lg .middle } __Motor de Ejecución sobre Kubernetes Jobs (BBVA)__

    ---

    **Problema:** Ejecutar automatizaciones pesadas y campañas de validación sobre nodos estáticos de larga duración generaba contención de recursos y deriva de entorno.
    
    **Solución:** Extendí el pipeline de despliegue para ejecutar cualquier operación de infraestructura como un **Kubernetes Job** efímero y aislado, inyectando variables en tiempo de ejecución y enviando telemetría al sistema central.

-   :material-server-security:{ .lg .middle } __Gobierno de Servicios Core con Ansible (BBVA)__

    ---

    **Alcance:** Propietario y mantenedor de la base de código Ansible agnóstica de entorno que aprovisiona y configura las plataformas internas críticas de desarrollo de BBVA — incluyendo clusters de **GitLab, Artifactory y Jenkins** — consumiendo variables automáticamente del Sistema de Gestión de Configuración.

-   :material-source-branch:{ .lg .middle } __Framework de Jenkins Shared Libraries (BBVA)__

    ---

    **Alcance:** Desarrollé librerías compartidas modulares en Groovy y plantillas reutilizables de pipelines que se convirtieron en el estándar CI/CD de múltiples equipos de infraestructura, reduciendo la duplicación y sentando las bases operativas que motivaron después la migración al Dispatcher HA propio.

-   :material-harddisk:{ .lg .middle } __Plataforma de Almacenamiento en Nube Privada sobre OpenStack Swift (Oesia · 2015–2017)__

    ---

    **Alcance:** Administré una nube privada en producción basada en **OpenStack y almacenamiento distribuido Ceph**, y desarrollé una aplicación corporativa de almacenamiento y compartición de archivos (equivalente funcional a Dropbox) en Python sobre el almacenamiento de objetos **OpenStack Swift**.

</div>

---

## 4. Proyectos Open-Source e I+D Personal

Sistemas públicos construidos fuera de las restricciones bancarias — con código fuente completo disponible en GitHub:

<div class="grid cards two-col" markdown>

-   :material-waveform:{ .lg .middle } __[OmniLecture Studio — Suite Multimodal de IA para Linux](omni-lecture.md)__

    ---

    Grabador nativo de pantalla/audio para Linux (Wayland/GNOME, GTK 3) con pipeline multimedia en FFmpeg (compresión H.264 a 10 FPS con `-tune stillimage` que ahorra hasta un 70% de espacio en disco, sincronización de reloj PTS y filtrado espectral `afftdn`) y flujos en LangGraph. Combina Whisper de doble motor (`faster-whisper` CPU `int8` + API cloud), OCR de diapositivas y manuscritos con OpenCV CLAHE + Tesseract y guardarraíles anti-alucinación para generar apuntes Markdown, documentos `.docx` y mazos Anki.

    [:octicons-arrow-right-24: Caso de estudio](omni-lecture.md) · [:fontawesome-brands-github: Repositorio GitHub](https://github.com/oredondo/omnilecture-studio)

-   :material-wrench-outline:{ .lg .middle } __[WrenchBuddy — Plataforma IA de Mantenimiento y RAG con pgvector](wrenchbuddy.md)__

    ---

    Plataforma full-stack de ciclo de vida de vehículos construida con **Django 6, DRF, PostgreSQL (`pgvector`), Celery, Redis y LangChain** (más un frontend en TypeScript). Utiliza visión/OCR para extraer facturas de taller y RAG vectorial de 768 dimensiones sobre manuales técnicos para alimentar un asistente mecánico contextual.

    [:octicons-arrow-right-24: Caso de estudio](wrenchbuddy.md) · [:fontawesome-brands-github: Backend](https://github.com/oredondo/WrenchBuddy) · [:fontawesome-brands-github: Frontend](https://github.com/oredondo/WrenchBuddy-frontend)

</div>
