from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Test_NonMemberReservation:
    def test_Reservation_NonMember(self):
        driver = webdriver.Chrome()
        driver.get("https://hotel.testplanisphere.dev/ja/plans.html")
        driver.find_element(By.LINK_TEXT, "このプランで予約").click()
        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(1))
        driver.find_element(By.NAME, "date").click()
