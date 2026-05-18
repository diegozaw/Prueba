def build_prompt(user_ticket: str) -> str:

    return f"""
You are a senior customer support analyst.

Analyze the support ticket and return ONLY valid JSON.

Valid priorities:
- LOW
- MEDIUM
- HIGH

JSON format:
{{
    "category": "...",
    "priority": "...",
    "summary": "...",
    "suggested_response": "..."
}}

Example 1:

Ticket:
"I cannot log into my account after resetting my password."

Response:
{{
    "category": "Login Issue",
    "priority": "HIGH",
    "summary": "User cannot access account after password reset.",
    "suggested_response": "Please reset the password again and verify your credentials."
}}

Example 2:

Ticket:
"I would like to know if dark mode is available."

Response:
{{
    "category": "Feature Request",
    "priority": "LOW",
    "summary": "User asks about dark mode availability.",
    "suggested_response": "Thank you for your suggestion. We will share it with the product team."
}}

Now analyze this ticket:

Ticket:
"{user_ticket}"
"""