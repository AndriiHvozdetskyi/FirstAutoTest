import time
from pages.homepage import HomePage
from pages.product import ProductPage

def test_open_s6(driver):
    homepage = HomePage(driver)
    homepage.open()
    homepage.click_galaxy_s6()
    product_page = ProductPage(driver)
    product_page.check_title_is("Samsung galaxy s6")

def test_open_monitors(driver):
    homepage = HomePage(driver)
    homepage.open()
    homepage.click_monitor()
    time.sleep(2)
    homepage.check_products_count(2)

# def test_open_s7(driver):
#     driver.get('https://demoblaze.com/')
#     galaxy_s7 = driver.find_element(By.XPATH, value='//a[text()="Samsung galaxy s7"]')
#     galaxy_s7.click()
#     title = driver.find_element(By.CSS_SELECTOR, value="h2")
#     assert title.text == "Samsung galaxy s7"