import json
import time

from src.openai_client import client, MODEL
from src.models import TicketAnalysis

INPUT_COST_PER_1M = 0.15
OUTPUT_COST_PER_1M = 0.60


def load_prompt(ticket_text):

    with open(
        "prompts/main_prompt.txt",
        "r",
        encoding="utf-8"
    ) as file:

        template = file.read()

    return template.replace("{user_ticket}", ticket_text)


def analyze_ticket(ticket_text):

    prompt = load_prompt(ticket_text)

    start_time = time.time()

    response = client.chat.completions.create(
        model=MODEL,
        temperature=0.2,
        max_tokens=100,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    end_time = time.time()

    latency_ms = round((end_time - start_time) * 1000, 2)

    content = response.choices[0].message.content

    data = json.loads(content)

    validated = TicketAnalysis(**data)

    usage = response.usage

    prompt_tokens = usage.prompt_tokens
    completion_tokens = usage.completion_tokens
    total_tokens = usage.total_tokens

    estimated_cost_usd = (
    (prompt_tokens / 1_000_000) * INPUT_COST_PER_1M +
    (completion_tokens / 1_000_000) * OUTPUT_COST_PER_1M
    )

    estimated_cost_usd = round(estimated_cost_usd, 6)

    metrics = {
        "prompt_tokens": prompt_tokens,
        "completion_tokens": completion_tokens,
        "total_tokens": total_tokens,
        "latency_ms": latency_ms,
        "estimated_cost_usd": estimated_cost_usd
    }

    return validated, metrics