---
title: Ecosistema de Plataforma y Proyectos de Ingeniería
description: >-
  Resumen a vuela pluma y catálogo completo de plataformas de despliegue, motores declarativos IaC, subsistemas de infraestructura y proyectos open-source.
---

# Ecosistema de Plataforma y Proyectos de Ingeniería

Durante más de una década he diseñado y evolucionado sistemas de plataforma, herramientas de infraestructura como código (IaC), planos de control multi-cloud y aplicaciones con inteligencia artificial aplicada.

---

### Resumen del Ecosistema a Vuela Pluma

El trabajo de ingeniería recogido en este portal se articula en torno a tres grandes pilares tecnológicos:

1. **Plataformas de Infraestructura Bancaria (BBVA):** Diseñadas para resolver la gobernanza de más de **30.000 máquinas** y **40.000 operaciones diarias**. Destacan **Orion** (plano de control IaaS que evolucionó de CMDB apificada a dispatcher en alta disponibilidad reemplazando a Jenkins), **Blueprint** (motor declarativo en YAML que orquesta despliegues mediante olas DAG y teardown idempotente) e iniciativas de IA operativa como **Orion AI** (LangGraph).
2. **Subsistemas Críticos de Red y Automatización:** Soluciones de ingeniería creadas para blindar la continuidad de negocio frente a obsolescencias técnicas (como el **puente REST a medida F5/OpenStack** desplegado con *zero downtime* tras la deprecación del soporte oficial), servicios de **gestión dinámica de configuración** y plataformas de almacenamiento masivo en nubes privadas con **OpenStack Swift y Ceph**.
3. **Sistemas Open-Source e I+D Personal en GitHub:** Herramientas públicas donde aplico optimizaciones multimedia de bajo nivel en **FFmpeg** (compresión H.264 stillimage a 10 FPS con ahorro del 70%, sincronización de reloj PTS y filtrado espectral en **OmniLecture Studio**), transcripción Whisper de doble motor, y arquitecturas RAG contextuales con **PostgreSQL (`pgvector`) y Django 6** en **WrenchBuddy**.

<div class="grid cards" markdown>

