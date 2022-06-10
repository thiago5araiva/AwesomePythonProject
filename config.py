from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


class Config:
    def __init__(self):
        options = webdriver.ChromeOptions()
        # options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=options)

    def get_html(self, url):
        self.driver.get(url)
        html = self.driver.find_element(By.TAG_NAME, 'body').get_attribute("innerHTML")
        soup = BeautifulSoup(html, 'html.parser')
        return soup
