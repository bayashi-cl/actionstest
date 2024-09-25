from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options


def test_google() -> None:
    options = Options()
    options.add_argument("--headless=new")

    with Chrome(options) as driver:
        driver.get("https://www.google.com")
        assert driver.title == "Google"
