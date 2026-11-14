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

**Senior Platform Engineer · Python** con **más de 10 años de experiencia** diseñando plataformas de despliegue y gobierno de infraestructura a gran escala, motores propios de Infrastructure as Code (IaC) e IA operativa determinista. Como **arquitecto y responsable de plataforma de Orion (y su capa declarativa Blueprint)** en **BBVA Technology** —incorporado en 2017 en plena transición estratégica a **NextGen** para liberar cargas críticas del *mainframe*, desde *on-premises* hasta nube híbrida—, diseñé el plano de control para **BBVA** que gobierna **más de 30.000 máquinas** (AWS, OpenStack, OpenShift y bare-metal) y **más de 40.000 operaciones diarias para más de 500 ingenieros**, eliminando el *vendor lock-in* y el punto único de fallo.

Asimismo, impulso la integración de **IA operativa con guardarraíles deterministas** (**LangGraph, ReAct, RAG**), desarrollo proyectos personales open-source en Python y lidero la adopción de estándares corporativos de despliegue entre centros de ingeniería en **España, México y Turquía**.

## Experiencia Profesional

### Senior Python Developer, DevOps — Arquitecto y Responsable de Plataforma
<p class="cv-meta"><strong>BBVA Technology</strong> (Infraestructura Core Banking de BBVA) · Madrid · 2017 – Presente</p>

- **Plataforma Central IaaS y Despliegue (Orion / NextGen):** Arquitecté el plano de control central IaaS de **BBVA** dentro de la iniciativa **NextGen** (evolucionado de *on-premises* a nube híbrida para descargar cargas del *mainframe*), gobernando **30.000+ máquinas** en AWS, OpenStack, OpenShift y bare-metal con **40.000+ operaciones diarias para 500+ ingenieros** mediante API REST OpenAPI, autoservicio web y RBAC granular.
- **Filosofía Propia de IaC y Planos YAML (Blueprint sobre Orion):** Concebí la capa declarativa de **Orion** mediante planos YAML versionados (**Blueprint**, análogo a Terraform) con ejecución concurrente por olas (DAG), reconciliación en vivo y **desmontajes idempotentes reanudables** — sustituyendo suites comerciales por nodo (Red Hat Automation Platform / Ansible Tower) con un **ahorro acumulado superior a 6 millones de euros**.
- **Pipeline Universal por Drivers y Gestión de Configuración:** Estandaricé el despliegue sobre 4 sustratos (AWS, OpenStack, OpenShift y bare-metal) bajo un único pipeline modular en Django, acoplado a un **Sistema Centralizado de Gestión de Configuración** que inyecta variables en runtime para garantizar **cero deriva (*zero drift*)** entre entornos.
- **Migración de Jenkins a Dispatcher HA y K8s Jobs:** Eliminé Jenkins como punto único de fallo (tras haber estandarizado el CI/CD con **Jenkins Shared Libraries** en Groovy) diseñando un **Dispatcher HA** en Django y Celery con API OpenAPI, reintentos a medida y ejecución aislada en **Kubernetes Jobs efímeros**, asegurando continuidad operativa bajo directrices **DORA**.
- **Ingeniería de Datos Híbrida y Auditoría DORA:** Diseñé la persistencia híbrida (**PostgreSQL, MongoDB, Redis**) para consultar más de 30.000 activos en tiempo real y automatizar canalizaciones de inventario y cumplimiento consumidas por auditoría bancaria (**DORA**).
- **Interoperabilidad de Red sin Downtime y Servicios Compartidos:** Construí un **Puente API RESTful entre F5 y OpenStack** desplegado con **cero tiempo de inactividad** tras la deprecación del fabricante, y mantuve el código **Ansible** agnóstico de entorno que gobierna **GitLab, Artifactory y Jenkins**.
- **IA Operativa (Orion AI — PoC Validada):** Concebí y validé un prototipo multi-agente (**LangGraph, ReAct, Qwen 131k LLM**) que correlaciona trazas del Dispatcher, *runbooks* en Redis (RAG) y diffs de GitLab bajo guardarraíles deterministas, reduciendo el triaje de incidentes de horas a segundos (listo a la espera de directrices de integración con la infraestructura central de IA).
- **Despliegue Internacional, Guardias y Mentoría:** Lideré el onboarding de la plataforma en **México y Turquía** (100+ ingenieros internacionales), operé guardias críticas con **disponibilidad >99,9%** y formé a equipos en estándares de automatización.

<p class="cv-tech"><strong>Tecnologías:</strong> Python, Django, DRF, Celery, AsyncIO, PostgreSQL, MongoDB, Redis, LangChain, LangGraph, ReAct, Model Context Protocol (MCP), Ansible, Kubernetes, OpenShift, AWS, OpenStack, Docker, Podman, Jenkins, GitLab CI, Groovy, F5, Infoblox.</p>

