from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


def test_opencart_main(browser, base_url):
    browser.get(base_url)
    wait = WebDriverWait(browser, 10)
    macbook = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()='MacBook']")))
    iphone = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()='iPhone']")))
    apple_cinema = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()='Apple Cinema 30\"']")))
    cannon = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()='Canon EOS 5D']")))
    main_window = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(@href, 'product_id=49')]")))


def test_product_card(browser, base_url):
    browser.get(base_url + '/en-gb/product/macbook')
    wait = WebDriverWait(browser, 10)
    title = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='col-sm']/h1[text()='MacBook']")))
    price = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='col-sm']//span[@class='price-new']")))
    quantity_input = wait.until(EC.visibility_of_element_located((By.ID, "input-quantity")))
    default_quantity = int(quantity_input.get_attribute("value"))
    assert default_quantity == 1, f"Expected '1', but got {default_quantity}"
    button = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@id='button-cart']")))
    button_text = button.text.strip()
    assert button_text == "Add to Cart", f"Expected 'Add to Cart' but got '{button_text}'"


def test_administration(browser, base_url):
    browser.get(base_url + '/administration/')
    wait = WebDriverWait(browser, 10)
    title = wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//div[@class='card-header' and contains(text(), 'Please enter your login details.')]")))
    username = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='input-username']")))
    assert username.get_attribute("placeholder") == "Username"
    password = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='input-password']")))
    assert password.get_attribute("placeholder") == "Password"
    login_button = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//button[@type='submit' and contains(text(), 'Login')]")))


def test_catalog_desktops(browser, base_url):
    browser.get(base_url + '/en-gb/catalog/desktops')
    wait = WebDriverWait(browser, 10)
    name_of_product = wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//div[contains(@class, 'product-thumb')]//div[contains(@class, 'description')]")))
    any_product = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'product-thumb')]")))
    add_to_cart_button = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                                      "//div[contains(@class, 'product-thumb')]//button[@type='submit' and contains(@formaction, 'route=checkout/cart.add')]")))
    add_to_wish_list_button = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                                           "//div[contains(@class, 'product-thumb')]//button[@type='submit' and contains(@formaction, 'route=account/wishlist.add')]")))
    price = wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//div[contains(@class, 'product-thumb')]//div[contains(@class, 'price')]")))


def test_register_page(browser, base_url):
    browser.get(base_url + '/index.php?route=account/register')
    wait = WebDriverWait(browser, 10)
    personal_details_block = wait.until(EC.visibility_of_element_located((By.XPATH, "//fieldset[@id='account']")))
    first_name = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='input-firstname']")))
    password = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='input-password']")))
    privacy = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//input[@name='agree' and @class='form-check-input']")))


def test_administration_login(browser, base_url):
    browser.get(base_url + '/administration/')
    wait = WebDriverWait(browser, 10)
    username = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='input-username']")))
    password = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='input-password']")))
    username.send_keys("user")
    password.send_keys("bitnami")
    login_button = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//button[@type='submit' and contains(text(), 'Login')]")))
    login_button.click()
    wait.until(EC.url_contains("dashboard"))
    assert "dashboard" in browser.current_url.lower(), "Login failed or did not redirect to dashboard"
    print("Login test passed successfully!")


def test_add_item_to_basket(browser, base_url):
    browser.get(base_url)
    wait = WebDriverWait(browser, 15, poll_frequency=0.1)
    macbook_add_to_cart_button = wait.until(
        EC.element_to_be_clickable((By.XPATH,
                                    "//div[contains(@class, 'product-thumb') and .//a[contains(@href, 'macbook')]]//form//button[.//i[contains(@class, 'fa-shopping-cart')]]"))
        )
    browser.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",macbook_add_to_cart_button)
    browser.execute_script("arguments[0].click();", macbook_add_to_cart_button)
    alert = wait.until(
            EC.visibility_of_element_located((By.XPATH,
                                              "//div[contains(@class, 'alert-success') and contains(., 'Success: You have added')]"))
        )

def test_change_currency(browser, base_url):
    browser.get(base_url)
    wait = WebDriverWait(browser, 10)
    currency_button = wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//form[@id='form-currency']//a[contains(@class, 'dropdown-toggle')]")))
    currency_button.click()
    euro = wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//form[@id='form-currency']//ul[contains(@class, 'dropdown-menu')]//a[@href='EUR']")))
    euro.click()
    price_check = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                               "//div[contains(@class, 'product-thumb')]//h4/a[text()='MacBook']/../../..//div[@class='price']//span[contains(@class, 'price-new')]")))
    price = price_check.text
    try:
        if '€' in price:
            print("Price is in EURO: ", price)
        else:
            print("Price is NOT in USD: ", price)
    except NoSuchElementException:
        print("Price element not found!")


def test_change_currency_in_catalog(browser, base_url):
    browser.get(base_url)
    wait = WebDriverWait(browser, 10)
    wait.until(EC.presence_of_element_located((By.ID, "logo")))

    currency_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//form[@id='form-currency']//a[contains(@class, 'dropdown-toggle')]")))
    currency_button.click()
    euro = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//form[@id='form-currency']//ul[contains(@class, 'dropdown-menu')]//a[@href='EUR']")))
    euro.click()
    wait.until(EC.presence_of_element_located((By.ID, "content")))
    wait.until(EC.element_to_be_clickable((
        By.XPATH,
        '//a[@class="nav-link dropdown-toggle" and text()="Desktops"]'
    ))).click()
    wait.until(EC.element_to_be_clickable((
        By.XPATH,
        '//a[@class="see-all" and text()="Show All Desktops"]'
    ))).click()
    wait.until(EC.url_contains("/en-gb/catalog/desktops"))
    price = wait.until(
        EC.visibility_of_element_located((By.XPATH, '//div[@id="product-list"]/div[1]//div[@class="price"]')))
    price = price.text
    if '€' in price:
        print("Price is in EURO: ", price)
    else:
        print("Price is NOT in USD: ", price)
