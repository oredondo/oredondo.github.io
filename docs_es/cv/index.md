---
title: Curriculum Vitae
description: >-
  CV de Oscar Redondo — Senior Platform Engineer · Python con más de 10 años diseñando plataformas internas de desarrollo, motores de automatización distribuida e IA operativa.
hide:
  - navigation
  - feedback
---

<div class="cv-actions no-print">
  <button class="md-button md-button--primary" onclick="window.print()">Imprimir / Guardar en PDF</button>
</div>

# Oscar Redondo

<p class="cv-headline">Senior Platform Engineer · Python — Plataformas Internas de Desarrollo, Automatización Distribuida e IA Aplicada</p>

<p class="cv-contact">
Madrid, España ·
<a href="mailto:o.redondo91@gmail.com">o.redondo91@gmail.com</a> ·
<a href="https://linkedin.com/in/oscarredondodjangopython">linkedin.com/in/oscarredondodjangopython</a> ·
<a href="https://github.com/oredondo">github.com/oredondo</a>
</p>

## Perfil Profesional

**Senior Platform Engineer · Python** con **más de 10 años de experiencia** diseñando plataformas internas de desarrollo a gran escala, motores de automatización distribuida y flujos de trabajo de IA operativa. Mi filosofía de ingeniería se centra en transformar infraestructura distribuida compleja en abstracciones limpias y en autoservicio — construyendo motores declarativos de ciclo de vida, capas universales de drivers y sistemas deterministas que eliminan cuellos de botella operativos.

Como **arquitecto único y responsable técnico de la suite central de plataforma IaaS (Orion y Blueprint)** para la Infraestructura Core Banking de BBVA, concebí y desarrollé los sistemas que gobiernan **decenas de miles de máquinas** en AWS, OpenStack, OpenShift y entornos locales, procesando **operaciones diarias de alto rendimiento para más de 500 ingenieros**. Diseñé la arquitectura híbrida de persistencia y consulta (PostgreSQL, MongoDB, Redis) para soportar operaciones de gran volumen, canalizaciones automáticas de exportación para auditoría y estricto cumplimiento normativo, desarrollando motores asíncronos propios de orquestación en YAML (`Blueprint`) y dispatchers de operaciones en Alta Disponibilidad que eliminaron el bloqueo de proveedores comerciales.

