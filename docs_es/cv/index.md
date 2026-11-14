---
title: Curriculum Vitae
description: >-
  CV de Oscar Redondo — Senior Platform Engineer · Python con más de 10 años diseñando plataformas de despliegue de infraestructura, motores propios de IaC e IA operativa a gran escala.
hide:
  - navigation
  - feedback
---

<div class="cv-actions no-print">
  <button class="md-button md-button--primary" onclick="window.print()">Imprimir / Guardar en PDF</button>
</div>

# Oscar Redondo

<p class="cv-headline">Senior Platform Engineer · Python — Plataformas de Despliegue de Infraestructura, IaC Declarativo e IA Aplicada</p>

<p class="cv-contact">
Madrid, España ·
<a href="mailto:o.redondo91@gmail.com">o.redondo91@gmail.com</a> ·
<a href="https://linkedin.com/in/oscarredondodjangopython">linkedin.com/in/oscarredondodjangopython</a> ·
<a href="https://github.com/oredondo">github.com/oredondo</a>
</p>

## Perfil Profesional

**Senior Platform Engineer · Python** con **más de 10 años de experiencia** diseñando plataformas de despliegue, aprovisionamiento y gobierno de infraestructura a gran escala, motores declarativos de Infrastructure as Code (IaC) y flujos de trabajo de IA operativa. Mi filosofía de ingeniería se fundamenta en hacer invisible la complejidad de la infraestructura distribuida — construyendo pasarelas en autoservicio, motores asíncronos en YAML guiados por grafos de dependencias (DAG), capas universales por drivers y sistemas deterministas que eliminan cuellos de botella operativos y garantizan conformidad y auditoría por diseño.

Como **arquitecto único y responsable técnico de la suite central de plataforma IaaS (Orion y Blueprint)** para la Infraestructura Core Banking de BBVA, concebí y desarrollé los sistemas que gobiernan **más de 30.000 máquinas** en AWS, OpenStack, OpenShift y bare-metal, procesando **más de 40.000 operaciones diarias para más de 500 ingenieros**. Diseñé la arquitectura híbrida de persistencia y consulta masiva (PostgreSQL, MongoDB, Redis) para soportar operaciones de gran volumen y canalizaciones automáticas de auditoría y cumplimiento normativo. Definí una filosofía propia de IaC mediante motores asíncronos en YAML (`Blueprint`), un pipeline universal de despliegue por drivers, inyección dinámica de configuración en runtime y dispatchers de operaciones en Alta Disponibilidad sobre Kubernetes Jobs, eliminando el bloqueo de proveedores comerciales.

