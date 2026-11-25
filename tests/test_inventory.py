from playwright.sync_api import expect

from pages.inventory_page import InventoryPage


def test_agregar_producto_al_carrito(inventory: InventoryPage):
    inventory.add_to_cart("Sauce Labs Backpack")

    expect(inventory.cart_badge).to_have_text("1")


def test_ordenar_por_precio_menor_a_mayor(inventory: InventoryPage):
    inventory.sort_by("lohi")

    expect(inventory.prices.first).to_have_text("$7.99")
    precios = inventory.price_values()
    assert precios == sorted(precios)