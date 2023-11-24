from time import sleep

from AuthPage import Authorization


def auth(browser):
    protei_auth_page = Authorization(browser)
    protei_auth_page.go_to_site()
    protei_auth_page.enter_email("test@protei.ru")
    protei_auth_page.enter_password("test")
    protei_main_page = protei_auth_page.click_on_the_authorization_button(browser)
    return protei_main_page


def test_auth(browser):
    protei_main_page = auth(browser)
    element = protei_main_page.check_main_page()
    assert element.get_attribute("class") == "uk-card-title"
    assert element.text == "Добро пожаловать!"


def test_navigation_to_variants(browser):
    protei_main_page = auth(browser)
    protei_variants_page = protei_main_page.click_on_the_variants_tab(browser)
    element = protei_variants_page.check_variants_page()
    assert element.get_attribute("class") == "uk-card-title"
    assert element.text == "НТЦ ПРОТЕЙ"


def test_navigation_to_users(browser):
    protei_main_page = auth(browser)
    protei_users_page = protei_main_page.click_on_the_users_tab(browser)
    element = protei_users_page.check_users_page()
    assert element.get_attribute("class") == "uk-panel-scrollable"


def test_navigation_to_users_dropdown(browser):
    protei_main_page = auth(browser)
    protei_users_page = protei_main_page.click_on_the_users_table_dropdown(browser)
    element = protei_users_page.check_users_page()
    assert element.get_attribute("class") == "uk-panel-scrollable"


def test_navigation_to_add_user(browser):
    protei_main_page = auth(browser)
    protei_add_user_page = protei_main_page.click_on_the_add_user_dropdown(browser)
    element = protei_add_user_page.check_add_user_page()
    assert element.get_attribute("class") == "uk-legend"
    assert element.text == "Добавление пользователя"


def test_pairwise_1(browser):
    protei_main_page = auth(browser)
    protei_add_user_page = protei_main_page.click_on_the_add_user_dropdown(browser)
    protei_add_user_page.enter_email("example@mail.com")
    protei_add_user_page.enter_password("qwerty12345")
    protei_add_user_page.enter_name("Иванушка")

    # 0 - male  |   1 - female
    protei_add_user_page.enter_sex(0)

    # 1 or 2 for radio button
    protei_add_user_page.enter_radio_button(1)

    protei_add_user_page.enter_checkbox(1)

    protei_add_user_page.click_on_the_add_button()
    modal = protei_add_user_page.check_modal_success()
    assert modal.get_attribute("class") == "uk-modal-dialog"

    button = protei_add_user_page.click_modal_button()
    assert button.get_attribute("class") == "uk-button uk-button-primary uk-modal-close"
    assert button.text == "OK"


def test_pairwise_2(browser):
    protei_main_page = auth(browser)
    protei_add_user_page = protei_main_page.click_on_the_add_user_dropdown(browser)
    protei_add_user_page.enter_email("EXAmPlE@YAndEx.Ru")
    protei_add_user_page.enter_password("f#db96l%4~boA@")
    protei_add_user_page.enter_name("Екатерина 2 Великая")

    # 0 - male  |   1 - female
    protei_add_user_page.enter_sex(1)

    # 1 or 2 for radio button
    protei_add_user_page.enter_radio_button(2)

    protei_add_user_page.enter_checkbox(2)

    protei_add_user_page.click_on_the_add_button()
    modal = protei_add_user_page.check_modal_success()
    assert modal.get_attribute("class") == "uk-modal-dialog"

    button = protei_add_user_page.click_modal_button()
    assert button.get_attribute("class") == "uk-button uk-button-primary uk-modal-close"
    assert button.text == "OK"


