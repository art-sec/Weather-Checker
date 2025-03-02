from selenium import webdriver
import time

CITY = 'London'

browser = webdriver.Chrome()
SITE_URL = "https://openweathermap.org"

browser.get(SITE_URL)
time.sleep(3)

search = browser.find_element('xpath', '//*[@id="weather-widget"]/div[2]/div/div/div[2]/div[1]/div/input//*[@id="weather-widget"]/div[2]/div/div/div[2]/div[1]/div/input')
search_confirm_button = browser.find_element('xpath', '//*[@id="weather-widget"]/div[2]/div/div/div[2]/div[1]/button//*[@id="weather-widget"]/div[2]/div/div/div[2]/div[1]/button')
search_confirm_value = browser.find_element('xpath', '//*[@id="weather-widget"]/div[2]/div/div/div[2]/div[1]/div/ul/li[1]')

search.send_keys(CITY)
time.sleep(1)
search_confirm_button.click
time.sleep(1)
search_confirm_value.click
time.sleep(2)