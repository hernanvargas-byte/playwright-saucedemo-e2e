from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username = page.get_by_placeholder("Username")
        self.password = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button", name="Login")
        self.error_message = page.locator('[data-test="error"]')

    def open(self):
        self.page.goto("/")

    def login(self, user: str, password: str):
        self.username.fill(user)
        self.password.fill(password)
        self.login_button.click()