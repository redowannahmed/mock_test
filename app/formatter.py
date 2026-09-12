def format_currency(value):
    """Format a number as currency."""
    return f"${value:.2f}"


def format_percentage(value):
    """Format a decimal value as a percentage."""
    return f"{value * 100:.1f}%"


def format_number(value):
    """Format a number with two decimal places."""
    return f"{value:.2f}"