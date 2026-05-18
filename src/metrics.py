import csv
import os

from datetime import datetime


def save_metrics(metrics):

    os.makedirs("metrics", exist_ok=True)

    file_path = "metrics/metrics.csv"

    file_exists = os.path.isfile(file_path)

    with open(
        file_path,
        "a",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        if not file_exists:

            writer.writerow([
                "timestamp",
                "prompt_tokens",
                "completion_tokens",
                "total_tokens",
                "latency_ms",
                "estimated_cost_usd"
            ])

        writer.writerow([
            datetime.now(),
            metrics["prompt_tokens"],
            metrics["completion_tokens"],
            metrics["total_tokens"],
            metrics["latency_ms"],
            metrics["estimated_cost_usd"]
        ])