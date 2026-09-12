import csv

from app.formatter import format_percentage


class CSVExporter:
    def __init__(self, output_path):
        self.output_path = output_path

    def export_csv(self, rows):
        """Export report rows to CSV."""

        with open(self.output_path, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            writer.writerow([
                "product",
                "price",
                "discount",
            ])

            for row in rows:
                writer.writerow([
                    row["product"],
                    row["price"],
                    row["discount_rate"],
                ])

    def export_formatted_csv(self, rows):
        """Export rows with formatted discount values."""

        with open(
            self.output_path,
            "w",
            newline="",
            encoding="utf-8",
        ) as file:
            writer = csv.writer(file)

            writer.writerow([
                "product",
                "price",
                "discount",
            ])

            for row in rows:
                writer.writerow([
                    row["product"],
                    row["price"],
                    format_percentage(row["discount_rate"]),
                ])