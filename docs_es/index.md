---
title: Senior Platform Engineer · Python
description: >-
  Oscar Redondo — Senior Platform Engineer · Python con más de 10 años diseñando
  plataformas de despliegue de infraestructura, motores propios de IaC e IA operativa a gran escala.
hide:
  - navigation
  - toc
  - feedback
---

<div class="hero" markdown>

<p class="hero__eyebrow">Senior Platform Engineer · Python · Madrid, España</p>

# Oscar Redondo { .hero__title }

<p class="hero__lead">
Diseño y construyo <strong>plataformas de despliegue y aprovisionamiento de infraestructura impulsadas por una filosofía propia de Infrastructure as Code</strong> — haciendo invisible la complejidad distribuida de AWS, OpenStack, OpenShift y bare-metal mediante APIs en autoservicio, motores declarativos de ciclo de vida y automatización determinista.
</p>

[:material-sitemap-outline: Explorar arquitectura y proyectos](projects/index.md){ .md-button .md-button--primary }
[:material-newspaper-variant-outline: Leer ensayos técnicos](blog/index.md){ .md-button }
[:material-file-account-outline: Ver mi CV](cv/index.md){ .md-button }

</div>

<div class="kpi-grid">
  <div class="kpi-card">
    <span class="kpi-value">30.000+</span>
    <span class="kpi-label">Máquinas gobernadas</span>
  </div>
  <div class="kpi-card">
    <span class="kpi-value">40.000+</span>
    <span class="kpi-label">Operaciones diarias</span>
  </div>
  <div class="kpi-card">
    <span class="kpi-value">500+</span>
    <span class="kpi-label">Ingenieros servidos</span>
  </div>
  <div class="kpi-card">
    <span class="kpi-value">10+ años</span>
    <span class="kpi-label">Plataformas y Python</span>
  </div>
</div>

## Filosofía de Ingeniería de Plataforma

*Tres principios arquitectónicos que guían cómo diseño y opero sistemas distribuidos a gran escala:*

<div class="grid cards" markdown>

-   :material-road-variant:{ .lg .middle } __Trazar Golden Paths, no colas de tickets__

    ---

    La complejidad de la infraestructura debe resolverse en el software, no en procesos burocráticos. Las APIs en autoservicio sobre AWS, OpenStack, OpenShift y bare-metal deben hacer que el camino seguro, auditable y conforme sea también el más rápido y sencillo para los equipos de ingeniería.

-   :material-file-code-outline:{ .lg .middle } __Filosofía propia de IaC y estado idempotente__

    ---

    Crear entornos desde cero es trivial; recuperarse de un fallo a mitad de un desmontaje de 30 pasos es donde se pone a prueba un sistema. Diseño motores declarativos en YAML con dependencias por olas (DAG) y desmontajes idempotentes que reconcilian contra el estado en vivo, eliminando el coste y el bloqueo de suites comerciales.

-   :material-shield-check-outline:{ .lg .middle } __Guardarraíles deterministas para la IA operativa__

    ---

    Los modelos de lenguaje y sistemas agénticos son componentes no confiables en operaciones críticas. En lugar de prompts libres, deben acotarse mediante máquinas de estado cíclicas (LangGraph), contratos de herramientas tipadas de solo lectura (MCP) y verificación estricta de esquemas antes de ejecutar diagnósticos o acciones.

</div>

## Ensayos de Arquitectura y Lecciones de Producción

*Reflexiones en profundidad tras una década construyendo plataformas cloud internas y operando infraestructura bancaria:*

<div class="grid cards" markdown>

-   :material-cached:{ .lg .middle } __[Cuando las Shared Libraries Tocan Techo: Por Qué Sustituimos Jenkins por un Dispatcher HA Propio](blog/posts/2026-02-15-leaving-jenkins-at-scale-custom-dispatcher.md)__

    ---

    Por qué estandarizar el CI/CD con Jenkins Shared Libraries fue el primer paso indispensable — y cómo dejó al descubierto los cuellos de botella de estado y disponibilidad que motivaron diseñar nuestro propio dispatcher en Django/Celery y Kubernetes Jobs efímeros.

    [:octicons-arrow-right-24: Leer ensayo de arquitectura](blog/posts/2026-02-15-leaving-jenkins-at-scale-custom-dispatcher.md)

