# Desarrollo de un Sistema de Gestión de Tareas

El sistema necesita un módulo de gestión de tareas para un equipo de desarrollo. Cada tarea debe tener un título, descripción, estado (pendiente, en progreso, completada) y fecha de vencimiento. El sistema debe permitir crear, actualizar y eliminar tareas, así como listarlas por estado y fecha. Es importante que el sistema sea escalable y maneje concurrentemente múltiples usuarios.

## Informacion General

| Campo | Valor |
|-------|-------|
| **Tema** | Desarrollo |
| **Nivel** | advanced-l1 |
| **Tipo** | practical |
| **Tiempo estimado** | 4-6 horas |

## Fases del Reto

### Fase 0: Configuración del Proyecto

**Objetivo:** Obtener el proyecto base funcional enviando el Código Base a un asistente de IA, que lo analizará, corregirá errores y generará un ZIP listo para usar.

**Tiempo estimado:** 15-30 minutos

**Instrucciones:**

- Asegúrate de tener instalado para ejecutar el proyecto: Un IDE o editor de código.
- Copia todo el contenido del campo **Código Base** de este reto — incluyendo el texto de instrucciones que aparece al inicio.
- Abre un asistente de IA (Claude en claude.ai, ChatGPT o Gemini — se recomienda Claude), pega el contenido copiado en el chat y envíalo.
- El asistente analizará los archivos, corregirá errores y generará un archivo ZIP descargable. Descárgalo y extráelo en la carpeta donde quieras trabajar.
- Verifica que el proyecto arranca sin errores.

**Entregable:** El proyecto compila/arranca sin errores.

<details>
<summary>Pistas de conocimiento</summary>

- Copia el Código Base completo incluyendo el texto de instrucciones al inicio — esas instrucciones le indican al asistente exactamente qué hacer con los archivos.
- Si el asistente no genera el ZIP automáticamente al terminar el análisis, escríbele: "genera el ZIP ahora".
- Si el proyecto tiene errores al arrancar, comparte el mensaje de error con el mismo asistente para que lo corrija.

</details>

### Fase 1: Definición del Modelo de Datos

**Objetivo:** Definir la estructura de datos para las tareas y sus atributos.

**Tiempo estimado:** 1 hora

**Instrucciones:**

- Identifica los atributos necesarios para una tarea.
- Decide cómo representar el estado de una tarea.
- Considera cómo manejar la fecha de vencimiento.

**Entregable:** Diagrama de modelo de datos para las tareas.

<details>
<summary>Pistas de conocimiento</summary>

- Piensa en cómo representar la información de manera eficiente y escalable.
- Considera cómo manejar la concurrencia en la actualización de tareas.

</details>

### Fase 2: Implementación de la Creación de Tareas

**Objetivo:** Implementar la funcionalidad para crear nuevas tareas.

**Tiempo estimado:** 1.5 horas

**Instrucciones:**

- Diseña la interfaz para crear una nueva tarea.
- Implementa la lógica para validar los datos de entrada.
- Considera cómo manejar errores de validación.

**Entregable:** Módulo funcional para crear nuevas tareas.

<details>
<summary>Pistas de conocimiento</summary>

- Piensa en cómo validar los datos de entrada de manera eficiente.
- Considera cómo manejar los errores de validación de manera amigable para el usuario.

</details>

### Fase 3: Implementación de la Actualización de Tareas

**Objetivo:** Implementar la funcionalidad para actualizar tareas existentes.

**Tiempo estimado:** 1.5 horas

**Instrucciones:**

- Diseña la interfaz para actualizar una tarea.
- Implementa la lógica para validar los datos de entrada al actualizar.
- Considera cómo manejar la concurrencia en la actualización de tareas.

**Entregable:** Módulo funcional para actualizar tareas existentes.

<details>
<summary>Pistas de conocimiento</summary>

- Piensa en cómo validar los datos de entrada al actualizar una tarea.
- Considera cómo manejar la concurrencia en la actualización de tareas para evitar conflictos.

</details>

### Fase 4: Implementación de la Eliminación de Tareas

**Objetivo:** Implementar la funcionalidad para eliminar tareas.

**Tiempo estimado:** 1 hora

**Instrucciones:**

- Diseña la interfaz para eliminar una tarea.
- Implementa la lógica para confirmar la eliminación de una tarea.
- Considera cómo manejar la recuperación de datos eliminados por error.

**Entregable:** Módulo funcional para eliminar tareas.

<details>
<summary>Pistas de conocimiento</summary>

- Piensa en cómo confirmar la eliminación de una tarea para evitar eliminaciones accidentales.
- Considera cómo manejar la recuperación de datos eliminados por error.

</details>

## Dimensiones Evaluadas

- **queEs**: ¿Qué es una tarea en el contexto de este sistema?
- **paraQueSirve**: ¿Para qué sirve el módulo de gestión de tareas en el sistema?
- **comoSeUsa**: ¿Cómo se usa el módulo de gestión de tareas para crear, actualizar y eliminar tareas?
- **erroresComunes**: ¿Qué errores comunes pueden ocurrir al crear, actualizar o eliminar tareas y cómo se manejan?
- **queDecisionesImplica**: ¿Qué decisiones de diseño implica la implementación del módulo de gestión de tareas?

## Criterios de Evaluacion

- Definición del modelo de datos para las tareas.
- Implementación de la funcionalidad para crear nuevas tareas.
- Implementación de la funcionalidad para actualizar tareas existentes.
- Implementación de la funcionalidad para eliminar tareas.
- Manejo de errores comunes en la creación, actualización y eliminación de tareas.
- Toma de decisiones de diseño para el módulo de gestión de tareas.

## Como trabajar con un asistente de IA

- **AGENTS.md** — instrucciones nativas del repo (Cursor, Codex, Copilot, Gemini, Claude Code). Abrí el proyecto y el agente las carga solo.
- **PROMPT_MEJORA.md** — el mismo prompt, para copiar y pegar en un chat (claude.ai, ChatGPT, etc.).

---

*Reto generado automaticamente por Challenge Generator - Pragma*
