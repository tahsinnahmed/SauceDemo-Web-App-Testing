from pom.inventory_page import InventoryPage
from pom.cart_page import CartPage
from pom.checkout_page import CheckoutPage

def test_checkout(logged_in_driver):
    inventory = InventoryPage(logged_in_driver)
    inventory.add_item()
    inventory.go_cart()

    cart = CartPage(logged_in_driver)
    cart.proceed_checkout()

    checkout = CheckoutPage(logged_in_driver)
    checkout.checkout()