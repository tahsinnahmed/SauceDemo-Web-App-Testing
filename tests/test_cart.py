from pom.inventory_page import InventoryPage

def test_cart(logged_in_driver):
    inventory = InventoryPage(logged_in_driver)
    inventory.add_item()
    inventory.go_cart()