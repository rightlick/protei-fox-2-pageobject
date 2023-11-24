from AuthPage import Authorization


def test(browser):

    protei_auth_page = Authorization(browser)
    protei_auth_page.go_to_site()
    protei_auth_page.enter_email("test@protei.ru")
    protei_auth_page.enter_password("test")
    protei_auth_page.click_on_the_authorization_button()