from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")

# Assuming chromedriver is in your PATH
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.wikipedia.org/")
print(driver.title)
driver.quit()
