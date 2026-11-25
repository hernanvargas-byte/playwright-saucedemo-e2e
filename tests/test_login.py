import re

from playwright.sync_api import Page, expect

from pages.login_page import LoginPage


def test_login_exitoso(page: Page):
    login = LoginPage(page)
    login.open()
    login.login("standard_user", "secret_sauce")

    expect(page).to_have_url(re.compile(r".*/inventory\.html"))
    expect(page.locator(".title")).to_have_text("Products")


def test_login_usuario_bloqueado(page: Page):
    login = LoginPage(page)
    login.open()
    login.login("locked_out_user", "secret_sauce")

    expect(login.error_message).to_contain_text("locked out")


def test_login_password_incorrecta(page: Page):
    login = LoginPage(page)
    login.open()
    login.login("standard_user", "clave_incorrecta")

    expect(login.error_message).to_contain_text("do not match")