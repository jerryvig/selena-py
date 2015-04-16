import time
import urllib
import urllib2

class MorningstarCollector:
  MORNINGSTAR_BASE_URL = 'http://financials.morningstar.com/ajax/ReportProcess4HtmlAjax.html'
  LIST_FILE = 'NDX.csv'

  @staticmethod
  def main():
    list_file = open(MorningstarCollector.LIST_FILE)
    raw_list = list_file.readlines()
    ticker_list = [ticker.strip() for ticker in raw_list]

    for ticker in ticker_list:
      print 'Doing ' + ticker
      query_params = {
      	't': 'XNAS:' + ticker,
		'region': 'usa',
		'culture': 'en-US',
		'reportType': 'is',
		'period': '12',
		'dataType': 'A',
		'order': 'asc',
		'columnYear': '5',
		'rounding': '3',
		'view': 'raw',
      }

      request = urllib2.Request(MorningstarCollector.MORNINGSTAR_BASE_URL, 
      	                        urllib.urlencode(query_params))
      response = urllib2.urlopen(request)
      print response.read()
      time.sleep(2)

MorningstarCollector.main()
