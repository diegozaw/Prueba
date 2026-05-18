# Ejecución

Crear archivo `.env`

```env
OPENAI_API_KEY=api_key
MODEL=gpt-4o-mini
```

Ejecutar: python -m src.run_query

# Tecnologías utilizadas

- Python 3.11+
- OpenAI API
- Pydantic
- python-dotenv

---

# Arquitectura del proyecto

```text
ai-ticket-analyzer/
│
├── src/
│   ├── __init__.py
│   ├── run_query.py
│   ├── openai_client.py
│   ├── ticket_service.py
│   ├── validators.py
│   ├── metrics.py
│   ├── models.py
│   └── safety.py
│
├── prompts/
│   └── main_prompt.txt
│
├── metrics/
│   └── metrics.csv
│
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

# Observabilidad y métricas

La aplicación registra métricas por ejecución para monitorear:
- consumo de tokens
- performance
- costos estimados

Las métricas registradas son:
- `prompt_tokens`
- `completion_tokens`
- `total_tokens`
- `latency_ms`
- `estimated_cost_usd`

La información se almacena en:

```text
metrics/metrics.csv
```

Esto permite:
- analizar consumo y costos
- medir tiempos de respuesta
- auditar ejecuciones
- comparar configuraciones del modelo
- monitorear estabilidad del sistema

---

# Ejemplo de métricas registradas

```json
{
  "prompt_tokens": 221,
  "completion_tokens": 66,
  "total_tokens": 287,
  "latency_ms": 6021.19,
  "estimated_cost_usd": 0.000073
}
```

---

# Cálculo de costos

Los costos estimados se calculan utilizando los precios públicos de OpenAI para el modelo `gpt-4o-mini`:

- Input tokens: USD 0.15 por 1 millón de tokens
- Output tokens: USD 0.60 por 1 millón de tokens

Los valores registrados son aproximados y se utilizan únicamente con fines de monitoreo y observabilidad.

---

# Ejemplo de uso

Input:

```text
No puedo iniciar sesión después de cambiar mi contraseña.
```

Output:

```json
{
  "category": "Problema de Login",
  "priority": "HIGH",
  "summary": "El usuario no puede acceder luego del cambio de contraseña.",
  "suggested_response": "Verifique las credenciales e intente restablecer la contraseña nuevamente."
}
```

# Tests

El proyecto incluye tests básicos para validar:
- estructura del JSON
- validación del esquema de salida

## Ejecutar tests

```bash
pytest
```