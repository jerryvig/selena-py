from pyglib import app
from pyglib import gflags
from selenium import webdriver

FLAGS = gflags.FLAGS

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
  ticker_list = ['AAPL', 'GOOGL', 'MSFT', 'FB', 'AMZN', 'NFLX', 'TSLA']

  browser = get_browser(FLAGS.browser_driver)
  if not browser:
    raise Error(
        'Failed to create browser instance with flag %s' % FLAGS.browser_driver)

  try:
    browser.get('http://financials.morningstar.com/income-statement/is.html?t=%s&region=USA' % ticker_list[3])
    body_element = browser.find_element_by_tag_name('body')
    revenue_row_elements = body_element.find_elements_by_xpath('//div[@id="data_i1"]')
    if revenue_row_elements:
      revenue_row = revenue_row_elements[0]
      y1_element = revenue_row.find_element_by_id('Y_1')
      y2_element = revenue_row.find_element_by_id('Y_2')
      y3_element = revenue_row.find_element_by_id('Y_3')
      y4_element = revenue_row.find_element_by_id('Y_4')
      y5_element = revenue_row.find_element_by_id('Y_5')
      y6_element = revenue_row.find_element_by_id('Y_6')
      if y1_element:
        print 'year one raw value = ' + str(y1_element.get_attribute('rawvalue'))
      if y2_element:
        print 'year two raw value = ' + str(y2_element.get_attribute('rawvalue'))
      if y3_element:
        print 'year three raw val = ' + str(y3_element.get_attribute('rawvalue'))
      if y4_element:
        print 'year four raw val = ' + str(y4_element.get_attribute('rawvalue'))
      if y5_element:
        print 'year five raw val = ' + str(y5_element.get_attribute('rawvalue'))
      if y6_element:
        print 'year six raw val = ' + str(y6_element.get_attribute('rawvalue'))
  finally:
    browser.close()
    quit()

if __name__ == '__main__':
  app.run()
