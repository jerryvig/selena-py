from selenium import webdriver

BASE_URL = 'http://www.cboe.com/DelayedQuote/QuoteTableDownload.aspx'
driver = webdriver.Chrome()
driver.get(BASE_URL)
input = driver.find_element_by_id('ctl00_ctl00_AllContent_ContentMain_QuoteTableDownloadCtl1_txtTicker')
input.send_keys('GOOG')
submit_button = driver.find_element_by_id('ctl00_ctl00_AllContent_ContentMain_QuoteTableDownloadCtl1_cmdSubmit')
submit_button.click()

# driver.quit()