-   :material-file-tree-outline:{ .lg .middle } __[Nueve Años de Plataformas Cloud Internas: Por Qué el YAML Declarativo Sustituyó a Nuestro Orquestador Comercial](blog/posts/2026-03-01-declarative-infrastructure-python.md)__

    ---

    Cómo ser propietarios del plano de control central cambia la decisión *build-vs-buy*, por qué evitamos archivos locales de estado y por qué el desmontaje idempotente es la verdadera prueba de fuego de cualquier motor de aprovisionamiento.

    [:octicons-arrow-right-24: Leer ensayo de arquitectura](blog/posts/2026-03-01-declarative-infrastructure-python.md)

-   :material-radar:{ .lg .middle } __[La PoC Fue la Parte Fácil: Lecciones al Construir un Motor Agéntico de Diagnóstico CI/CD en Banca](blog/posts/2026-03-10-agentic-cicd-diagnostics-langgraph.md)__

    ---

    Por qué los grafos cíclicos con estado en LangGraph superan a las cadenas lineales en el triaje de incidentes, y qué bloquea realmente el paso de prototipos validados de IA a producción masiva en un gran banco regulado.

    [:octicons-arrow-right-24: Leer ensayo de arquitectura](blog/posts/2026-03-10-agentic-cicd-diagnostics-langgraph.md)

</div>

<div style="text-align: right; margin-top: -0.5rem; margin-bottom: 2.5rem;" markdown>

[Explorar todos los ensayos del blog :octicons-arrow-right-24:](blog/index.md){ .md-button .md-button--primary }

</div>

## Sistemas de Plataforma e Infraestructura Corporativa

*Topología de sistemas, trade-offs de arquitectura y modos de fallo en entornos de producción multi-cloud:*

<div class="grid cards two-col" markdown>

-   :material-cloud-cog-outline:{ .lg .middle } __[Orion — Plataforma IaaS Central y Pipeline por Drivers](projects/orion-iaas.md)__

    ---

    Arquitecto y responsable del plano de control IaaS y despliegue para BBVA: una sola interfaz OpenAPI que gobierna 30.000+ máquinas sobre AWS, OpenStack, OpenShift y bare-metal (40.000+ operaciones diarias), respaldada por PostgreSQL, MongoDB, Redis y auditorías automáticas.

    <span class="tech-tag">Python</span><span class="tech-tag">Django REST</span><span class="tech-tag">Celery</span><span class="tech-tag">PostgreSQL</span><span class="tech-tag">MongoDB</span><span class="tech-tag">Redis</span>

    [:octicons-arrow-right-24: Leer caso de estudio](projects/orion-iaas.md)

-   :material-file-tree-outline:{ .lg .middle } __[Blueprint — Motor Declarativo de Ciclo de Vida](projects/blueprint.md)__

    ---

    Motor asíncrono en Python estilo Terraform guiado por planos YAML versionados. Orquesta olas DAG en paralelo contra Orion, emite trazas completas de auditoría y soporta desmontajes idempotentes — eliminando licencias comerciales.

    <span class="tech-tag">Python</span><span class="tech-tag">AsyncIO</span><span class="tech-tag">Planificación DAG</span><span class="tech-tag">YAML Declarativo</span><span class="tech-tag">GitOps</span>

    [:octicons-arrow-right-24: Leer caso de estudio](projects/blueprint.md)

-   :material-cached:{ .lg .middle } __[Dejar Jenkins Atrás — Dispatcher HA y Ejecución K8s](projects/dispatcher-migration.md)__

    ---

    Cómo evolucionamos desde Jenkins hacia un Dispatcher de Operaciones en Alta Disponibilidad (Django + Celery), inyección dinámica de configuración en runtime y ejecución efímera en Kubernetes Jobs.

    <span class="tech-tag">Django</span><span class="tech-tag">Celery</span><span class="tech-tag">Kubernetes Jobs</span><span class="tech-tag">Ansible</span><span class="tech-tag">OpenAPI</span>

    [:octicons-arrow-right-24: Leer caso de estudio](projects/dispatcher-migration.md)

