import os
import time
from pyglib import app
from pyglib import gflags
from pyglib import log
from selenium import webdriver

FLAGS = gflags.FLAGS
MORNINGSTAR_BASE_URL = 'http://financials.morningstar.com/income-statement/is.html?t=%s&region=USA'
OUTPUT_FILE_NAME = 'ms_data.csv'

gflags.DEFINE_string(
    'browser_driver', 'Chrome',
    'The name of the browser driver to use, "Chrome", "Firefox", '
    '"PhantomJS", etc.')


class Error(Exception):
  """Base class for exceptions in this module."""
  pass


def get_browser(name):
  if name == 'Chrome':
    return webdriver.Chrome()
  elif name == 'Firefox':
    return webdriver.Firefox()
  elif name == 'PhantomJS':
    return webdriver.PhantomJS()


def main(unused_argv):
  tickers = ('AAPL', 'GOOGL', 'MSFT', 'FB', 'AMZN', 'NFLX', 'TSLA', 'TWTR', 'BABA', 'BIDU', 'PYPL', 'SPLK', 'SQ', 'CRM', 'TWLO', 'BOX')

  browser = get_browser(FLAGS.browser_driver)
  if not browser:
    raise Error(
        'Failed to create browser instance with flag %s' % FLAGS.browser_driver)

  try:
    os.unlink(OUTPUT_FILE_NAME)
  except OSError:
    log.info('The file %s not found in the working directory.', OUTPUT_FILE_NAME)

  try:
    for symbol in tickers:
      browser.get(MORNINGSTAR_BASE_URL % symbol)
      body_element = browser.find_element_by_tag_name('body')
      time.sleep(1.0)
      revenue_row_elements = body_element.find_elements_by_xpath('//div[@id="data_i1"]')
      if revenue_row_elements:
        revenue_row = revenue_row_elements[0]
        y1_element = revenue_row.find_element_by_id('Y_1')
        y2_element = revenue_row.find_element_by_id('Y_2')
        y3_element = revenue_row.find_element_by_id('Y_3')
        y4_element = revenue_row.find_element_by_id('Y_4')
        y5_element = revenue_row.find_element_by_id('Y_5')
        y6_element = revenue_row.find_element_by_id('Y_6')
        y1_raw_val = y1_element.get_attribute('rawvalue') if y1_element else 0
        y2_raw_val = y2_element.get_attribute('rawvalue') if y2_element else 0
        y3_raw_val = y3_element.get_attribute('rawvalue') if y3_element else 0
        y4_raw_val = y4_element.get_attribute('rawvalue') if y4_element else 0
        y5_raw_val = y5_element.get_attribute('rawvalue') if y5_element else 0
        y6_raw_val = y6_element.get_attribute('rawvalue') if y6_element else 0

        with open(OUTPUT_FILE_NAME, 'a') as f:
          f.write('"%s","%s","%s","%s","%s","%s","%s"\n' % (symbol, y1_raw_val, y2_raw_val, y3_raw_val, y4_raw_val, y5_raw_val, y6_raw_val))

      time.sleep(1.25)
  finally:
    browser.close()
    quit()

if __name__ == '__main__':
  app.run()
