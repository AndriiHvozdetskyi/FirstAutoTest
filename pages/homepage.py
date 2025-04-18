from selenium.webdriver.common.by import By

class HomePage:

    def __init__(self, driver):
        self.driver = driver


    def open(self):
        self.driver.get('https://demoblaze.com/')

    def click_galaxy_s6(self):
        galaxy_a6 = self.driver.find_element(By.XPATH, value='//a[text()="Samsung galaxy s6"]')
        galaxy_a6.click()

    def click_monitor(self):
        monitors = self.driver.find_element(By.CSS_SELECTOR, value='''[onclick="byCat('monitor')"]''')
        monitors.click()

    def check_products_count(self, count):
        monitors = self.driver.find_elements(By.CLASS_NAME, value='card')
        assert len(monitors) == count