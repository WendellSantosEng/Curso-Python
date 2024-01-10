from pathlib import Path
import time
from selenium import webdriver

def open_browser_(options: str) -> webdriver.Chrome:
    ROOT_FOLDER = Path(__file__).parent

    chrome_options = webdriver.ChromeOptions()

    if options is not None:
        for option in options:
            chrome_options.add_argument(option) 

    browser = webdriver.Chrome(
        options = chrome_options,
    )

    return browser

if(__name__ == "__main__"):

    # Example
    options = ("--disable_gpu", "--no-sandbox",)

    open_browser_()
    
    chrome_browser.get("https://www.google.com.br/")
    time.sleep(30)