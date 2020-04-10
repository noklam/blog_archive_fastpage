# ETF Mixer
Use case:
ETF A: 30% Apple, 10% Microsoft, 60% other
ETF B: 10% Apple, 30% Microsoft, 65% other

Say you want to buy ETF in the market, but your ideal portfilo is having 20% Apple and 20% Microsoft and the rest you don't care about too much. One way of achieveing this is to build a portfolio of ETA A + ETF B to get what you want. This is easy to calculate with just 2 ETFs and 2 stocks, it get messy when you want 10 stocks with 100+ ETFs.

__This simple tool is build exactly for this purpose.__


## Component
* A scraping script to get you the etfs constituents (you can add your list to etf_list.csv)
* A Optimizer to solve the combination while minimizing the factor
* A Web app to display the result with sliders to play around 

Factor
* Lower management fee preferred
* Numbers of ETF as few as possible 
* Only consider a given number of ETFs

# Reminder
* management fee is not included.
* there could be multiple 

# Resource
* IEX API
* https://hackernoon.com/python-notebook-research-to-replicate-etf-using-free-data-ca9f88eb7349

tags: optimization, etf constituents, altair, portfolio