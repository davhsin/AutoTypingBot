from selenium import webdriver   
from selenium.webdriver.chrome.options import Options # 用來引入 Chrome 瀏覽器的選項設定（Options）
from selenium.webdriver.common.by import By # 提供了不同的方法或函式，用於定位網頁元素。
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
import time

# 初始化
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
browser = webdriver.Chrome(options=chrome_options)
# browser = webdriver.Firefox()
browser.get('https://monkeytype.com/')

# 等到出現就按下那該死的cookie
reject_cookie = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//*[@class='button rejectAll']")
        )
).click()

# 改成字數模式
word_mode = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//div[@class='textButton' and @mode='words']")
        )
).click()

for i in range(0, 51):
    # 找到元素
    element = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//div[@class='word active']")
            )
    )
    # 輸入文字
    input_element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@id='wordsInput']")
        )
    ).send_keys(element.text + ' ') # here is a bug :(
        

