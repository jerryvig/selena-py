import time

from selenium import webdriver

def main():
  driver = webdriver.Firefox()
  driver.get('https://www.safeway.com/ShopStores/OSSO-Login.page')
  userIdInput = driver.find_element_by_id('userId')
  userIdInput.send_keys('agentq314@yahoo.com')
  contrasena = driver.find_element_by_id('password')
  contrasena.send_keys('overthere')
  signIn = driver.find_element_by_id('SignInBtn')
  signIn.click()

  # Sleep and then proceed with the checks.
  time.sleep(5)
  driver.quit()

main()
