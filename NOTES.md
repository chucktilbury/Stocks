# Notes

These notes are not formal design docs. They are random notes to track the development process and help me to not forget what I was doing.

## ToDo

* Properly fork the repos for the libraries that we are using. Wire them up so we can actually use them.
* Develop a widget that can do candlestick and line graphs on the same canvas. Test it. (requires the matplotlib library)
  * Allow different length data sets with horizontal scroll bars.
* Build the user interface with stubbed out menus. UI will use the notebooks and SQL interface from the Accounting app.
* Implement the logic to read the status of a stock from the internet. (requires the pandas library)
* Include the logic to pick one and/or retrieve the lists from the internet.  (there are 100's of stocks)
* Begin to implement the individual indicator strategies as graph entries. Allow more than one to be displayed.
* Allow specific data sets to be stored in the database.
  * Store analysis scenarios in the database.
* Allow automatic scheduled updating of the database from the internet.
* Create a daemon that can run the rules without the UI and send email alerts.

## Done

* This file. :)

## Questions

* Why does bacon taste so good?

## Links
https://www.geeksforgeeks.org/multithreaded-download-of-yahoo-stock-history-with-python-yfinance/
https://pypi.org/project/yfinance/
https://algotrading101.com/learn/yfinance-guide/
https://www.investopedia.com/
https://data.nasdaq.com/tools/python
https://site.financialmodelingprep.com/developer/docs/
https://www.alphavantage.co/
https://developer.morningstar.com/
https://eodhistoricaldata.com/
https://marketstack.com/product


