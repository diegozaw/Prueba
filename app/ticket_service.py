import json

from app.openai_client import client, MODEL
from app.prompt_builder import build_prompt
from app.models import TicketAnalysis


def analyze_ticket(ticket_text: str):

    prompt = build_prompt(ticket_text)

    response = client.chat.completions.create(
        model=MODEL,
        temperature=0.2,
        max_tokens=300,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    content = response.choices[0].message.content

    data = json.loads(content)

    validated = TicketAnalysis(**data)

    return validated, response.usage