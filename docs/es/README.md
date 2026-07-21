# Fernando Abishai Agent Skills

Catálogo de flujos de ingeniería de software orientados a evidencia para Codex, Claude Code, Cursor, OpenCode y otros agentes compatibles con Agent Skills.

> **Regla principal:** un agente puede proponer libremente, pero solo puede afirmar que terminó cuando haya ejecutado el límite relevante del sistema y registrado el resultado.

## Instalación

```bash
npx skills@latest add FernandoAbishai/agent-skills
```

Para instalar todo el catálogo globalmente en Codex y Claude Code:

```bash
npx skills@latest add FernandoAbishai/agent-skills \
  --skill '*' \
  --agent codex \
  --agent claude-code \
  --global \
  --yes
```

Invocación independiente:

```text
Claude Code: /fernandoabishai <tarea>
Codex:       $fernandoabishai <tarea>
```

Como plugin nativo de Claude Code:

```text
/plugin marketplace add FernandoAbishai/agent-skills
/plugin install fa-engineering@fernandoabishai
```

Invocación del plugin:

```text
/fa-engineering:fernandoabishai <tarea>
```

## Ciclo de evidencia

```text
ACLARAR → ESPECIFICAR → DIVIDIR → IMPLEMENTAR → DEPURAR / REVISAR → VERIFICAR → PUBLICAR
```

## Qué problema resuelve

Los agentes de programación suelen:

- modificar código antes de entender el comportamiento solicitado;
- confundir archivos cambiados con funcionalidad comprobada;
- quedarse con la primera hipótesis durante una depuración;
- planificar por capas técnicas en lugar de entregar capacidades completas;
- declarar éxito porque una prueba aislada pasó;
- mezclar intención, comportamiento, riesgo y diseño en una revisión genérica.

Estas skills convierten disciplina de ingeniería en procesos pequeños y reutilizables con artefactos y criterios de finalización comprobables.

## Catálogo inicial

### Flujos invocados por el usuario

- `fernandoabishai`: enruta la tarea al flujo mínimo necesario.
- `setup-engineering-context`: descubre comandos, arquitectura y límites del repositorio.
- `clarify-change`: resuelve decisiones de comportamiento, alcance y seguridad.
- `write-change-spec`: crea una especificación neutral respecto a la implementación.
- `plan-delivery`: divide el trabajo en incrementos verticales y reversibles.
- `implement-change`: implementa una porción verificada a la vez.

### Disciplinas invocadas por el modelo

- `debug-with-evidence`: depura con reproducción, hipótesis competidoras y experimentos discriminantes.
- `review-change`: revisa intención, comportamiento, riesgo y diseño por separado.
- `verify-system`: comprueba el recorrido completo de ejecución.
- `ship-with-evidence`: prepara evidencia de publicación, monitoreo y rollback.

## Diferenciación

El repositorio no pretende ser una traducción ni una copia renombrada de otro catálogo. Su tesis específica es que la evidencia, los límites de autorización, la verificación en runtime y los criterios de finalización deben formar parte central de cada flujo.

Todavía es una versión temprana. No se presenta como universalmente superior a repositorios más maduros; debe demostrar su valor mediante comparaciones y evaluaciones reproducibles.

## Recursos

Los templates y referencias viven dentro de cada skill para que sigan disponibles aunque el usuario instale una sola skill.

```text
skill-name/
├── SKILL.md
├── agents/openai.yaml
├── references/
├── templates/
└── examples/
```

Consulta el [README principal](../../README.md) y el [catálogo de ingeniería](../../skills/engineering/README.md) para más detalles.
