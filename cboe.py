
import time


import urllib2
from selenium import webdriver

def get_csv_file(ticker):
	BASE_URL = 'http://www.cboe.com/DelayedQuote/QuoteTableDownload.aspx'
	driver = webdriver.Chrome()
	driver.get(BASE_URL)
	input = driver.find_element_by_id('ctl00_ctl00_AllContent_ContentMain_QuoteTableDownloadCtl1_txtTicker')
	input.send_keys(ticker)
	submit_button = driver.find_element_by_id('ctl00_ctl00_AllContent_ContentMain_QuoteTableDownloadCtl1_cmdSubmit')
	submit_button.click()
	time.sleep(5)
	driver.quit()

def get_real_time_quote(ticker):
	response = urllib2.urlopen('http://download.finance.yahoo.com/d/quotes.csv?s=' + ticker + '&f=sk1')
	parts = response.read().split(',')
	ticker = parts[0].replace('"', '')
	quoteParts = parts[1].split('<b>')
	quotePartsII = quoteParts[1].split('</b>')
	quoteObject = {'ticker': ticker, 'quote': quotePartsII[0]}
	return quoteObject

def parse_csv_file():
	print 'parsing the CSV file here.'

#get_csv_file('AAPL')
#print get_real_time_quote('GOOG')
parse_csv_file()
