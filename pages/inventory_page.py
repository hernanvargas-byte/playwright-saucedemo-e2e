from playwright.sync_api import Page


class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.title = page.locator(".title")
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.sort_select = page.locator(".product_sort_container")
        self.prices = page.locator(".inventory_item_price")

    def add_to_cart(self, product_name: str):
        product = self.page.locator(".inventory_item").filter(has_text=product_name)
        product.get_by_role("button", name="Add to cart").click()

    def sort_by(self, option: str):
        self.sort_select.select_option(option)

    def price_values(self) -> list[float]:
        return [float(p.replace("$", "")) for p in self.prices.all_inner_texts()]