from pyglib import app
from pyglib import log
from selenium import webdriver

USER_ID = 'agentq314@yahoo.com'
CONTRASENA = 'overthere'
LOGIN_PAGE_URL = 'https://www.safeway.com/CMS/account/login/'
PERSONALIZED_DEALS_PAGE_URL = 'http://www.safeway.com/ShopStores/Justforu-Coupons.page#/offerTypes/PD'

def get_driver(name):
  if name == 'Chrome':
    return webdriver.Chrome()
  elif name == 'Firefox':
    return webdriver.Firefox()
  elif name == 'PhantomJS':
    return webdriver.PhantomJS()


def load_personalized(driver):
  driver.get(PERSONALIZED_DEALS_PAGE_URL)
  elements = driver.find_element_by_xpath('//a[@href="#/offerTypes/PD"]')
  log.info('elements = %s', elements)
  # Continue the logic here...


def main(unused_argv):
  driver = get_driver('Chrome')
  try:
    driver.implicitly_wait(8)
    driver.get(LOGIN_PAGE_URL)
    user_id_input = driver.find_element_by_id('input-email')
    user_id_input.send_keys(USER_ID)
    contrasena = driver.find_element_by_id('password-password')
    contrasena.send_keys(CONTRASENA)
    sign_in_boton = driver.find_element_by_id('create-account-btn')
    sign_in_boton.send_keys('\n')
    sign_in_boton.click()
    
    load_personalized(driver)
  finally:
    driver.close()


if __name__ == '__main__':
  app.run()

