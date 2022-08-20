from __future__ import print_function
import rootdir

from pyalgotrade.feed import csvfeed

feed = csvfeed.Feed("Date", "%Y-%m-%d")
feed.addValuesFromCSV("vvothers/orclQuanDlData_short.csv")
for dateTime, value in feed:
    print(dateTime, value)