En la intersección entre ingeniería de infraestructura e IA aplicada, concebí y validé **Orion AI** (LangGraph, ReAct, Qwen 131k de contexto) para automatizar el análisis de causa raíz en CI/CD bajo guardarraíles deterministas, y desarrollo sistemas open-source multimodales y con RAG en Python ([OmniLecture Studio](https://github.com/oredondo/omnilecture-studio), [WrenchBuddy](https://github.com/oredondo/WrenchBuddy)). Con sólida trayectoria impulsando arquitectura técnica e integración entre centros de ingeniería en **España, México y Turquía**, definiendo estándares corporativos de despliegue y formando ingenieros.

## Experiencia Profesional

### Senior Python Developer, DevOps — Responsable de Plataforma IaaS y Despliegue
<p class="cv-meta"><strong>BBVA Technology</strong> (Infraestructura Core Banking) · Madrid · 2017 – Presente</p>

- **Arquitectura de la Plataforma Central IaaS y Despliegue (Orion):** Propietario único y arquitecto principal del plano de control central de gobierno, inventario y despliegue IaaS de BBVA — gobernando **más de 30.000 máquinas** en AWS, OpenStack, OpenShift y bare-metal y procesando **más de 40.000 operaciones diarias para más de 500 ingenieros**. Lideré todas las decisiones técnicas de extremo a extremo: API REST documentada en OpenAPI/Swagger, modelo de autoservicio, permisos RBAC granulares y procesamiento asíncrono distribuido, haciendo invisible la complejidad física y multi-cloud a los equipos de desarrollo.
- **Filosofía Propia de IaC y Orquestación Declarativa (Blueprint):** Concebí y desarrollé **Blueprint**, un motor asíncrono de orquestación en Python guiado por planos YAML versionados (conceptualmente análogo a Terraform). Construido para ejecutar aprovisionamiento en paralelo mediante análisis de dependencias por olas (DAG), reconciliación contra el estado en vivo de Orion y **operaciones de desmontaje idempotentes** que reanudan destrucciones interrumpidas en cientos de entornos sin reprocesar pasos — eliminando el 100% de los costes de licencias comerciales (como Red Hat Automation Platform / Ansible Tower).
- **Pipeline Universal por Drivers y Gestión Centralizada de Configuración:** Diseñé un pipeline universal de despliegue en Django basado en un **patrón modular de drivers** que unifica 4 sustratos tecnológicos (AWS, OpenStack, OpenShift y bare-metal) bajo una misma base de código. Desarrollé un **Sistema Centralizado de Gestión de Configuración** que desacopla las variables de la lógica de automatización, inyectándolas dinámicamente en tiempo de ejecución para garantizar **cero deriva de configuración (*zero drift*)** entre desarrollo, preproducción y producción.
- **Migración de Jenkins a Dispatcher HA y Motor de Ejecución en K8s Jobs:** Lideré la sustitución estratégica de Jenkins como punto único de fallo (tras haber estandarizado inicialmente el CI/CD mediante **Jenkins Shared Libraries** modulares en Groovy) diseñando un **Dispatcher de Operaciones en Alta Disponibilidad** en Django y Celery con API REST OpenAPI, políticas de reintentos a medida y un **Motor de Ejecución sobre Kubernetes Jobs** que ejecuta cada automatización como un contenedor efímero, aislado y observable.
- **Ingeniería de Datos Híbrida y Pipelines Automáticos de Auditoría:** Diseñé y administré la arquitectura de datos híbrida (**PostgreSQL, MongoDB, Redis**) para gobernar más de 30.000 activos en tiempo real, optimizando consultas concurrentes de alto volumen y construyendo canalizaciones automatizadas de extracción de datos (informes CSV de auditoría) consumidas directamente por los equipos de cumplimiento normativo y auditores bancarios.
- **Interoperabilidad de Red sin Downtime y Servicios Compartidos:** Desarrollé un **Puente API RESTful a medida entre F5 y OpenStack** desplegado con **cero tiempo de inactividad** tras la deprecación oficial de la integración del fabricante, y mantuve la **base de código Ansible** agnóstica de entorno que gobierna los clusters internos de infraestructura compartida (**GitLab, Artifactory y Jenkins**).
- **IA Operativa (Orion AI — PoC Validada):** Concebí, diseñé y desarrollé una PoC multi-agente validada (**LangGraph, ReAct, Qwen 131k LLM**) que analiza concurrentemente logs de ejecución, runbooks operativos (indexados en Redis para RAG) y diffs de commits en GitLab bajo guardarraíles deterministas para reducir el triaje de CI/CD de horas a segundos; prototipo validado y preparado a la espera de directrices de integración con la infraestructura central de IA.
- **Integración Internacional, Operaciones en Producción y Mentoría:** Lideré la integración técnica y el onboarding de la plataforma con equipos de ingeniería en **México y Turquía** (escalando la adopción a más de 100 ingenieros internacionales), asumí guardias e incidentes de producción a escala bancaria manteniendo una disponibilidad superior al 99,9% y formé a ingenieros en buenas prácticas de automatización y plataforma.

<p class="cv-tech"><strong>Tecnologías:</strong> Python, Django, DRF, Celery, AsyncIO, PostgreSQL, MongoDB, Redis, LangChain, LangGraph, ReAct, Model Context Protocol (MCP), Ansible, Kubernetes, OpenShift, AWS, OpenStack, Docker, Podman, Jenkins, GitLab CI, Groovy, F5, Infoblox.</p>

### Administrador y Desarrollador OpenStack
<p class="cv-meta"><strong>Oesia</strong> · Madrid · 2015 – 2017</p>

- **Operación de Nube Privada (OpenStack y Ceph):** Administré y mantuve una infraestructura de nube privada en producción basada en **OpenStack y almacenamiento distribuido Ceph**, garantizando una disponibilidad del 99,9%, alto rendimiento y fiabilidad para los equipos internos.
- **Plataforma de Almacenamiento Privado (OpenStack Swift):** Diseñé y desarrollé una aplicación corporativa de almacenamiento en nube privada auto-alojada (equivalente conceptual a Dropbox) en Python sobre el almacenamiento de objetos **OpenStack Swift**, proporcionando compartición segura y escalable de archivos para más de 200 usuarios sobre clusters de 50+ TB sin depender de nubes públicas.

<p class="cv-tech"><strong>Tecnologías:</strong> OpenStack, Ceph, Swift, Python, Linux.</p>

## Sistemas Destacados y Proyectos Open-Source

| Sistema | Alcance y Arquitectura |
| :--- | :--- |
| **[Orion — Plataforma IaaS](../projects/orion-iaas.md)** *(BBVA)* | Plano de control central en autoservicio con OpenAPI, capa híbrida PostgreSQL/MongoDB/Redis y pipelines automáticos de auditoría sobre 30.000+ máquinas en AWS, OpenStack, OpenShift y bare-metal (40.000+ ops diarias). |
| **[Blueprint — Motor Declarativo](../projects/blueprint.md)** *(BBVA)* | Orquestador asíncrono en Python guiado por YAML con concurrencia por olas DAG, trazabilidad de trabajos en Orion y desmontajes idempotentes reanudables (filosofía propia de IaC sin Red Hat Automation Platform). |
| **[Dispatcher HA, Gestión de Config y K8s Jobs](../projects/dispatcher-migration.md)** *(BBVA)* | Migración desde Jenkins Shared Libraries hacia un dispatcher de operaciones en Alta Disponibilidad con Django/Celery, inyección de variables en runtime y ejecución efímera en Kubernetes Jobs. |
| **Puente API F5 / OpenStack y Ansible Core** *(BBVA)* | Puente REST sin downtime que restauró la interoperabilidad de balanceadores F5 con OpenStack; automatización Ansible agnóstica de entorno para GitLab, Artifactory y Jenkins. |
| **[Orion AI — Auto-Diagnóstico CI/CD](../projects/orion-ai.md)** *(PoC BBVA)* | Prototipo multi-agente validado en LangGraph + ReAct que correlaciona logs de pipelines, runbooks indexados en Redis y diffs de GitLab bajo guardarraíles deterministas. |
| **[OmniLecture Studio](../projects/omni-lecture.md)** *([GitHub](https://github.com/oredondo/omnilecture-studio))* | Suite nativa para Linux (Wayland, GTK 3) con pipeline multimedia FFmpeg (H.264 stillimage, filtrado afftdn y sync PTS), grafos en LangGraph, doble motor Whisper (int8 + API) y OCR con OpenCV CLAHE + Tesseract. |
| **[WrenchBuddy](../projects/wrenchbuddy.md)** *([GitHub](https://github.com/oredondo/WrenchBuddy))* | Plataforma full-stack de ciclo de vida de vehículos en Django 6, DRF, PostgreSQL (`pgvector` RAG de 768 dim), Celery, Redis, S3/MinIO, OCR de facturas con LangChain Vision y TypeScript. |

## Habilidades Técnicas

| Categoría | Tecnologías |
| :--- | :--- |
| **Lenguajes Core y Backend** | Python, AsyncIO, Django, Django REST Framework, FastAPI, Celery, Pydantic, SQL, Groovy, Bash, Go |
| **Infraestructura Cloud y Plataformas** | AWS, OpenStack, OpenShift, Kubernetes, Docker, Podman, Ceph, Swift, Balanceadores F5, Infoblox, Linux |
| **IaC y Motores de Ejecución** | Blueprint (DSL asíncrono propio en YAML), Ansible, Terraform, Pulumi, Helm, ArgoCD, GitOps, Kubernetes Jobs |
| **Datos y Mensajería** | PostgreSQL (`pgvector`), MongoDB, Redis, RabbitMQ, AWS S3 / MinIO, Optimización de Consultas Masivas y Auditoría |
| **CI/CD y Observabilidad** | GitLab CI, GitHub Actions, Jenkins (Shared Libraries), Prometheus, Grafana, ELK / Splunk, HashiCorp Vault |
| **IA Aplicada y Sistemas Agénticos** | LangGraph, LangChain, Agentes ReAct, Model Context Protocol (MCP), RAG, Bases Vectoriales, Whisper, Ollama, vLLM |

## Formación Académica

**Grado en Ingeniería Electrónica de Comunicaciones**
<p class="cv-meta"><strong>Universidad Politécnica de Madrid</strong> · 2009 – 2016</p>

Ingeniería de telecomunicación y sistemas electrónicos con fundamentos sólidos en software, integración hardware, diseño de sistemas digitales y arquitectura de redes.

## Certificaciones y Formación Continua

| Año | Curso | Proveedor |
| :--- | :--- | :--- |
| 2026 | Complete MCP Developer Guide: Agents, Servers & Tools | Udemy |
| 2026 | Curso Completo: LangChain, LangGraph y Agentes de IA con Python | Udemy |
| 2026 | Curso Completo de Spec-Driven Development (SDD) y Agentes IA | Udemy |
| 2026 | Curso Completo: Bases de Datos Vectoriales para IA Generativa | Udemy |
| 2025 | Developing Secure Software (LFD121) | Linux Foundation |

## Idiomas

- **Español:** Nativo
- **Inglés:** Competencia profesional
