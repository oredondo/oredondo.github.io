---
title: Curriculum Vitae
description: >-
  CV de Oscar Redondo — Senior Python & Platform Engineer con más de 10 años construyendo
  plataformas internas de desarrollo, motores de automatización y sistemas de IA agéntica.
hide:
  - navigation
  - feedback
---

<div class="cv-actions no-print">
  <button class="md-button md-button--primary" onclick="window.print()">Imprimir / Guardar en PDF</button>
</div>

# Oscar Redondo

<p class="cv-headline">Senior Python &amp; Platform Engineer · DevOps &amp; Automatización · IA Aplicada</p>

<p class="cv-contact">
Madrid, España ·
<a href="mailto:o.redondo91@gmail.com">o.redondo91@gmail.com</a> ·
<a href="https://linkedin.com/in/oscarredondodjangopython">linkedin.com/in/oscarredondodjangopython</a> ·
<a href="https://github.com/oredondo">github.com/oredondo</a>
</p>

## Perfil profesional

Senior Python & Platform Engineer con **más de 10 años de experiencia** diseñando arquitecturas
para plataformas internas de alta escala, motores de automatización distribuida y flujos de trabajo
agénticos en producción.

Como **arquitecto único y responsable técnico de la suite IaaS central (Orion y Blueprint) para la Infraestructura Core Banking de BBVA**,
diseñé e implementé los sistemas que gobiernan **decenas de miles de máquinas** en AWS, OpenStack,
OpenShift y entornos locales, procesando **operaciones masivas diarias para más de 500
ingenieros**. Diseñé la arquitectura de datos subyacente (PostgreSQL, MongoDB, Redis) para soportar
operaciones de alto rendimiento, exportaciones masivas de auditoría y cumplimiento normativo estricto,
y desarrollé motores asíncronos en YAML que eliminaron el bloqueo de proveedor empresarial.

En la intersección entre ingeniería de plataformas e IA aplicada, construyo sistemas agénticos
fundamentados en estándares de ingeniería de software rigurosos: **Orion AI** (LangGraph / ReAct) automatiza
el diagnóstico de fallos en CI/CD bajo guardarraíles deterministas, reduciendo el tiempo de triaje de horas
a segundos. Con experiencia liderando arquitectura técnica con equipos internacionales en México y Turquía,
definiendo estándares de despliegue y formando ingenieros.

## Logros clave

- Diseñé y lidero la plataforma detrás de **operaciones diarias de infraestructura de alto rendimiento** sobre **decenas de miles de máquinas** en cloud híbrido para **más de 500 ingenieros**.
- Sustituí una **suite comercial de automatización con licencias recurrentes** por Blueprint, un motor declarativo AsyncIO propio en Python.
- Reduje el tiempo de entrega de aprovisionamiento **de días a minutos** mediante autoservicio sin tickets.
- Alcancé **100% de cumplimiento en auditoría** con canalizaciones automáticas de exportación de gobernanza.
- Desarrollé una PoC agéntica de diagnóstico que genera informes con evidencias citadas en **menos de 15 segundos** con **más del 94% de precisión** validada.

## Experiencia profesional

### Senior Python Developer, DevOps — Responsable de Plataforma IaaS
<p class="cv-meta"><strong>BBVA Technology</strong> (Infraestructura Core Banking) · Madrid · 2017 – Presente</p>

