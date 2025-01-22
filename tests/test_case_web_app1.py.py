def test_web_app1_case1(driver):
    from pages.base_page import BasePage

    page = BasePage(driver)
    driver.get("https://example.com")
    assert "example" in driver.title
