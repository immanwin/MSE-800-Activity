from shop import calculate_price
    
def get_tax_rate():
    """Stands in for a call to a web service (slow, needs a network)."""
    raise RuntimeError("tax service unavailable")
def total_with_tax(unit_price, quantity):
    return round(calculate_price(unit_price, quantity) * (1 + get_tax_rate()), 2)