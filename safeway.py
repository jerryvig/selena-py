import time

from selenium import webdriver
from selenium.webdriver.support import expected_conditions

def loadPersonalizedDeals(driver):
  driver.get('http://www.safeway.com/ShopStores/Justforu-Coupons.page#/offerTypes/PD')
  driver.find_element_by_xpath('//a[@href="#/offerTypes/PD"]')
  driver.quit()

def main():
  USER_ID = 'agentq314@yahoo.com'
  CONTRASENA = 'overthere'
  
  driver = webdriver.Firefox()
  driver.implicitly_wait(8)
  driver.get('https://www.safeway.com/ShopStores/OSSO-Login.page')
  userIdInput = driver.find_element_by_id('userId')
  userIdInput.send_keys(USER_ID)
  contrasena = driver.find_element_by_id('password')
  contrasena.send_keys(CONTRASENA)
  signIn = driver.find_element_by_id('SignInBtn')
  signIn.send_keys('\n')

  #time.sleep(5)

  # Sleep and then proceed with the checks.
  # Do another wait here.
  try:
    j4u_link = driver.find_element_by_xpath('//a[@href="/ShopStores/Offers-Landing-IMG.page"]')
    loadPersonalizedDeals(driver)
  except:
    loadPersonalizedDeals(driver)

main()