### Administrador y Desarrollador OpenStack
<p class="cv-meta"><strong>Oesia</strong> · Madrid · 2015 – 2017</p>

- **Operación de Nube Privada (OpenStack y Ceph):** Administré y mantuve una infraestructura de nube privada en producción basada en **OpenStack y almacenamiento distribuido Ceph**, garantizando una disponibilidad del 99,9%, alto rendimiento y fiabilidad para los equipos internos.
- **Plataforma de Almacenamiento Privado (OpenStack Swift):** Diseñé y desarrollé una aplicación corporativa de almacenamiento en nube privada auto-alojada (equivalente conceptual a Dropbox) en Python sobre el almacenamiento de objetos **OpenStack Swift**, proporcionando compartición segura y escalable de archivos para más de 200 usuarios sobre clusters de 50+ TB sin depender de nubes públicas.

<p class="cv-tech"><strong>Tecnologías:</strong> OpenStack, Ceph, Swift, Python, Linux.</p>

## Sistemas Destacados y Proyectos Personales Open-Source

| Sistema | Alcance y Arquitectura |
| :--- | :--- |
| **[Orion — Plataforma IaaS](../projects/orion-iaas.md)** *(BBVA)* | Plano de control central en autoservicio con OpenAPI, capa híbrida PostgreSQL/MongoDB/Redis y pipelines automáticos de auditoría sobre 30.000+ máquinas en AWS, OpenStack, OpenShift y bare-metal (40.000+ ops diarias). |
| **[Blueprint — Capa Declarativa sobre Orion](../projects/blueprint.md)** *(BBVA)* | Capa de definición declarativa en YAML interpretada y ejecutada nativamente por Orion con concurrencia por olas DAG, trazabilidad por Job ID y desmontajes idempotentes reanudables (sin Red Hat Automation Platform). |
| **[Dispatcher HA, Gestión de Config y K8s Jobs](../projects/dispatcher-migration.md)** *(BBVA)* | Migración desde Jenkins Shared Libraries hacia un dispatcher de operaciones en Alta Disponibilidad con Django/Celery, inyección de variables en runtime y ejecución efímera en Kubernetes Jobs. |
| **Puente API F5 / OpenStack y Ansible Core** *(BBVA)* | Puente REST sin downtime que restauró la interoperabilidad de balanceadores F5 con OpenStack; automatización Ansible agnóstica de entorno para GitLab, Artifactory y Jenkins. |
| **[Orion AI — Auto-Diagnóstico CI/CD](../projects/orion-ai.md)** *(PoC BBVA)* | Prototipo multi-agente validado en LangGraph + ReAct que correlaciona logs de pipelines, runbooks indexados en Redis y diffs de GitLab bajo guardarraíles deterministas. |
| **[OmniLecture Studio](../projects/omni-lecture.md)** *([GitHub](https://github.com/oredondo/omnilecture-studio))* | Suite nativa para Linux (Wayland, GTK 3) con filtrado acústico FFmpeg (`afftdn`, `silenceremove`), transcripción anti-alucinación en Whisper y grafos de conocimiento en Markdown. |
| **[WrenchBuddy](../projects/wrenchbuddy.md)** *([GitHub](https://github.com/oredondo/WrenchBuddy))* | Idea en fase de construcción muy temprana para el ciclo de vida de vehículos en Django 6, DRF, PostgreSQL (`pgvector` RAG de 768 dim), Celery, Redis, S3/MinIO, OCR Vision y TypeScript. |

## Habilidades Técnicas

| Categoría | Tecnologías |
| :--- | :--- |
| **Lenguajes Core y Backend** | Python, AsyncIO, Django, Django REST Framework, FastAPI, OpenAPI / Swagger, Celery, Pydantic, SQL, Groovy, Bash, Go |
| **Infraestructura Cloud y Plataformas** | AWS, OpenStack, OpenShift, Kubernetes, Docker, Podman, Ceph, Swift, Balanceadores F5, Infoblox, Linux |
| **IaC y Motores de Ejecución** | Orion / Blueprint (capa declarativa propia en YAML), JSON Schema, Ansible, Terraform, Pulumi, Helm, ArgoCD, GitOps, Kubernetes Jobs |
| **Datos y Mensajería** | PostgreSQL (`pgvector`), MongoDB, Redis, RabbitMQ, AWS S3 / MinIO, Optimización de Consultas Masivas y Auditoría |
| **CI/CD y Observabilidad** | GitLab CI, GitHub Actions, Jenkins (Shared Libraries), Prometheus, Grafana, ELK / Splunk, HashiCorp Vault |
| **IA Aplicada y Sistemas Agénticos** | LangGraph, LangChain, Agentes ReAct, Model Context Protocol (MCP), RAG, Bases Vectoriales, Whisper, FFmpeg, Ollama, vLLM |

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