En la intersección entre ingeniería de plataformas e IA aplicada, diseñé la PoC validada **Orion AI** (LangGraph, ReAct, Qwen 131k de contexto) para automatizar el diagnóstico de fallos en CI/CD bajo guardarraíles deterministas, y desarrollo sistemas open-source multimodales y con RAG en Python ([OmniLecture Studio](https://github.com/oredondo/omnilecture-studio), [WrenchBuddy](https://github.com/oredondo/WrenchBuddy)). Con experiencia impulsando arquitectura técnica con equipos internacionales en **España, México y Turquía**, definiendo estándares corporativos de despliegue y formando ingenieros.

## Experiencia Profesional

### Senior Python Developer, DevOps — Responsable de Plataforma IaaS
<p class="cv-meta"><strong>BBVA Technology</strong> (Infraestructura Core Banking) · Madrid · 2017 – Presente</p>

- **Arquitectura de la Plataforma Central IaaS (Orion):** Concebí, diseñé y construí desde cero como propietario único la plataforma central de gobierno, inventario y despliegue IaaS de BBVA — gestionando **decenas de miles de máquinas** en AWS, OpenStack, OpenShift y bare-metal para **más de 500 ingenieros**. Lideré todas las decisiones técnicas de extremo a extremo: diseño REST con OpenAPI, permisos RBAC, procesamiento asíncrono y evolución a largo plazo.
- **Ingeniería de Datos Híbrida y Pipelines Automáticos de Auditoría:** Diseñé y administré la arquitectura de persistencia sobre **PostgreSQL, MongoDB y Redis** — optimizando consultas masivas sobre decenas de miles de activos heterogéneos y construyendo canalizaciones automáticas de exportación de auditoría (informes CSV) consumidas directamente por auditores internos y responsables de cumplimiento.
- **Orquestación Declarativa de Ciclo de Vida (Blueprint):** Concebí y desarrollé **Blueprint**, un motor asíncrono de orquestación en Python guiado por planos YAML versionados (conceptualmente análogo a Terraform). Integrado nativamente con Orion para orquestar aprovisionamiento en paralelo, trazabilidad completa por trabajo y **operaciones de destrucción idempotentes** que reanudan desmontajes parciales de forma segura — eliminando la necesidad de suites comerciales como Red Hat Automation Platform.
- **Migración de Jenkins a Dispatcher HA Propio:** Lideré la migración estratégica para dejar atrás Jenkins (tras haber estandarizado previamente el CI/CD entre equipos mediante **Jenkins Shared Libraries** modulares en Groovy) diseñando un **Dispatcher de Operaciones en Alta Disponibilidad** en Django y Celery con interfaz REST OpenAPI, lógica de reintentos a medida y observabilidad completa de ejecución.
- **Pipeline Universal por Drivers, Configuración en Runtime y Motor K8s:** Construí un pipeline universal de despliegue en Django basado en un **patrón modular de drivers** (desplegando sobre AWS, OpenStack, OpenShift y servidores físicos con la misma base de código), un **Sistema Centralizado de Gestión de Configuración** que inyecta variables de entorno dinámicamente en tiempo de despliegue, y un **Motor de Ejecución sobre Kubernetes Jobs** que ejecuta automatizaciones como contenedores efímeros aislados.
- **Interoperabilidad sin Downtime y Servicios Compartidos:** Desarrollé un **Puente API RESTful a medida entre F5 y OpenStack** sin tiempo de inactividad tras la deprecación oficial de la integración nativa del fabricante, y mantuve la **base de código Ansible** agnóstica de entorno que gobierna los clusters internos de **GitLab, Artifactory y Jenkins**.
- **IA Operativa (Orion AI — PoC Validada):** Concebí, diseñé y desarrollé una PoC multi-agente validada (**LangGraph, ReAct, Qwen 131k LLM**) que analiza concurrentemente logs de ejecución, runbooks operativos (indexados en Redis para RAG) y diffs de commits en GitLab bajo guardarraíles deterministas para reducir el triaje de CI/CD de horas a segundos; prototipo validado y preparado a la espera de directrices de integración con la infraestructura central de IA.
- **Integración Internacional, Operaciones en Producción y Mentoría:** Lideré la integración técnica y el onboarding de la plataforma con equipos de ingeniería en **México y Turquía**, asumí guardias e incidentes de producción a escala bancaria y formé a ingenieros en buenas prácticas de automatización y plataforma.

<p class="cv-tech"><strong>Tecnologías:</strong> Python, Django, DRF, Celery, AsyncIO, PostgreSQL, MongoDB, Redis, LangChain, LangGraph, ReAct, Model Context Protocol (MCP), Ansible, Kubernetes, OpenShift, AWS, OpenStack, Docker, Podman, Jenkins, GitLab CI, Groovy, F5, Infoblox.</p>

### Administrador y Desarrollador OpenStack
<p class="cv-meta"><strong>Oesia</strong> · Madrid · 2015 – 2017</p>

- **Operación de Nube Privada (OpenStack y Ceph):** Administré y mantuve una infraestructura de nube privada en producción basada en **OpenStack y almacenamiento distribuido Ceph**, garantizando disponibilidad, rendimiento y fiabilidad para los equipos internos.
- **Plataforma de Almacenamiento Privado (OpenStack Swift):** Diseñé y desarrollé una aplicación corporativa de almacenamiento en nube privada auto-alojada (equivalente conceptual a Dropbox) en Python sobre el almacenamiento de objetos **OpenStack Swift**, proporcionando compartición segura y escalable de archivos sin depender de nubes públicas.

<p class="cv-tech"><strong>Tecnologías:</strong> OpenStack, Ceph, Swift, Python, Linux.</p>

## Sistemas Destacados y Proyectos Open-Source

| Sistema | Alcance y Arquitectura |
| :--- | :--- |
| **[Orion — Plataforma IaaS](../projects/orion-iaas.md)** *(BBVA)* | Plano de control central en autoservicio con OpenAPI, capa híbrida PostgreSQL/MongoDB/Redis y pipelines automáticos de auditoría sobre AWS, OpenStack, OpenShift y bare-metal. |
| **[Blueprint — Motor Declarativo](../projects/blueprint.md)** *(BBVA)* | Orquestador asíncrono en Python guiado por YAML con concurrencia por olas DAG, trazabilidad de trabajos en Orion y desmontajes idempotentes reanudables. |
| **[Dispatcher HA, Gestión de Config y K8s Jobs](../projects/dispatcher-migration.md)** *(BBVA)* | Migración desde Jenkins Shared Libraries hacia un dispatcher de operaciones en Alta Disponibilidad con Django/Celery, inyección de variables en runtime y ejecución efímera en Kubernetes Jobs. |
| **Puente API F5 / OpenStack y Ansible Core** *(BBVA)* | Puente REST sin downtime que restauró la interoperabilidad de balanceadores F5 con OpenStack; automatización Ansible agnóstica de entorno para GitLab, Artifactory y Jenkins. |
| **[Orion AI — Auto-Diagnóstico CI/CD](../projects/orion-ai.md)** *(PoC BBVA)* | Prototipo multi-agente validado en LangGraph + ReAct que correlaciona logs, runbooks indexados en Redis y diffs de GitLab bajo guardarraíles deterministas. |
| **[OmniLecture Studio](../projects/omni-lecture.md)** *([GitHub](https://github.com/oredondo/omnilecture-studio))* | Suite nativa para Linux (Wayland/GNOME, GTK 3) de captura de pantalla/audio y pipeline en LangGraph con doble motor Whisper (`faster-whisper` `int8` + API) y OCR con OpenCV CLAHE + Tesseract. |
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
