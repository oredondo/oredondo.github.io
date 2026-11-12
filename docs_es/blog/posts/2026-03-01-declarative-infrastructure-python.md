---
draft: false
description: >-
  Por qué un equipo de plataforma corporativo reemplazó una suite comercial de orquestación por un motor AsyncIO ligero e idempotente guiado por YAML declarativo.
slug: declarative-yaml-engine-python
date: 2026-03-01
authors:
  - oredondo
categories:
  - Platform Engineering
  - Python
  - Architecture
tags:
  - IaC
  - Python
  - AsyncIO
  - PlatformEngineering
---

# Por qué construimos nuestro propio motor YAML declarativo en Python

En infraestructura empresarial, la respuesta por defecto a la orquestación suele ser adquirir una suite
comercial como Red Hat Automation Platform (Ansible Tower) o forzar una herramienta genérica en flujos para los que nunca fue concebida.

Aquí explicamos por qué decidimos desarrollar **Blueprint** —un motor de orquestación asíncrono propio en Python—
y cómo eliminó el bloqueo de proveedor garantizando idempotencia real sobre más de 30.000 máquinas bancarias.

<!-- more -->

## La trampa de las plataformas comerciales

Las suites de orquestación comerciales presentan a menudo tres problemas críticos en arquitecturas corporativas:

1. **Modelos de licencia restrictivos:** los costes escalan con el número de hosts gestionados o la frecuencia de operaciones, penalizando el crecimiento de la automatización.
2. **Caja negra y lagunas en auditoría:** cuando un trabajo falla en mitad de una secuencia de 50 pasos, reconstruir el estado exacto para los auditores es doloroso y costoso.
3. **Desajuste de integración (*impedance mismatch*):** las APIs internas del banco (como nuestra plataforma Orion) requieren semánticas de reintento específicas, inyección dinámica de variables y políticas de rollback a medida.

## La solución: Planos declarativos y asíncronos

Diseñamos **Blueprint** alrededor de tres principios fundamentales:

### 1. Especificaciones declarativas en YAML
Los desarrolladores no escriben scripts de ejecución procedimentales. Declaran el estado deseado de su pila de infraestructura en archivos YAML versionados en Git:

```yaml
version: "2.0"
target_environment: "aws-production"

resources:
  - name: "payment-worker-pool"
    type: "compute.instance_group"
    count: 12
    flavor: "m5.xlarge"
    driver: "aws"
    
  - name: "payment-redis-cache"
    type: "cache.cluster"
    engine: "redis"
    depends_on: ["payment-worker-pool"]
```

### 2. Ejecución mediante grafo acíclico dirigido (DAG)
El motor en Python analiza el manifiesto YAML, lo valida contra un esquema JSON Schema y construye un DAG de ejecución en memoria. Los componentes independientes se aprovisionan concurrentemente mediante `asyncio.gather()`, serializando estrictamente las dependencias.

### 3. Desmontajes idempotentes
A diferencia de los scripts ingenuos que fallan si un recurso ya fue eliminado, la operación destroy de Blueprint comprueba el estado real en vivo antes de actuar, reanudando desmontajes interrumpidos sin necesidad de manipular bases de datos manualmente.

## Conclusión

Construir un motor de plataforma propio no significa reinventar la rueda: significa saber cuándo un producto comercial acarrea más costes de licencia y fricción operativa que un motor asíncrono limpio de 2.000 líneas en Python perfectamente adaptado a la topología de tu organización.

---

*Puedes consultar la arquitectura detallada en el [caso de estudio de Blueprint](../../projects/blueprint.md).*
