BLOCKED_PATTERNS = [
    "ignore previous instructions",
    "ignore all previous instructions",
    "reveal system prompt",
    "show api key",
    "developer message",
    "system prompt",
    "api key"
]


def detect_prompt_injection(text):

    text = text.lower()

    for pattern in BLOCKED_PATTERNS:

        if pattern in text:
            return True

    return False