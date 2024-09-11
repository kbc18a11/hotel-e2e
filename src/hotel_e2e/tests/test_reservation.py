from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from datetime import datetime


class Test_NonMemberReservation:
    def test_Reservation_NonMember(self):
        driver = webdriver.Chrome()
        driver.get("https://hotel.testplanisphere.dev/ja/plans.html")
        driver.find_element(By.LINK_TEXT, "このプランで予約").click()
        driver.switch_to.window(driver.window_handles[1])
        element = WebDriverWait(driver, timeout=10).until(lambda d: EC.element_to_be_clickable((By.NAME, "date")))(driver)
        element.click()
        element = WebDriverWait(driver, timeout=10).until(
            lambda d: EC.element_to_be_clickable((By.CLASS_NAME, "ui-datepicker-next"))
        )(driver)
        element.click()
        element = WebDriverWait(driver, timeout=10).until(lambda d: EC.element_to_be_clickable((By.LINK_TEXT, "1")))(driver)
        element.click()
        term_btn = WebDriverWait(driver, timeout=10).until(lambda d: EC.presence_of_element_located((By.NAME, "term")))(
            driver
        )
        term_btn.clear()
        term_btn.send_keys("7")
        head_count_btn = WebDriverWait(driver, timeout=10).until(
            lambda d: EC.presence_of_element_located((By.NAME, "head-count"))
        )(driver)
        head_count_btn.clear()
        head_count_btn.send_keys("2")
        driver.find_element(By.NAME, "breakfast").click()
        driver.find_element(By.NAME, "early-check-in").click()
        driver.find_element(By.NAME, "sightseeing").click()
        driver.find_element(By.NAME, "username").send_keys("テスト太郎")
        contact = Select(
            WebDriverWait(driver, timeout=10).until(lambda d: EC.presence_of_element_located((By.NAME, "contact")))(driver)
        )
        contact.select_by_visible_text("メールでのご連絡")
        WebDriverWait(driver, timeout=10).until(lambda d: EC.presence_of_element_located((By.NAME, "email")))(
            driver
        ).send_keys("hoge@example.com")
        WebDriverWait(driver, timeout=10).until(lambda d: EC.presence_of_element_located((By.NAME, "comment")))(
            driver
        ).send_keys("テスト")
        driver.find_element(By.XPATH, "//button[@data-test='submit-button']").click()
        assert "合計 123,000円（税込み）" == driver.find_element(By.ID, "total-bill").text
        today = datetime.now()
        year = today.year if today.month < 12 else today.year + 1
        month = today.month + 1 if today.month < 12 else 1
        assert f"{year}年{month}月1日 〜 {year}年{month}月8日 7泊" == driver.find_element(By.ID, "term").text
        assert "2名様" == driver.find_element(By.ID, "head-count").text
        plans = [plan.text for plan in driver.find_element(By.ID, "plans").find_elements(By.TAG_NAME, "li")]
        assert plans == ["朝食バイキング", "昼からチェックインプラン", "お得な観光プラン"]
        assert "テスト太郎様" == driver.find_element(By.ID, "username").text
        assert "メール：hoge@example.com" == driver.find_element(By.ID, "contact").text
        assert "テスト" == driver.find_element(By.ID, "comment").text
        driver.find_element(By.XPATH, "//button[@data-toggle='modal']").click()
        assert (
            "予約を完了しました"
            == WebDriverWait(driver, timeout=10)
            .until(lambda d: EC.presence_of_element_located((By.CLASS_NAME, "modal-title")))(driver)
            .text
        )
