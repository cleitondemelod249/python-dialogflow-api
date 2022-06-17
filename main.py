from google_auth_oauthlib.flow import Flow
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from ut import utils

appflow = Flow.from_client_secrets_file(
    'client_secrets.json',
    scopes=['openid', 'https://www.googleapis.com/auth/dialogflow',
            'https://www.googleapis.com/auth/cloud-platform'],
    redirect_uri='http://localhost:5000')

auth_uri = appflow.authorization_url()
driver = webdriver.Chrome()
driver.get(auth_uri[0])
username = driver.find_element(By.NAME, 'identifier')
username.send_keys(utils.USERNAME)
username.send_keys(Keys.RETURN)
time.sleep(3)
passwd = driver.find_element(By.NAME, 'password')
passwd.send_keys(utils.PASSWD)
passwd.send_keys(Keys.RETURN)
time.sleep(40)
driver.quit()