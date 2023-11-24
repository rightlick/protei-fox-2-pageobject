from AuthPage import Authorization


def test_auth(browser):

    protei_auth_page = Authorization(browser)
    protei_auth_page.go_to_site()
    protei_auth_page.enter_email("test@protei.ru")
    protei_auth_page.enter_password("test")
    protei_auth_page.click_on_the_authorization_button()
    element = protei_auth_page.check_main_page()
    assert element.get_attribute("class") == "uk-card-title"
    assert element.text == "Добро пожаловать!"
