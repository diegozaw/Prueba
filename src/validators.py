def validate_input(text: str):

    if not text.strip():
        raise ValueError("Ticket vacío")

    if len(text) < 10:
        raise ValueError("Ticket demasiado corto")