def test_pairwise_3(browser):
    protei_main_page = auth(browser)
    protei_add_user_page = protei_main_page.click_on_the_add_user_dropdown(browser)
    protei_add_user_page.enter_email("8888@88.com")
    protei_add_user_page.enter_password("надёжныйпароль")
    protei_add_user_page.enter_name("Владимир Владимирович Путин")

    # 0 - male  |   1 - female
    protei_add_user_page.enter_sex(0)

    # 1 or 2 for radio button
    protei_add_user_page.enter_radio_button(2)

    protei_add_user_page.enter_checkbox(3)

    protei_add_user_page.click_on_the_add_button()
    modal = protei_add_user_page.check_modal_success()
    assert modal.get_attribute("class") == "uk-modal-dialog"

    button = protei_add_user_page.click_modal_button()
    assert button.get_attribute("class") == "uk-button uk-button-primary uk-modal-close"
    assert button.text == "OK"


def test_pairwise_4(browser):
    protei_main_page = auth(browser)
    protei_add_user_page = protei_main_page.click_on_the_add_user_dropdown(browser)
    protei_add_user_page.enter_email("москва@москва.рф")
    protei_add_user_page.enter_password("港口で難船")
    protei_add_user_page.enter_name("اردشیر")

    # 0 - male  |   1 - female
    protei_add_user_page.enter_sex(1)

    # 1 or 2 for radio button
    protei_add_user_page.enter_radio_button(2)

    protei_add_user_page.enter_checkbox(1)
    protei_add_user_page.enter_checkbox(2)

    protei_add_user_page.click_on_the_add_button()
    modal = protei_add_user_page.check_modal_success()
    assert modal.get_attribute("class") == "uk-modal-dialog"

    button = protei_add_user_page.click_modal_button()
    assert button.get_attribute("class") == "uk-button uk-button-primary uk-modal-close"
    assert button.text == "OK"


def test_pairwise_5(browser):
    protei_main_page = auth(browser)
    protei_add_user_page = protei_main_page.click_on_the_add_user_dropdown(browser)
    protei_add_user_page.enter_email("admin@example")
    protei_add_user_page.enter_password("123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345")
    protei_add_user_page.enter_name("Q")

    # 0 - male  |   1 - female
    protei_add_user_page.enter_sex(0)

    # 1 or 2 for radio button
    protei_add_user_page.enter_radio_button(2)

    protei_add_user_page.enter_checkbox(1)
    protei_add_user_page.enter_checkbox(3)

    protei_add_user_page.click_on_the_add_button()
    modal = protei_add_user_page.check_modal_success()
    assert modal.get_attribute("class") == "uk-modal-dialog"

    button = protei_add_user_page.click_modal_button()
    assert button.get_attribute("class") == "uk-button uk-button-primary uk-modal-close"
    assert button.text == "OK"


def test_pairwise_6(browser):
    protei_main_page = auth(browser)
    protei_add_user_page = protei_main_page.click_on_the_add_user_dropdown(browser)
    protei_add_user_page.enter_email("postmaster@[123.123.123.123]")
    protei_add_user_page.enter_password("п")
    protei_add_user_page.enter_name("123456789012345678901234567890")

    # 0 - male  |   1 - female
    protei_add_user_page.enter_sex(1)

    # 1 or 2 for radio button
    protei_add_user_page.enter_radio_button(1)

    protei_add_user_page.enter_checkbox(2)
    protei_add_user_page.enter_checkbox(3)

    protei_add_user_page.click_on_the_add_button()
    modal = protei_add_user_page.check_modal_success()
    assert modal.get_attribute("class") == "uk-modal-dialog"

    button = protei_add_user_page.click_modal_button()
    assert button.get_attribute("class") == "uk-button uk-button-primary uk-modal-close"
    assert button.text == "OK"


def test_pairwise_7(browser):
    protei_main_page = auth(browser)
    protei_add_user_page = protei_main_page.click_on_the_add_user_dropdown(browser)
    protei_add_user_page.enter_email("emailaddresss@example.com")
    protei_add_user_page.enter_password("latineca")
    protei_add_user_page.enter_name("あんな")

    # 0 - male  |   1 - female
    protei_add_user_page.enter_sex(1)

    # 1 or 2 for radio button
    protei_add_user_page.enter_radio_button(2)

    protei_add_user_page.enter_checkbox(1)
    protei_add_user_page.enter_checkbox(2)
    protei_add_user_page.enter_checkbox(3)

    protei_add_user_page.click_on_the_add_button()
    modal = protei_add_user_page.check_modal_success()
    assert modal.get_attribute("class") == "uk-modal-dialog"

    button = protei_add_user_page.click_modal_button()
    assert button.get_attribute("class") == "uk-button uk-button-primary uk-modal-close"
    assert button.text == "OK"


