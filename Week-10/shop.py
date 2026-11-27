class OutOfStockError(Exception):
    """Raised when more items are sold than are in stock."""

def calculate_price(unit_price, quantity, discount_rate=0.0):
    """Return the price for a quantity of items, rounded to 2 decimal places."""
    if unit_price <= 0:
        raise ValueError("unit_price must be positive")
    if quantity < 1:
        raise ValueError("quantity must be at least 1")
    if not 0 <= discount_rate < 1:
        raise ValueError("discount_rate must be in the range [0, 1)")
    return round(unit_price * quantity * (1 - discount_rate), 2)
class Product:
    def __init__(self, name, price, stock=0):
        self.name = name
        self.price = price
        self.stock = stock
    @property
    def in_stock(self):
        return self.stock > 0
 
    def sell(self, quantity=1):
        if quantity < 1:
            raise ValueError("quantity must be at least 1")
        if quantity > self.stock:
            raise OutOfStockError(f"Not enough {self.name} in stock")
        self.stock -= quantity
    def restock(self, quantity):
        if quantity < 1:
            raise ValueError("quantity must be at least 1")
        self.stock += quantity
class Inventory:
    def __init__(self):
        self._products = []
 
    def add(self, product):
        self._products.append(product)
 
    def in_stock_products(self):
        return [p for p in self._products if p.in_stock]
 
    def cheapest_in_stock(self):
        products = self.in_stock_products()
        if not products:
            return None
        return min(products, key=lambda p: p.price)
