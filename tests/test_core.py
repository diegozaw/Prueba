from src.models import TicketAnalysis


def test_ticket_analysis_schema():

    data = {
        "category": "Problema de Login",
        "priority": "HIGH",
        "summary": "El usuario no puede iniciar sesión.",
        "suggested_response": "Por favor verifique sus credenciales."
    }

    result = TicketAnalysis(**data)

    assert result.category == "Problema de Login"
    assert result.priority == "HIGH"