-   :material-server-network:{ .lg .middle } __Plataformas Enterprise & Control Plane__

    ---

    Planos de control de despliegue, motores declarativos estilo IaC y sustitución de monolitos CI/CD para operar más de 30.000 máquinas y 40.000 operaciones diarias en banca sin puntos únicos de fallo (SPOF).

    [:octicons-arrow-down-24: Ver plataformas corporativas](#casos-de-estudio-corporativos)

-   :material-lan-connect:{ .lg .middle } __Subsistemas de Red y Automatización__

    ---

    Puentes REST a medida para sortear deprecaciones de fabricante (F5 / OpenStack) con zero downtime, inyección dinámica de configuración en runtime y almacenamiento en OpenStack Swift / Ceph.

    [:octicons-arrow-down-24: Ver subsistemas](#subsistemas-de-plataforma)

-   :material-robot-industrial:{ .lg .middle } __Open-Source, FFmpeg e IA Aplicada__

    ---

    Desarrollo nativo en Linux/GTK con pipelines multimedia optimizados en FFmpeg (H.264 stillimage, PTS sync), transcripción Whisper y arquitecturas RAG con PostgreSQL, `pgvector` y LangChain.

    [:octicons-arrow-down-24: Ver proyectos open-source](#proyectos-open-source)

</div>

---

## 1. Casos de Estudio de Arquitectura Corporativa {: #casos-de-estudio-corporativos }

<div class="grid cards two-col" markdown>

-   :material-cloud-cog-outline:{ .lg .middle } __[Orion — Plataforma IaaS Central y Pipeline por Drivers](orion-iaas.md)__

    ---

    Arquitecto y responsable del plano de control IaaS y despliegue: una sola interfaz OpenAPI que gobierna 30.000+ máquinas en AWS, OpenStack, OpenShift y bare-metal (40.000+ operaciones diarias), respaldada por una capa híbrida PostgreSQL + MongoDB + Redis y canalizaciones automáticas de auditoría.

    <span class="tech-tag">Python</span><span class="tech-tag">Django REST</span><span class="tech-tag">Celery</span><span class="tech-tag">PostgreSQL</span><span class="tech-tag">MongoDB</span><span class="tech-tag">Redis</span>

    [:octicons-arrow-right-24: Arquitectura y trade-offs](orion-iaas.md)

-   :material-file-tree-outline:{ .lg .middle } __[Blueprint — Motor Declarativo de Ciclo de Vida](blueprint.md)__

    ---

    Motor de orquestación asíncrono en Python guiado por planos YAML versionados. Calcula grafos DAG de ejecución, reconcilia contra el estado en vivo de Orion y reanuda destrucciones interrumpidas de forma idempotente — eliminando licencias comerciales.

    <span class="tech-tag">Python</span><span class="tech-tag">AsyncIO</span><span class="tech-tag">Planificación DAG</span><span class="tech-tag">YAML Declarativo</span><span class="tech-tag">GitOps</span>

    [:octicons-arrow-right-24: Arquitectura y trade-offs](blueprint.md)

-   :material-cached:{ .lg .middle } __[Dejar Jenkins Atrás — Dispatcher HA y Ejecución K8s](dispatcher-migration.md)__

    ---

    Cómo migramos desde los cuellos de botella de Jenkins hacia un Dispatcher de Operaciones en Alta Disponibilidad (Django + Celery), inyección dinámica de configuración en runtime y ejecución efímera en Kubernetes Jobs.

    <span class="tech-tag">Django</span><span class="tech-tag">Celery</span><span class="tech-tag">Kubernetes Jobs</span><span class="tech-tag">Ansible</span><span class="tech-tag">OpenAPI</span>

    [:octicons-arrow-right-24: Arquitectura y trade-offs](dispatcher-migration.md)

-   :material-radar:{ .lg .middle } __[Orion AI — Diagnóstico Agéntico CI/CD (PoC Validada)](orion-ai.md)__

    ---

    Prototipo multi-agente en LangGraph + ReAct que correlaciona logs de pipelines, runbooks indexados en Redis y diffs de GitLab bajo guardarraíles deterministas — junto con un análisis honesto de las barreras reales de paso a producción en banca.

    <span class="tech-tag">LangGraph</span><span class="tech-tag">ReAct</span><span class="tech-tag">MCP</span><span class="tech-tag">Qwen 131k</span><span class="tech-tag">Guardarraíles Deterministas</span>

    [:octicons-arrow-right-24: Arquitectura y lecciones de rollout](orion-ai.md)

</div>

---

## 2. Subsistemas de Plataforma y Automatización de Infraestructura {: #subsistemas-de-plataforma }

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

## 3. Proyectos Open-Source e I+D Personal {: #proyectos-open-source }

Sistemas públicos construidos fuera de las restricciones bancarias — con código fuente completo disponible en GitHub:

<div class="grid cards two-col" markdown>

-   :material-waveform:{ .lg .middle } __[OmniLecture Studio — Suite Multimodal de IA para Linux](omni-lecture.md)__

    ---

    Grabador nativo de pantalla/audio para Linux (Wayland/GNOME, GTK 3) con pipeline multimedia en FFmpeg (compresión H.264 a 10 FPS con `-tune stillimage` que ahorra hasta un 70% de espacio en disco, sincronización de reloj PTS y filtrado espectral `afftdn`) y flujos en LangGraph. Combina Whisper de doble motor (`faster-whisper` CPU `int8` + API cloud), OCR de diapositivas y manuscritos con OpenCV CLAHE + Tesseract y guardarraíles anti-alucinación para generar grafos de conocimiento interconectados en Markdown y mazos Anki.

    <span class="tech-tag">Python 3.12</span><span class="tech-tag">GTK 3 / PyGObject</span><span class="tech-tag">FFmpeg</span><span class="tech-tag">faster-whisper</span><span class="tech-tag">LangGraph</span><span class="tech-tag">OpenCV</span>

    [:octicons-arrow-right-24: Caso de estudio](omni-lecture.md) · [:fontawesome-brands-github: Repositorio GitHub](https://github.com/oredondo/omnilecture-studio)

-   :material-wrench-outline:{ .lg .middle } __[WrenchBuddy — Plataforma IA de Mantenimiento y RAG con pgvector](wrenchbuddy.md)__

    ---

    Plataforma full-stack de ciclo de vida de vehículos construida con **Django 6, DRF, PostgreSQL (`pgvector`), Celery, Redis y LangChain** (más un frontend en TypeScript). Utiliza visión/OCR para extraer facturas de taller y RAG vectorial de 768 dimensiones sobre manuales técnicos para alimentar un asistente mecánico contextual.

    <span class="tech-tag">Django 6</span><span class="tech-tag">PostgreSQL / pgvector</span><span class="tech-tag">LangChain</span><span class="tech-tag">Celery / Redis</span><span class="tech-tag">TypeScript</span>

    [:octicons-arrow-right-24: Caso de estudio](wrenchbuddy.md) · [:fontawesome-brands-github: Backend](https://github.com/oredondo/WrenchBuddy) · [:fontawesome-brands-github: Frontend](https://github.com/oredondo/WrenchBuddy-frontend)

</div>
