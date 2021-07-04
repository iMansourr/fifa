import sys

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyotp
from selenium.common.exceptions import (NoSuchElementException,TimeoutException, WebDriverException)
from selenium.webdriver.support import ui
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
# import fifa
import requests
import random
import pickle
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select

# Initiate the driver
driver = webdriver.Chrome(ChromeDriverManager().install())

# Open the Website
driver.get('https://www.ea.com/fifa/ultimate-team/web-app/')

loginBtn = WebDriverWait(driver, 10).until(
EC.element_to_be_clickable((By.XPATH, '//*[@id="Login"]/div/div/button[1]')))
loginBtn.click()

web_app_email = "meza-jeff7171@mail.ru"
web_app_password = "zTHIC3B5t"
driver.find_element_by_name("email").send_keys(web_app_email)
driver.find_element_by_name("password").send_keys(web_app_password)
driver.find_element_by_xpath('//*[@id="btnLogin"]/span').click()
driver.find_element_by_xpath('//*[@id="panel-tfa"]/div/div/div/div[3]/p/span/input').click()
driver.find_element_by_xpath('//*[@id="btnSendCode"]').click()

totp = pyotp.TOTP('3kn6wp3h42akdqd3')
totp.now()
driver.find_element_by_name("oneTimeCode").send_keys(totp.now())
driver.find_element_by_xpath('//*[@id="btnSubmit"]/span/span').click()

ut_nav = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH,'/html/body/main/section/nav')))

def ut_shield(): # a function to hide the ut-click-shield so we can access the other elements. ( use this function whenever you get an error saying item is not clickable )
        WebDriverWait(driver, 30).until(EC.invisibility_of_element_located((By.CLASS_NAME, 'ut-click-shield')))

ut_shield()
# to access the transfer market button
transfer_market_btn = WebDriverWait(driver, 30).until(
EC.element_to_be_clickable((By.XPATH, '/html/body/main/section/nav/button[3]')))
transfer_market_btn.click()

ut_shield()
# to access the transfer market search element
# transfer_market_search_btn = driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div/div[2]')
# transfer_market_search_btn.click()
#
#
# driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[1]/div[2]/div/div').click()
# driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[1]/div[2]/div/ul/li[4]').click()
# driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[6]/div[2]/input').send_keys('2000')
# driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div[2]/div/div[2]/button[2]').click()
#
# results = WebDriverWait(driver, 30).until(EC.visibility_of_all_elements_located((By.XPATH, '//li[contains(@class,"listFUTItem")]')))
#
#
# buy_now_prices = WebDriverWait(driver, 30).until(EC.visibility_of_all_elements_located((By.XPATH, '/html/body/main/section/section/div[2]/div/div/section[1]/div/ul/li/div/div[2]/div[3]/span[2]')))
# lowest_price = -1
# lowest_card = -1
# x = 0
# for price in buy_now_prices:
#     x += 1
#     # print(price.text)
#     current_price = int(price.text.replace(',',''))
#     if lowest_price == -1:
#         lowest_price = int(current_price)
#         lowest_card = x
#     else:
#         if int(current_price) < int(lowest_price):
#             lowest_price = int(current_price)
#             lowest_card = x
#
#
# player_purchased_name = WebDriverWait(driver, 30).until(EC.visibility_of_all_elements_located((By.XPATH, f'/html/body/main/section/section/div[2]/div/div/section[1]/div/ul/li[{lowest_card}]/div/div[1]/div[2]')))
# for i in player_purchased_name:
#     print("Player Name: " + i.text)
# print("Purchased Price: " + str(lowest_price))
#
# select_player = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, f'/html/body/main/section/section/div[2]/div/div/section[1]/div/ul/li[{lowest_card}]')))
# select_player.click()
#
# buy_now_btn = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[2]/button[2]')))
# buy_now_btn.click()
#
# confirm_buy = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/section/div/div/button[1]')))
# confirm_buy.click()
#
# list_on_transfer_market_btn = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[2]/div[1]/button')))
# list_on_transfer_market_btn.click()

transfer_list_btn = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/section/section/div[2]/div/div/div[3]')))
transfer_list_btn.click()

item_list = WebDriverWait(driver, 30).until(EC.visibility_of_all_elements_located((By.XPATH, '/html/body/main/section/section/div[2]/div/div/div/section[2]/ul')))
for i in item_list:
    print(i.text)

