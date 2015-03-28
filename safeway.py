#import time 

from selenium import webdriver
from selenium.webdriver.support import expected_conditions

def main():
  USER_ID = ''
  CONTRASENA = ''
  
  driver = webdriver.Firefox()
  driver.implicitly_wait(8)
  driver.get('https://www.safeway.com/ShopStores/OSSO-Login.page')
  userIdInput = driver.find_element_by_id('userId')
  userIdInput.send_keys(USER_ID)
  contrasena = driver.find_element_by_id('password')
  contrasena.send_keys(CONTRASENA)
  signIn = driver.find_element_by_id('SignInBtn')
  signIn.click()

  # Sleep and then proceed with the checks.
  # Do another wait here.
  j4u_link = driver.find_element_by_xpath('//a[@href="/ShopStores/Offers-Landing-IMG.page"]')
  driver.get('http://www.safeway.com/ShopStores/Justforu-PersonalizedDeals.page')
  disclaimer_div = driver.find_element_by_id('disclaimer-1007')
  driver.get('http://www.safeway.com/ShopStores/Justforu-CouponCenter.page')
  disclaimer_div_ii = driver.find_element_by_id('disclaimer-1007')

  driver.quit()

main()
