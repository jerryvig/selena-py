from pyglib import app
from pyglib import log
from selenium import webdriver
from selenium.webdriver.support import expected_conditions


def get_driver(name):
  if name == 'Chrome':
    return webdriver.Chrome()
  elif name == 'Firefox':
    return webdriver.Firefox()
  elif name == 'PhantomJS':
    return webdriver.PhantomJS()


def loadPersonalizedDeals(driver):
  driver.get('http://www.safeway.com/ShopStores/Justforu-Coupons.page#/offerTypes/PD')
  try:
    elements = driver.find_element_by_xpath('//a[@href="#/offerTypes/PD"]')
    log.info('elements = %s', elements) 
    # Continue the logic here.
  except:
    log.info('GIVING UP')


def main(unused_argv):
  USER_ID = 'agentq314@yahoo.com'
  CONTRASENA = 'overthere'
  
  driver = get_driver('Chrome')
  try:
    driver.implicitly_wait(8)
    driver.get('https://www.safeway.com/CMS/account/login/')
    userIdInput = driver.find_element_by_id('input-email')
    userIdInput.send_keys(USER_ID)
    contrasena = driver.find_element_by_id('password-password')
    contrasena.send_keys(CONTRASENA)
    signIn = driver.find_element_by_id('create-account-btn')
    signIn.send_keys('\n')

    # Sleep and then proceed with the checks.
    # Do another wait here.
    try:
      j4u_link = driver.find_element_by_xpath('//a[@href="/ShopStores/Offers-Landing-IMG.page"]')
      loadPersonalizedDeals(driver)
    except:
      loadPersonalizedDeals(driver)
  finally:
    driver.close()


if __name__ == '__main__':
  app.run()

