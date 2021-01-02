from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import time

#This example requires Selenium WebDriver 3.13 or newer
url = input("Enter product url: ")
with webdriver.Chrome('chromedriver') as driver:
  wait = WebDriverWait(driver, 10)
  # city scrapping
  driver.get("https://shop.lululemon.com/stores/all-lululemon-stores")
  wait.until(presence_of_element_located((By.CLASS_NAME,"state-section-container")))
  time.sleep(5)
  driver.find_element_by_css_selector("#filter-all-store-locations").click()
  driver.find_element_by_css_selector("#filter-all-store-locations > option:nth-child(1)").click()
  time.sleep(5)
  locations = driver.find_elements_by_class_name("lll-font-body-secondary")
  cities = set()
  for store in locations:
    cities.add((store.text).split(":")[0])

  # #product
  driver.get(url)
  wait.until(presence_of_element_located((By.CLASS_NAME, "purchase-method__bopis__link")))
  driver.find_element(By.CLASS_NAME, "purchase-method__bopis__link").click()
  wait.until(presence_of_element_located((By.CLASS_NAME, "select-menu__selected")))
  store_names = set()

  # wrap in city loop
  for city in cities:
    input_bar = driver.find_element_by_class_name("search-bar__input")
    input_bar.send_keys(Keys.CONTROL + "a")
    input_bar.send_keys(Keys.DELETE)
    input_bar.send_keys(city)
    driver.find_element_by_class_name("search-bar__search-button").click()
    time.sleep(5)

    try:
      # nothing to see here
      err = driver.find_element_by_class_name("error-message")
      continue
    except:
      print("Stores available")

    try:
      bopis_list = driver.find_element_by_class_name("store-list")
      bopis_stores = bopis_list.find_elements_by_class_name("store-list__item")
      for store in bopis_stores:
        store_names.add(store.find_element_by_class_name("radio-btn__label").text)
    except:
      print("No BOPIS stores in ", city)

    try:
      in_person_list = driver.find_element_by_class_name("store-list--unavailable")
      in_person_stores = in_person_list.find_elements_by_class_name("store-list__item")
      for store in in_person_stores:
        store_names.add(store.find_element_by_class_name("store-list__store-name").text)
    except:
      print("No in-person stores in ", city)

  if (len(store_names) != 0):
    print(store_names)
  else:
    print("No in-store stock")