- **Arquitectura de la plataforma central IaaS:** Diseñó y lideró como arquitecto único la suite central de automatización IaaS (Orion y Blueprint), gobernando **decenas de miles de nodos** en cloud híbrido (AWS, OpenStack, OpenShift) para **más de 500 ingenieros**, mediante una capa abstracta de drivers en Python y un tejido de tareas distribuidas en Celery.
- **Velocidad de entrega en autoservicio:** Aceleró los plazos de aprovisionamiento de infraestructura **de varios días a minutos** eliminando la gestión manual de tickets, diseñando APIs REST en autoservicio con Django REST Framework y un motor de estados asíncrono orientado a eventos.
- **Eliminación de software comercial:** Eliminó el coste recurrente de licencias comerciales de automatización en cientos de servidores, diseñando e implementando **Blueprint**: un orquestador declarativo propio en Python asíncrono con `graphlib.TopologicalSorter` y `asyncio.TaskGroup`.
- **Cumplimiento normativo y auditoría:** Alcanzó un **100% de cumplimiento en auditorías regulatorias bancarias**, diseñando una arquitectura híbrida de persistencia que combina registros inmutables en PostgreSQL para trazabilidad SOX con MongoDB para indexación polimórfica de activos.
- **IA operativa y reducción de MTTR:** Redujo el tiempo de triaje de incidencias en CI/CD **de horas a menos de 15 segundos** con **más del 94% de precisión** validada, creando **Orion AI**: un sistema multi-agente cíclico en LangGraph con bucles ReAct y guardarraíles deterministas de citación de evidencias.
- **Habilitación técnica internacional:** Estandarizó la adopción de la plataforma en los centros de ingeniería de **España, México y Turquía**, liderando sesiones de arquitectura técnica internacional, definiendo estándares corporativos de despliegue y desarrollando extensiones dedicadas.
- **Resiliencia en producción:** Mantuvo una **disponibilidad superior al 99.9% en operaciones diarias de alto rendimiento**, diseñando caché distribuida en Redis, aislamiento de colas Celery por proveedor y liderando la respuesta a incidentes en guardias para pipelines bancarios críticos.

<p class="cv-tech"><strong>Tecnologías:</strong> Python, Django, DRF, Celery, AsyncIO, MongoDB, PostgreSQL, Redis, LangChain, LangGraph, ReAct, Model Context Protocol (MCP), Ansible, Jenkins, GitLab CI, AWS, OpenStack, OpenShift, Kubernetes, Docker, Podman, Groovy, Infoblox, F5.</p>

### Administrador y Desarrollador OpenStack
<p class="cv-meta"><strong>Oesia</strong> · Madrid · 2015 – 2017</p>

- **Almacenamiento en nube privada:** Implementó una plataforma corporativa de almacenamiento en nube privada para equipos de desarrollo internos, diseñando un servicio de compartición de archivos en Python sobre el almacenamiento de objetos de **OpenStack Swift**.
- **Fiabilidad de infraestructura:** Garantizó la alta disponibilidad y redundancia de datos en entornos multi-inquilino, administrando clusters en producción de **OpenStack y almacenamiento distribuido Ceph**, gestionando monitorización, aprovisionamiento y mantenimiento de nodos.

<p class="cv-tech"><strong>Tecnologías:</strong> OpenStack, Ceph, Swift, Python, Linux.</p>

## Habilidades técnicas

| Categoría | Tecnologías |
| :--- | :--- |
| **Arquitectura core y lenguajes** | Python (experto), AsyncIO, Celery, Django, Django REST Framework, Groovy, Bash, SQL |
| **IA aplicada y sistemas agénticos** | LangGraph, LangChain, bucles ReAct, Model Context Protocol (MCP), bases vectoriales, RAG, Whisper |
| **Infraestructura cloud y plataformas** | AWS, OpenStack, OpenShift, Kubernetes, Docker, Podman, Ceph, F5, Infoblox |
| **IaC declarativo y automatización** | Blueprint (motor YAML asíncrono propio), GitOps, Ansible, conceptos Terraform |
| **Bases de datos y mensajería** | PostgreSQL, MongoDB, Redis, RabbitMQ / colas de trabajadores Celery |
| **CI/CD y entrega continua** | GitLab CI, Jenkins (librerías compartidas Groovy), despachadores HA de operaciones |

## Formación académica

**Grado en Ingeniería Electrónica de Comunicaciones**
<p class="cv-meta"><strong>Universidad Politécnica de Madrid</strong> · 2009 – 2016</p>

Ingeniería de telecomunicación y sistemas electrónicos con fundamentos sólidos en software, integración hardware, diseño de sistemas digitales y arquitectura de redes.

## Certificaciones y formación continua

| Año | Curso | Proveedor |
| :--- | :--- | :--- |
| 2026 | Complete MCP Developer Guide: Agents, Servers & Tools | Udemy |
| 2026 | Curso Completo: LangChain, LangGraph y Agentes de IA con Python | Udemy |
| 2026 | Curso Completo de Spec-Driven Development (SDD) y Agentes IA | Udemy |
| 2026 | Curso Completo: Bases de Datos Vectoriales para IA Generativa | Udemy |
| 2025 | Developing Secure Software (LFD121) | Linux Foundation |
