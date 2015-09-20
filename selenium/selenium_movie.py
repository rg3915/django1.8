# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

customer = webdriver.Firefox()
customer.get('http://localhost:8000/movie/add/')
time.sleep(2)

search = customer.find_element_by_id('id_movie')
search.send_keys('Star Wars 7')
time.sleep(2)

search = customer.find_element_by_id('id_category')
search.send_keys('aventura')
time.sleep(2)

search = customer.find_element_by_id('id_distributor')
search.send_keys('Walt Disney Pictures')
time.sleep(2)

search = customer.find_element_by_id('id_raised')
search.send_keys('2,5')
time.sleep(2)

search = customer.find_element_by_id('id_release')
search.send_keys('17/12/2015')

button = customer.find_element_by_id('id_submit')
# button.click()