def test_pairwise_8(browser):
    protei_main_page = auth(browser)
    protei_add_user_page = protei_main_page.click_on_the_add_user_dropdown(browser)
    protei_add_user_page.enter_email("ivanov322gamer1@mail.ru")
    protei_add_user_page.enter_password("СВЕТЛАНА")
    protei_add_user_page.enter_name("СВЕТЛАНА")

    # 0 - male  |   1 - female
    protei_add_user_page.enter_sex(1)

    # 1 or 2 for radio button
    protei_add_user_page.enter_radio_button(2)

    protei_add_user_page.click_on_the_add_button()
    modal = protei_add_user_page.check_modal_success()
    assert modal.get_attribute("class") == "uk-modal-dialog"

    button = protei_add_user_page.click_modal_button()
    assert button.get_attribute("class") == "uk-button uk-button-primary uk-modal-close"
    assert button.text == "OK"


def test_pairwise_9_negative_empty_email(browser):
    protei_main_page = auth(browser)
    protei_add_user_page = protei_main_page.click_on_the_add_user_dropdown(browser)
    protei_add_user_page.enter_email("")
    protei_add_user_page.enter_password("7d F5v")
    protei_add_user_page.enter_name("Tom Marvolo Riddle")

    # 0 - male  |   1 - female
    protei_add_user_page.enter_sex(0)

    # 1 or 2 for radio button
    protei_add_user_page.enter_radio_button(1)

    protei_add_user_page.click_on_the_add_button()

    alert = protei_add_user_page.check_alert_fail_email()
    assert alert.get_attribute("class") == "uk-alert uk-alert-danger"


def test_pairwise_10_negative_empty_password(browser):
    protei_main_page = auth(browser)
    protei_add_user_page = protei_main_page.click_on_the_add_user_dropdown(browser)
    protei_add_user_page.enter_email("name@and.subdomains.example.com")
    protei_add_user_page.enter_password("")
    protei_add_user_page.enter_name("Иван")

    # 0 - male  |   1 - female
    protei_add_user_page.enter_sex(1)

    # 1 or 2 for radio button
    protei_add_user_page.enter_radio_button(2)

    protei_add_user_page.enter_checkbox(1)

    protei_add_user_page.click_on_the_add_button()

    alert = protei_add_user_page.check_alert_fail_password()
    assert alert.get_attribute("class") == "uk-alert uk-alert-danger"


def test_pairwise_11_negative_empty_name(browser):
    protei_main_page = auth(browser)
    protei_add_user_page = protei_main_page.click_on_the_add_user_dropdown(browser)
    protei_add_user_page.enter_email("e@9.is")
    protei_add_user_page.enter_password("QwErTy")
    protei_add_user_page.enter_name("")

    # 0 - male  |   1 - female
    protei_add_user_page.enter_sex(0)

    # 1 or 2 for radio button
    protei_add_user_page.enter_radio_button(2)

    protei_add_user_page.enter_checkbox(2)

    protei_add_user_page.click_on_the_add_button()

    alert = protei_add_user_page.check_alert_fail_name()
    assert alert.get_attribute("class") == "uk-alert uk-alert-danger"


def test_pairwise_12_negative_long_password(browser):
    protei_main_page = auth(browser)
    protei_add_user_page = protei_main_page.click_on_the_add_user_dropdown(browser)
    protei_add_user_page.enter_email("e.x.a.m.p.l.e@sub_domain.example.com")
    protei_add_user_page.enter_password("12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234")
    protei_add_user_page.enter_name("Ра")

    # 0 - male  |   1 - female
    protei_add_user_page.enter_sex(1)

    # 1 or 2 for radio button
    protei_add_user_page.enter_radio_button(2)

    protei_add_user_page.enter_checkbox(3)

    protei_add_user_page.click_on_the_add_button()

    modal = protei_add_user_page.check_modal_fail()
    assert modal.is_displayed()
    assert modal.get_attribute("class") == "uk-modal-dialog"
    button = protei_add_user_page.click_modal_button()
    assert button.get_attribute("class") == "uk-button uk-button-primary uk-modal-close"
    assert button.text == "OK"


