import time
from pyglib import app
from pyglib import log
from selenium import webdriver

IMPLICIT_WAIT = 9
USER_ID = 'agentq314@yahoo.com'
CONTRASENA = 'overthere'
LOGIN_PAGE_URL = 'https://www.safeway.com/CMS/account/login/'
PERSONALIZED_DEALS_PAGE_URL = 'http://www.safeway.com/ShopStores/Justforu-Coupons.page#/offerTypes/PD'
COUPONS_PAGE_URL = 'http://www.safeway.com/ShopStores/Justforu-Coupons.page#/offerTypes/CC'
J4U_TRIES = 3


def get_driver(name):
  if name == 'Chrome':
    return webdriver.Chrome()
  elif name == 'Firefox':
    return webdriver.Firefox()
  elif name == 'PhantomJS':
    return webdriver.PhantomJS()


def load_personalized(driver):
  driver.get(PERSONALIZED_DEALS_PAGE_URL)
  elements = driver.find_elements_by_xpath('//a[@href="#/offerTypes/PD"]')
  log.info('PD link elements = %s', elements)
  make_my_store_elements = driver.find_elements_by_xpath(
      '//button[text()="Make this My Store"]')
  for button in make_my_store_elements:
    button.click()
    log.info('Sleeping %d seconds...', IMPLICIT_WAIT)
    time.sleep(IMPLICIT_WAIT)
    break

  add_buttons = driver.find_elements_by_xpath('//span[text()="Add"]')
  log.info('Found %d buttons on personalized deals page.', len(add_buttons))
  for button in add_buttons:
    button.click()


def load_coupons(driver):
  driver.get(COUPONS_PAGE_URL)
  elements = driver.find_element_by_xpath('//a[@href="#/offerTypes/CC"]')
  log.info('CC link elements = %s', elements)
  add_buttons = driver.find_elements_by_xpath('//span[text()="Add"]')
  log.info('Found %d buttons on coupons page.', len(add_buttons))
  for button in add_buttons:
    button.click()


def get_j4u_link(driver):
  j4u_link = None
  for i in xrange(J4U_TRIES):
    j4u_link = driver.find_element_by_xpath(
        '//a[@href="/ShopStores/Offers-Landing-IMG.page"]')
    if j4u_link:
      return j4u_link
  return j4u_link


def main(unused_argv):
  driver = get_driver('Chrome')
  try:
    driver.implicitly_wait(IMPLICIT_WAIT)
    driver.get(LOGIN_PAGE_URL)
    user_id_input = driver.find_element_by_id('input-email')
    user_id_input.send_keys(USER_ID)
    contrasena = driver.find_element_by_id('password-password')
    contrasena.send_keys(CONTRASENA)
    sign_in_boton = driver.find_element_by_id('create-account-btn')
    sign_in_boton.send_keys('\n')

    j4u_link = get_j4u_link(driver)
    if j4u_link:
      load_personalized(driver)
      time.sleep(IMPLICIT_WAIT)
      log.info('Sleeping %d seconds...', IMPLICIT_WAIT)
      load_coupons(driver)

  finally:
    driver.close()


if __name__ == '__main__':
  app.run()

