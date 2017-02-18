from pyglib import app
from pyglib import log
from selenium import webdriver

USER_ID = 'agentq314@yahoo.com'
CONTRASENA = 'overthere'


def get_driver(name):
  if name == 'Chrome':
    return webdriver.Chrome()
  elif name == 'Firefox':
    return webdriver.Firefox()
  elif name == 'PhantomJS':
    return webdriver.PhantomJS()


def load_personalized(driver):
  driver.get(
      'http://www.safeway.com/ShopStores/Justforu-Coupons.page#/offerTypes/PD')
  elements = driver.find_element_by_xpath('//a[@href="#/offerTypes/PD"]')
  log.info('elements = %s', elements)
  # Continue the logic here...


def main(unused_argv):
  driver = get_driver('Chrome')
  try:
    driver.implicitly_wait(8)
    driver.get('https://www.safeway.com/CMS/account/login/')
    user_id_input = driver.find_element_by_id('input-email')
    user_id_input.send_keys(USER_ID)
    contrasena = driver.find_element_by_id('password-password')
    contrasena.send_keys(CONTRASENA)
    sign_in = driver.find_element_by_id('create-account-btn')
    sign_in.send_keys('\n')
    driver.implicitly_wait(5)

    load_personalized(driver)
  finally:
    driver.close()


if __name__ == '__main__':
  app.run()