def test_pairwise_13_negative_long_email(browser):
    protei_main_page = auth(browser)
    protei_add_user_page = protei_main_page.click_on_the_add_user_dropdown(browser)
    protei_add_user_page.enter_email("long.email-addresss@example.com")
    protei_add_user_page.enter_password("حرف حرف میاره")
    protei_add_user_page.enter_name("Aрtёm")

    # 0 - male  |   1 - female
    protei_add_user_page.enter_sex(0)

    # 1 or 2 for radio button
    protei_add_user_page.enter_radio_button(1)

    protei_add_user_page.enter_checkbox(1)
    protei_add_user_page.enter_checkbox(2)

    protei_add_user_page.click_on_the_add_button()

    alert = protei_add_user_page.check_alert_fail_email()
    assert alert.get_attribute("class") == "uk-alert uk-alert-danger"


def test_pairwise_14_negative_long_name(browser):
    protei_main_page = auth(browser)
    protei_add_user_page = protei_main_page.click_on_the_add_user_dropdown(browser)
    protei_add_user_page.enter_email("abc@example.com")
    protei_add_user_page.enter_password("ABCDE")
    protei_add_user_page.enter_name("1234567890123456789012345678901")

    # 0 - male  |   1 - female
    protei_add_user_page.enter_sex(1)

    # 1 or 2 for radio button
    protei_add_user_page.enter_radio_button(1)

    protei_add_user_page.enter_checkbox(1)
    protei_add_user_page.enter_checkbox(3)

    protei_add_user_page.click_on_the_add_button()

    modal = protei_add_user_page.check_modal_fail()
    assert modal.is_displayed()
    assert modal.get_attribute("class") == "uk-modal-dialog"
    button = protei_add_user_page.click_modal_button()
    assert button.get_attribute("class") == "uk-button uk-button-primary uk-modal-close"
    assert button.text == "OK"


def test_pairwise_15_negative_invalid_email(browser):
    protei_main_page = auth(browser)
    protei_add_user_page = protei_main_page.click_on_the_add_user_dropdown(browser)
    protei_add_user_page.enter_email("elki-palki@best-server-ever.com")
    protei_add_user_page.enter_password("па")
    protei_add_user_page.enter_name("12345678901234567890123456789")

    # 0 - male  |   1 - female
    protei_add_user_page.enter_sex(1)

    # 1 or 2 for radio button
    protei_add_user_page.enter_radio_button(2)

    protei_add_user_page.enter_checkbox(2)
    protei_add_user_page.enter_checkbox(3)

    protei_add_user_page.click_on_the_add_button()

    alert = protei_add_user_page.check_alert_fail_email()
    assert alert.get_attribute("class") == "uk-alert uk-alert-danger"


def test_pairwise_16_negative_invalid_email_without_at(browser):
    protei_main_page = auth(browser)
    protei_add_user_page = protei_main_page.click_on_the_add_user_dropdown(browser)
    protei_add_user_page.enter_email("example")
    protei_add_user_page.enter_password("P@ssword")
    protei_add_user_page.enter_name("S1mple_fan")

    # 0 - male  |   1 - female
    protei_add_user_page.enter_sex(1)

    # 1 or 2 for radio button
    protei_add_user_page.enter_radio_button(2)

    protei_add_user_page.enter_checkbox(1)
    protei_add_user_page.enter_checkbox(2)
    protei_add_user_page.enter_checkbox(3)

    protei_add_user_page.click_on_the_add_button()

    alert = protei_add_user_page.check_alert_fail_email()
    assert alert.get_attribute("class") == "uk-alert uk-alert-danger"
