# Desarrollo de un Microservicio de Gestión de Productos

En el contexto de una empresa fintech, necesitas desarrollar un microservicio que gestione productos financieros. Cada producto tiene un nombre, precio, stock y categoría. El sistema no debe permitir productos con nombres duplicados ni precios negativos. El objetivo es crear un microservicio robusto y escalable que pueda ser integrado en un sistema más amplio de gestión de finanzas.

## Informacion General

| Campo | Valor |
|-------|-------|
| **Tema** | Desarrollo |
| **Nivel** | advanced-l2 |
| **Tipo** | practical |
| **Tiempo estimado** | 4-6 horas |

## Fases del Reto

### Fase 0: Configuración del Proyecto

**Objetivo:** Obtener el proyecto base funcional enviando el Código Base a un asistente de IA, que lo analizará, corregirá errores y generará un ZIP listo para usar.

**Tiempo estimado:** 15-30 minutos

**Instrucciones:**

- Asegúrate de tener instalado para ejecutar el proyecto: Python 3.10+, pip, VS Code o similar.
- Copia todo el contenido del campo **Código Base** de este reto — incluyendo el texto de instrucciones que aparece al inicio.
- Abre un asistente de IA (Claude en claude.ai, ChatGPT o Gemini — se recomienda Claude), pega el contenido copiado en el chat y envíalo.
- El asistente analizará los archivos, corregirá errores y generará un archivo ZIP descargable. Descárgalo y extráelo en la carpeta donde quieras trabajar.
- Ejecuta `pip install -r requirements.txt` y luego arranca el proyecto. Si no hay errores, estás listo.

**Entregable:** El proyecto compila/arranca sin errores.

<details>
<summary>Pistas de conocimiento</summary>

- Copia el Código Base completo incluyendo el texto de instrucciones al inicio — esas instrucciones le indican al asistente exactamente qué hacer con los archivos.
- Si el asistente no genera el ZIP automáticamente al terminar el análisis, escríbele: "genera el ZIP ahora".
- Si el proyecto tiene errores al arrancar, comparte el mensaje de error con el mismo asistente para que lo corrija.

</details>

### Fase 1: Definición de Requisitos y Diseño Inicial

**Objetivo:** Definir los requisitos funcionales y no funcionales del microservicio y diseñar su estructura inicial.

**Tiempo estimado:** 1 hora

**Instrucciones:**

- Identifica los requisitos funcionales y no funcionales del microservicio de gestión de productos.
- Diseña la estructura inicial del microservicio, incluyendo los endpoints necesarios y las validaciones a implementar.

**Entregable:** Documento de diseño inicial con los requisitos y la estructura propuesta del microservicio.

<details>
<summary>Pistas de conocimiento</summary>

- Considera las reglas de negocio y las restricciones del dominio al definir los requisitos.
- Piensa en cómo el microservicio se integrará con otros componentes del sistema.

</details>

### Fase 2: Implementación de Endpoints y Validaciones

**Objetivo:** Implementar los endpoints del microservicio y las validaciones necesarias para asegurar la integridad de los datos.

**Tiempo estimado:** 2 horas

**Instrucciones:**

- Implementa los endpoints del microservicio para crear, leer, actualizar y eliminar productos.
- Agrega las validaciones necesarias para asegurar que los productos no tengan nombres duplicados ni precios negativos.

**Entregable:** Microservicio con endpoints implementados y validaciones funcionales.

<details>
<summary>Pistas de conocimiento</summary>

- Utiliza un enfoque iterativo para implementar y probar cada endpoint.
- Considera cómo manejar los errores de validación y proporcionar mensajes de error claros al usuario.

</details>

### Fase 3: Integración y Pruebas

**Objetivo:** Integrar el microservicio con otros componentes del sistema y realizar pruebas exhaustivas.

**Tiempo estimado:** 2 horas

**Instrucciones:**

- Integra el microservicio con otros componentes del sistema, como el servicio de autenticación y el servicio de notificaciones.
- Realiza pruebas unitarias y de integración para asegurar que el microservicio funciona correctamente en diferentes escenarios.

**Entregable:** Microservicio integrado y pruebas unitarias y de integración realizadas.

<details>
<summary>Pistas de conocimiento</summary>

- Utiliza un enfoque de pruebas impulsadas por el comportamiento (BDD) para asegurar que el microservicio cumple con los requisitos.
- Considera cómo simular diferentes escenarios de uso y errores para probar la robustez del microservicio.

</details>

## Dimensiones Evaluadas

- **queEs**: ¿Qué es un microservicio y por qué se utiliza en este contexto?
- **paraQueSirve**: ¿Para qué sirve el microservicio de gestión de productos en el sistema fintech?
- **comoSeUsa**: ¿Cómo se usan los endpoints del microservicio para crear, leer, actualizar y eliminar productos?
- **erroresComunes**: ¿Qué errores comunes pueden ocurrir al implementar las validaciones de datos y cómo se manejan?
- **queDecisionesImplica**: ¿Qué decisiones implica la integración del microservicio con otros componentes del sistema?

## Criterios de Evaluacion

- Definición clara de los requisitos funcionales y no funcionales del microservicio.
- Diseño inicial del microservicio con endpoints y validaciones propuestas.
- Implementación de los endpoints del microservicio y validaciones funcionales.
- Integración del microservicio con otros componentes del sistema y realización de pruebas exhaustivas.

## Como trabajar con un asistente de IA

- **AGENTS.md** — instrucciones nativas del repo (Cursor, Codex, Copilot, Gemini, Claude Code). Abrí el proyecto y el agente las carga solo.
- **PROMPT_MEJORA.md** — el mismo prompt, para copiar y pegar en un chat (claude.ai, ChatGPT, etc.).

---

*Reto generado automaticamente por Challenge Generator - Pragma*
