---
title: Sobre mí
description: >-
  Sobre Oscar Redondo — Senior Platform Engineer · Python en Madrid. Filosofía de ingeniería, trayectoria arquitectónica y contacto.
hide:
  - navigation
---

# Sobre mí

Soy **Oscar Redondo**, **Senior Platform Engineer · Python** afincado en Madrid, España.

Durante la última década, mi carrera ha girado en torno a una única pregunta: **¿cómo lograr que cientos de ingenieros desplieguen rápido sobre decenas de miles de servidores heterogéneos sin sacrificar el gobierno, la fiabilidad ni el descanso en las guardias?**

Mi respuesta consiste en tratar la infraestructura interna como un producto de software — trazando **Golden Paths** mediante APIs limpias, abstracciones por drivers y motores declarativos donde la seguridad, la auditoría y la recuperación ante fallos vienen integradas por diseño en lugar de imponerse mediante colas de tickets manuales.

## Trayectoria Arquitectónica

- **Desde el almacenamiento y los hipervisores hacia arriba:** Me formé en Ingeniería Electrónica de Comunicaciones en la **Universidad Politécnica de Madrid** y comencé mi carrera en **Oesia** administrando una nube privada en producción con **OpenStack y Ceph** y desarrollando una plataforma de almacenamiento sobre **OpenStack Swift**. Empezar cerca de los clusters de almacenamiento, hipervisores y redes marcó mi forma de diseñar abstracciones de alto nivel.
- **Construyendo la plataforma cloud interna de un banco capa por capa:** Desde 2017 en **BBVA Technology**, soy el arquitecto único y responsable de la suite central de plataforma IaaS (**Orion** y **Blueprint**). Cada vez que una herramienta estándar se convertía en un cuello de botella de escala o licenciamiento, diseñé un reemplazo en Python — migrando de Jenkins a un **Dispatcher HA en Django/Celery**, desacoplando la configuración en runtime, ejecutando cargas en **Kubernetes Jobs**, conectando **F5 y OpenStack** sin tiempo de inactividad y desarrollando **Orion AI (PoC)** con LangGraph y ReAct.
- **Ingeniería open-source:** Fuera del ámbito corporativo, diseño y mantengo proyectos open-source de IA y backend en GitHub — como **[OmniLecture Studio](https://github.com/oredondo/omnilecture-studio)** (suite multimodal nativa en Linux Wayland/GTK 3) y **[WrenchBuddy](https://github.com/oredondo/WrenchBuddy)** (plataforma de ciclo de vida de vehículos con Django 6, Celery y RAG sobre `pgvector`).

## Principios de Ingeniería

<div class="grid cards" markdown>

-   :material-road-variant:{ .lg .middle } __Trazar Golden Paths, no colas de tickets__

    ---

    Si un ingeniero necesita un manual de 20 páginas o un ticket de aprobación manual para aprovisionar infraestructura estándar, la abstracción ha fracasado. Las APIs en autoservicio deben hacer que el camino seguro y auditable sea también el más sencillo.

-   :material-file-code-outline:{ .lg .middle } __Estado declarativo y recuperación idempotente__

    ---

    Crear recursos desde cero es sencillo; recuperarse de un fallo a mitad de un desmontaje de 30 pasos es donde se pone a prueba un sistema. Toda operación debe consultar el estado en vivo y ser segura de relanzar.

-   :material-shield-check-outline:{ .lg .middle } __Guardarraíles deterministas alrededor de la IA__

    ---

    Los LLMs y grafos multi-agente transforman el triaje operativo solo cuando se tratan como componentes no confiables — acotados por esquemas tipados, contratos de herramientas de solo lectura (MCP) y verificación estricta de evidencias.

-   :material-account-group-outline:{ .lg .middle } __Responsabilidad extremo a extremo y colaboración internacional__

    ---

    Llevar el busca de guardia de lo que diseñas mantiene la arquitectura honesta. Compartir esa arquitectura entre equipos — desde formar a ingenieros junior hasta integrar centros de ingeniería en España, México y Turquía — es lo que hace que una plataforma perdure.

</div>

## Fuera de la Terminal

Cuando no estoy frente al código, suelo estar rodando o haciendo mantenimiento a mi moto (la inspiración real detrás de [WrenchBuddy](projects/wrenchbuddy.md)), haciendo snowboard, de ruta por la montaña o escuchando música.

## Contacto

- :fontawesome-brands-linkedin: **LinkedIn:** [linkedin.com/in/oscarredondodjangopython](https://linkedin.com/in/oscarredondodjangopython)
- :fontawesome-brands-github: **GitHub:** [github.com/oredondo](https://github.com/oredondo)
- :material-email-outline: **Email:** [o.redondo91@gmail.com](mailto:o.redondo91@gmail.com)
