from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time


def main():
    
    url_input = input("Enter Url: ")
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("start--maximized")
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extentions")
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    driver.get(url_input)
    time.sleep(5)
    
    try:
        title = driver.find_element(By.TAG_NAME, "h1").text
    except:
        title = "Title not found"
        
    try: 
        price = driver.find_element(By.CLASS_NAME, "price-current").text
    except:
        price = "Price not found"
        
    try:
        stock = driver.find_element(By.CLASS_NAME, "flags-body has-icon-left fa-exclamation-triangle").text
    except:
        stock = "In Stock"

    with open("output.txt", "w", encoding="utf-8") as file:
        file.write(f"Title: {title}\nPrice: {price}\nStock: {stock}")
    
    driver.quit()

    
if __name__ == "__main__": 
    main()