from src.ticket_service import analyze_ticket
from src.validators import validate_input
from src.metrics import save_metrics
from src.safety import detect_prompt_injection


def main():

    print("=== AI Ticket Analyzer ===")

    ticket = input("Describe el problema: ")

    try:

        validate_input(ticket)

        if detect_prompt_injection(ticket):
            print("\nPotential prompt injection detected.")
            return

        result, metrics = analyze_ticket(ticket)

        print("\nResultado:\n")
        print(result.model_dump_json(indent=2))

        print("\nMétricas:\n")
        print(metrics)

        save_metrics(metrics)

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()