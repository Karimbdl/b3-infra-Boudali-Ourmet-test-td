import  unittest
import sys

sys.path.append('GIT/cart.py')
from cart import Cart
from product import Product



class TestCart(unittest.TestCase):
    def setUp(self):
        self.cart = Cart()
        self.product1 = Product(name="Laptop", price=1000, stock=5)
        self.product2 = Product(name="Mouse", price=50, stock=10)

    def test_application_coupon(self):
        """Test d'application d'un coupon valide."""
        self.cart.add_product(self.product1, 2)
        self.cart.coupon("SUMMER10", 10)
        self.assertEqual(self.cart.calculate_total(), 1800)

    def coupon_invalide(self):
        """Test d'application d'un coupon avec un pourcentage invalide."""
        with self.assertRaises(ValueError):
            self.cart.coupon("INVALID", -10)

    def test_modify_cart_success(self):
        """Test de modification de la quantité d'un produit existant."""
        self.cart.add_product(self.product1, 3)
        self.cart.modifyPanier(self.product1, 2)
        self.assertEqual(self.cart.items[self.product1], 2)



if __name__ == "__main__":
    unittest.main()