-   :material-radar:{ .lg .middle } __[Orion AI — Auto-Diagnóstico CI/CD (PoC Validada)](projects/orion-ai.md)__

    ---

    Prototipo multi-agente validado con LangGraph y bucles ReAct que correlaciona logs de ejecución, runbooks indexados en Redis y diffs de GitLab bajo guardarraíles deterministas — junto con un análisis honesto de las restricciones de despliegue bancario.

    <span class="tech-tag">LangGraph</span><span class="tech-tag">ReAct</span><span class="tech-tag">MCP</span><span class="tech-tag">Qwen 131k</span><span class="tech-tag">Guardarraíles Deterministas</span>

    [:octicons-arrow-right-24: Leer caso de estudio](projects/orion-ai.md)

</div>

<div style="text-align: right; margin-top: -0.5rem; margin-bottom: 2.5rem;" markdown>

[Ver la evolución completa de arquitectura y subsistemas :octicons-arrow-right-24:](projects/index.md){ .md-button }

</div>

## Sistemas Open-Source en GitHub

<div class="grid cards two-col" markdown>

-   :material-waveform:{ .lg .middle } __[OmniLecture Studio — Suite IA Multimodal para Linux](projects/omni-lecture.md)__

    ---

    Suite nativa para Linux (Wayland/GNOME, GTK 3) con pipeline multimedia en FFmpeg (compresión H.264 a 10 FPS con `-tune stillimage` que ahorra hasta un 70% de espacio, sincronización PTS y filtros de audio `afftdn`), combinada con transcripción dual Whisper, OCR CLAHE en OpenCV y grafos en LangGraph.

    <span class="tech-tag">Python</span><span class="tech-tag">FFmpeg</span><span class="tech-tag">GTK 3 / Wayland</span><span class="tech-tag">LangGraph</span><span class="tech-tag">Whisper int8</span><span class="tech-tag">OpenCV / OCR</span>

    [:octicons-arrow-right-24: Caso de estudio](projects/omni-lecture.md) · [:fontawesome-brands-github: Código en GitHub](https://github.com/oredondo/omnilecture-studio)

-   :material-wrench-outline:{ .lg .middle } __[WrenchBuddy — Plataforma IA de Vehículos y RAG con pgvector](projects/wrenchbuddy.md)__

    ---

    Plataforma full-stack construida con Django 6, DRF, PostgreSQL (`pgvector` RAG de 768 dim), Celery, Redis, S3/MinIO, OCR de facturas con LangChain Vision, informes PDF en ReportLab y frontend en TypeScript.

    <span class="tech-tag">Django 6 / DRF</span><span class="tech-tag">PostgreSQL pgvector</span><span class="tech-tag">Celery &amp; Redis</span><span class="tech-tag">LangChain RAG</span><span class="tech-tag">TypeScript</span>

    [:octicons-arrow-right-24: Caso de estudio](projects/wrenchbuddy.md) · [:fontawesome-brands-github: Backend](https://github.com/oredondo/WrenchBuddy) · [:fontawesome-brands-github: Frontend](https://github.com/oredondo/WrenchBuddy-frontend)

</div>

<div class="cta-banner" markdown>

### Colaboración y Debate Técnico

Abierto a debatir sobre arquitectura de plataformas de despliegue, diseño de motores declarativos de IaC, sistemas distribuidos en Python y adopción de agentes de IA en producción.

[:material-linkedin: Conectar en LinkedIn](https://linkedin.com/in/oscarredondodjangopython){ .md-button .md-button--primary }
[:fontawesome-brands-github: GitHub (@oredondo)](https://github.com/oredondo){ .md-button }
[:material-email-outline: o.redondo91@gmail.com](mailto:o.redondo91@gmail.com){ .md-button }

</div>
