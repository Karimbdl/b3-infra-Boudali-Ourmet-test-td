from product import Product

class Cart:
    def __init__(self):
        self.items = {}  # {product: quantity}

    def add_product(self, product: Product, quantity: int):
        if product.stock < quantity:
            raise ValueError(f"Cannot add {quantity} of {product.name}. Only {product.stock} left.")
        self.items[product] = self.items.get(product, 0) + quantity

    def remove_product(self, product: Product):
        if product in self.items:
            del self.items[product]
        else:
            raise KeyError(f"{product.name} is not in the cart.")
    
    def videPanier(self):
        self.items.clear()
    
    def modifyPanier(self, product: Product, quantity:int):
        if product not in self.items:
            raise KeyError(f"{product.name} n'est pas dans le cart ")
        if quantity <= 0 : 
            del self.items[product]
        else:
            if quantity > product.stock: 
                raise ValueError(f"Ne peut mettre la quantité en {quantity}. Only {product.stock}")
            self.items[product] = quantity
            
    def coupon(self, code: str, percentage: int):
        if percentage <= 0 or percentage > 100:
            raise ValueError('Invalid discount percentage.')
        self.discount = percentage  # Ajoute une propriété de réduction au panier

    def calculate_total(self):
        total = sum(product.price * quantity for product, quantity in self.items.items())
        if hasattr(self, 'discount'):  # Vérifie si une réduction est appliquée
            total -= total * (self.discount / 100)
        return total


    def display_cart(self):
        if not self.items:
            return "Your cart is empty."
        return "\n".join([f"{product.name} x {quantity} - {product.price * quantity}€"
                          for product, quantity in self.items.items()])