from app.ticket_service import analyze_ticket
from app.validators import validate_input
from app.metrics import save_metrics


def main():

    print("=== AI Ticket Analyzer ===")

    ticket = input("Describe el problema: ")

    try:

        validate_input(ticket)

        result, usage = analyze_ticket(ticket)

        print("\nResultado:\n")
        print(result.model_dump_json(indent=2))

        save_metrics(
            usage.prompt_tokens,
            usage.completion_tokens,
            usage.total_tokens
        )

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()