import csv
from datetime import datetime


def save_metrics(tokens_input, tokens_output, total_tokens):

    with open("logs/metrics.csv", "a", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        writer.writerow([
            datetime.now(),
            tokens_input,
            tokens_output,
            total_tokens
        ])