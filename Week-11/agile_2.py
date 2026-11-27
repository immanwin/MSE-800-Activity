def calculate_rental_fee(days: int, daily_rate: float) -> float:
    """
    Calculates rental fee based on the rules:
    - Fewer than one day is an error.
    - Base fee is days multiplied by the daily rate.
    - 7 or more days get a 10% discount.
    """
    if days < 1:
        raise ValueError("Rental period must be at least 1 day.")

    total = days * daily_rate

    if days >= 7:
        total *= 0.90  # 10% off

    return round(total, 2)