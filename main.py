from selenium import webdriver
from dotenv import load_dotenv
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

load_dotenv('variables.env')

tw_login = os.getenv('TW_LOGIN')
tw_pw = os.getenv('TW_PW')
tw_handle = os.getenv('TW_HANDLE')

chromedriver = '/Users/gael/Desktop/100_days_code/*Tools/chromedriver'
driver = webdriver.Chrome(chromedriver)

driver.get('https://www.speedtest.net/')
time.sleep(1)

accept_cookies = driver.find_element(By.ID, 'onetrust-accept-btn-handler')
accept_cookies.click()
time.sleep(1)

close_textbox = driver.find_element(By.CLASS_NAME, 'close-btn')
close_textbox.click()
time.sleep(1)

start_test = driver.find_element(By.CLASS_NAME, 'js-start-test')
start_test.click()
time.sleep(45)

close_button = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/a')
close_button.click()
time.sleep(1)

download_speed = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
upload_speed = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text

tweet = f"Bonjour REDbySFR pourquoi j'ai seulement {download_speed}down/{upload_speed}up contre 1Go up/1Go down promis ?"

driver.get('https://twitter.com/i/flow/login')
time.sleep(3)

login = driver.find_element(By.NAME, 'text')
login.click()
login.send_keys(tw_login)
time.sleep(3)

next_btn = driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]')
next_btn.click()
time.sleep(3)

try:
    handle = driver.find_element(By.NAME, 'text')
    handle.click()
    handle.send_keys(tw_handle)
    time.sleep(1)
    nex_btn_2 = driver.find_element(By.XPATH, '//*[@data-testid="ocfEnterTextNextButton"]')
    nex_btn_2.click()
    time.sleep(2)
except:
    pass

pw = driver.find_element(By.NAME, 'password')
pw.click()
pw.send_keys(tw_pw)
time.sleep(3)

login_btn = driver.find_element(By.XPATH, '//*[@data-testid="LoginForm_Login_Button"]')
login_btn.click()
time.sleep(3)

tweet_area = driver.find_element(By.CLASS_NAME, 'public-DraftStyleDefault-block')
tweet_area.click()
tweet_area.send_keys(tweet)

send_tweet = driver.find_element(By.XPATH, '//*[@data-testid="tweetButtonInline"]')
send_tweet.click()

time.sleep(5)
driver.quit()



