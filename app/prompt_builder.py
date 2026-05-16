def build_prompt(user_ticket: str) -> str:

    return f"""
You are a senior customer support analyst.

Analyze the support ticket and return:
- category
- priority
- summary
- suggested_response

Rules:
- Priority must be LOW, MEDIUM or HIGH
- Summary max 30 words
- Professional tone
- Return ONLY valid JSON

Ticket:
{user_ticket}
"""