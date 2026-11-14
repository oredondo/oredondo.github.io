---
title: Senior Platform Engineer · Python
description: >-
  Oscar Redondo — Senior Platform Engineer · Python con más de 10 años construyendo
  plataformas internas de desarrollo, motores de automatización distribuida e IA
  operativa. Arquitecto único de la plataforma IaaS central de BBVA.
hide:
  - navigation
  - toc
  - feedback
---

<div class="hero" markdown>

<p class="hero__eyebrow">Senior Platform Engineer · Python · Madrid, España</p>

# Oscar Redondo { .hero__title }

<p class="hero__lead">
Diseño y construyo <strong>plataformas internas de desarrollo que hacen invisible la complejidad de la infraestructura distribuida</strong> — transformando operaciones de nube híbrida en AWS, OpenStack, OpenShift y bare-metal en APIs limpias en autoservicio, motores declarativos de ciclo de vida y automatización determinista.
</p>

[:material-sitemap-outline: Explorar el ecosistema de plataforma](projects/index.md){ .md-button .md-button--primary }
[:material-file-account-outline: Ver mi CV](cv/index.md){ .md-button }
[:fontawesome-brands-github: GitHub (@oredondo)](https://github.com/oredondo){ .md-button }

</div>

<div class="kpi-grid">
  <div class="kpi-card">
    <span class="kpi-value">10.000s</span>
    <span class="kpi-label">Nodos gobernados</span>
  </div>
  <div class="kpi-card">
    <span class="kpi-value">Alto Volumen</span>
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

## Cómo se conecta todo: una plataforma construida capa por capa

Durante los últimos nueve años en **BBVA Technology**, mi trabajo no ha consistido en herramientas aisladas, sino en una única **Plataforma Interna de Desarrollo** que ha evolucionado capa por capa a medida que resolvíamos cada cuello de botella de escala:

```mermaid
flowchart LR
    JSL["Jenkins Shared Libraries<br/>(CI/CD estandarizado)"] -->|"Superó límite de controlador único"| DISP["Dispatcher HA de Operaciones<br/>(API en Django + Celery)"]
    CFG["Gestión Central de Config<br/>(Inyección de variables en runtime)"] --> DISP & PIPE
    DISP --> K8S["Motor de Kubernetes Jobs<br/>(Pods efímeros)"]
    DISP --> PIPE["Pipeline Universal por Drivers<br/>(AWS · OpenStack · OpenShift · Bare-metal)"]
    PIPE --> ORION["Plano de Control IaaS Orion<br/>(RBAC, BD híbrida y auditoría)"]
    ORION --> BP["Motor Blueprint<br/>(YAML declarativo y teardown idempotente)"]
    ORION --> AI["Orion AI (PoC Validada)<br/>(Diagnóstico CI/CD con LangGraph + ReAct)"]
```

## Casos de Estudio de Arquitectura Corporativa

*Topología abstracta, trade-offs y modos de fallo — respetando la confidencialidad bancaria sin código propietario ni inventado:*

<div class="grid cards two-col" markdown>

-   :material-cloud-cog-outline:{ .lg .middle } __[Orion — Plataforma IaaS Central y Pipeline por Drivers](projects/orion-iaas.md)__

    ---

    Arquitecto único de la plataforma IaaS central para la Infraestructura Core Banking de BBVA: una sola interfaz OpenAPI sobre AWS, OpenStack, OpenShift y bare-metal, respaldada por PostgreSQL, MongoDB, Redis, auditorías automáticas y un puente API sin downtime entre F5 y OpenStack.

    <span class="tech-tag">Python</span><span class="tech-tag">Django REST</span><span class="tech-tag">Celery</span><span class="tech-tag">PostgreSQL</span><span class="tech-tag">MongoDB</span><span class="tech-tag">Redis</span>

    [:octicons-arrow-right-24: Leer caso de estudio](projects/orion-iaas.md)

-   :material-file-tree-outline:{ .lg .middle } __[Blueprint — Motor Declarativo de Ciclo de Vida](projects/blueprint.md)__

    ---

    Motor asíncrono en Python estilo Terraform guiado por planos YAML versionados. Orquesta olas DAG en paralelo contra Orion, emite trazas completas de auditoría y soporta desmontajes idempotentes — eliminando licencias comerciales.

    <span class="tech-tag">Python</span><span class="tech-tag">AsyncIO</span><span class="tech-tag">Planificación DAG</span><span class="tech-tag">YAML Declarativo</span><span class="tech-tag">GitOps</span>

    [:octicons-arrow-right-24: Leer caso de estudio](projects/blueprint.md)

-   :material-cached:{ .lg .middle } __[Dejar Jenkins Atrás — Dispatcher HA y Ejecución K8s](projects/dispatcher-migration.md)__

    ---

    Cómo evolucionamos desde Jenkins Shared Libraries en Groovy hacia un Dispatcher de Operaciones en Alta Disponibilidad (Django + Celery), inyección dinámica de configuración en runtime y ejecución efímera en Kubernetes Jobs.

    <span class="tech-tag">Django</span><span class="tech-tag">Celery</span><span class="tech-tag">Kubernetes Jobs</span><span class="tech-tag">Ansible</span><span class="tech-tag">OpenAPI</span>

    [:octicons-arrow-right-24: Leer caso de estudio](projects/dispatcher-migration.md)

-   :material-stethoscope:{ .lg .middle } __[Orion AI — Auto-Diagnóstico CI/CD (PoC Validada)](projects/orion-ai.md)__

    ---

    Prototipo multi-agente validado con LangGraph y bucles ReAct que correlaciona logs de ejecución, documentación en Redis y diffs de GitLab bajo guardarraíles deterministas — junto con un análisis honesto de las restricciones de despliegue bancario.

    <span class="tech-tag">LangGraph</span><span class="tech-tag">ReAct</span><span class="tech-tag">MCP</span><span class="tech-tag">Qwen 131k</span><span class="tech-tag">Guardarraíles Deterministas</span>

    [:octicons-arrow-right-24: Leer caso de estudio](projects/orion-ai.md)

</div>

## Sistemas Open-Source Públicos en GitHub

*Bases de código completas y ejecutables desarrolladas fuera del ámbito bancario:*

<div class="grid cards two-col" markdown>

-   :material-school-outline:{ .lg .middle } __[OmniLecture Studio — Suite IA Multimodal para Linux](projects/omni-lecture.md)__

    ---

    Suite nativa para Linux (Wayland/GNOME, GTK 3) de captura de pantalla/audio y pipeline en LangGraph que combina doble motor Whisper (`faster-whisper` CPU `int8` + API cloud), detección 16×16 de cambio de diapositiva y OCR con OpenCV CLAHE + Tesseract.

    <span class="tech-tag">Python</span><span class="tech-tag">GTK 3 / Wayland</span><span class="tech-tag">LangGraph</span><span class="tech-tag">Whisper int8</span><span class="tech-tag">OpenCV / OCR</span>

    [:octicons-arrow-right-24: Caso de estudio](projects/omni-lecture.md) · [:fontawesome-brands-github: Código en GitHub](https://github.com/oredondo/omnilecture-studio)

-   :material-wrench-outline:{ .lg .middle } __[WrenchBuddy — Plataforma IA de Vehículos y RAG con pgvector](projects/wrenchbuddy.md)__

    ---

    Plataforma full-stack construida con Django 6, DRF, PostgreSQL (`pgvector` RAG de 768 dim), Celery, Redis, S3/MinIO, OCR de facturas con LangChain Vision, informes PDF en ReportLab y frontend en TypeScript.

    <span class="tech-tag">Django 6 / DRF</span><span class="tech-tag">PostgreSQL pgvector</span><span class="tech-tag">Celery &amp; Redis</span><span class="tech-tag">LangChain RAG</span><span class="tech-tag">TypeScript</span>

    [:octicons-arrow-right-24: Caso de estudio](projects/wrenchbuddy.md) · [:fontawesome-brands-github: Backend](https://github.com/oredondo/WrenchBuddy) · [:fontawesome-brands-github: Frontend](https://github.com/oredondo/WrenchBuddy-frontend)

</div>

## Notas de Ingeniería y Ensayos de Arquitectura

<div class="grid cards" markdown>

-   __[Cuando las Shared Libraries Tocan Techo: Por Qué Sustituimos Jenkins por un Dispatcher HA Propio](blog/posts/2026-02-15-leaving-jenkins-at-scale-custom-dispatcher.md)__

    ---

    Por qué estandarizar el CI/CD con Jenkins Shared Libraries fue el primer paso indispensable — y cómo dejó al descubierto los límites que motivaron nuestro dispatcher HA en Django/Celery y Kubernetes Jobs efímeros.

-   __[Nueve Años de Plataformas Cloud Internas: Por Qué el YAML Declarativo Sustituyó a Nuestro Orquestador Comercial](blog/posts/2026-03-01-declarative-infrastructure-python.md)__

    ---

    Cómo ser propietarios del plano de control central cambia la decisión build-vs-buy, por qué evitamos archivos locales de estado y por qué el desmontaje idempotente es la prueba real de cualquier motor.

-   __[La PoC Fue la Parte Fácil: Lecciones al Construir un Motor Agéntico de Diagnóstico CI/CD en Banca](blog/posts/2026-03-10-agentic-cicd-diagnostics-langgraph.md)__

    ---

    Por qué los grafos cíclicos en LangGraph superan a las cadenas lineales en el triaje de logs, y qué bloquea realmente el paso de prototipos validados de IA a producción masiva en entornos regulados.

</div>

<div class="cta-banner" markdown>

### Hablemos de arquitectura de plataformas

Me encanta conversar sobre plataformas internas de desarrollo, sistemas distribuidos en Python, abstracciones multi-cloud e integración segura de agentes de IA en operaciones reales.

[:material-linkedin: Conectar en LinkedIn](https://linkedin.com/in/oscarredondodjangopython){ .md-button .md-button--primary }
[:fontawesome-brands-github: GitHub (@oredondo)](https://github.com/oredondo){ .md-button }
[:material-email-outline: o.redondo91@gmail.com](mailto:o.redondo91@gmail.com){ .md-button }

</div>
