# Ejecución

Ejecutar python -m app.main

# AI Ticket Analyzer

Proyecto integrador desarrollado en Python utilizando la API de OpenAI.

La aplicación analiza tickets de soporte utilizando un LLM para:
- clasificar el problema
- detectar prioridad
- resumir el incidente
- generar una respuesta sugerida

El sistema devuelve una salida estructurada en formato JSON lista para ser consumida por otros sistemas.


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
├── app/
│   ├── main.py
│   ├── openai_client.py
│   ├── prompt_builder.py
│   ├── ticket_service.py
│   ├── validators.py
│   ├── metrics.py
│   └── models.py
│
├── logs/
│   └── metrics.csv
│
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

# Funcionalidades

- Análisis automático de tickets
- Clasificación de categoría
- Detección de prioridad
- Generación de resumen
- Respuesta sugerida automática
- Salida estructurada JSON
- Validación con Pydantic
- Registro de métricas
- Manejo básico de errores
- Protección básica contra prompt injection

---

# Técnica de Prompt Engineering utilizada

Se utilizó una combinación de:

## Role Prompting

El modelo recibe el rol de:
> "Senior Customer Support Analyst"

Esto mejora consistencia y calidad de respuestas.


## Low Temperature

Se utilizó:
```python
temperature=0.2
```

para reducir:
- alucinaciones
- variabilidad
- respuestas inconsistentes
- JSON inválido

---

# Modelo utilizado

Modelo:
```text
gpt-4.1-mini
```

Motivos:
- bajo costo
- alta velocidad
- buena capacidad de structured output
- suficiente calidad para el MVP

---

# Salida estructurada

La aplicación devuelve un contrato JSON estable:

```json
{
  "category": "Problema de Login",
  "priority": "HIGH",
  "summary": "El usuario no puede iniciar sesión.",
  "suggested_response": "Por favor restablezca la contraseña nuevamente."
}
```

---

# Métricas

El sistema registra:
- tokens de entrada
- tokens de salida
- tokens totales

Las métricas se almacenan en:

```text
logs/metrics.csv
```

Esto permite:
- analizar consumo
- estimar costos
- auditar ejecuciones

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

