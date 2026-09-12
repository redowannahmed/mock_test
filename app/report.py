from app.calculator import calculate_discount


class SalesReport:
    def __init__(self, items):
        self.items = items

    def calculate_totals(self):
        total = 0

        for item in self.items:
            total += calculate_discount(
                item["price"],
                item["discount_rate"],
            )

        return total

    def get_rows(self):
        return self.items