import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SystemTest(unittest.TestCase):
    def setUp(self):
        # Inisialisasi WebDriver
        self.driver = webdriver.Chrome()

    def tearDown(self):
        # Tambahkan penundaan waktu sebelum menutup WebDriver
        time.sleep(5)

        # Menutup WebDriver
        self.driver.quit()

    def login(self, username, password):

        time.sleep(2)
        email_input = self.driver.find_element(By.ID, "email")
        password_input = self.driver.find_element(By.ID, "password")\
        
        email_input.send_keys(username)
        password_input.send_keys(password)

        time.sleep(2)
        button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        button.click()

        # Tunggu maksimal 10 detik hingga alert muncul
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())

        # Menangani alert dengan mengonfirmasi (klik OK)
        alert = self.driver.switch_to.alert
        alert.accept()

    def test_login(self):
        self.driver.get("https://trensentimen.my.id/")
        time.sleep(2)
        self.login("erdito@gmail.com", "fghjkliow")


if __name__ == "__main__":
    unittest.main()