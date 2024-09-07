from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class Test_NonMemberReservation:
    def test_Reservation_NonMember(self):
        driver = webdriver.Chrome()
        driver.get("https://hotel.testplanisphere.dev/ja/plans.html")
        driver.find_element(By.LINK_TEXT, "このプランで予約").click()
        driver.switch_to.window(driver.window_handles[1])
        driver.find_element(By.NAME, "date").click()
        driver.find_element(By.CLASS_NAME, "ui-datepicker-next").click()
        driver.find_element(By.LINK_TEXT, "1").click()
        term_btn = driver.find_element(By.NAME, "term")
        term_btn.clear()
        term_btn.send_keys("7")
        head_count_btn = driver.find_element(By.NAME, "head-count")
        head_count_btn.clear()
        head_count_btn.send_keys("2")
        driver.find_element(By.NAME, "breakfast").click()
        driver.find_element(By.NAME, "early-check-in").click()
        driver.find_element(By.NAME, "sightseeing").click()
        # driver.find_element(By.NAME, "username").send_keys("テスト太郎")
        print(driver.save_screenshot("src/hotel_e2e/tests/img/test.png"))
        assert "123,000円" == driver.find_element(By.NAME, "total-bill").text
