strikeprice = input('Please enter the strike price, or 0 if done: ')
while strikeprice != 0:
	putCall = input('0 for put, 1 for call: ')
	contractPrice =input('What is the price per contract?: ')
	StockPrice = input('what is the current stock price?: ')
	contractSize = input('how many contracts (typically 100): ')


	if putCall == 0:
		print "with a strike price of %s * %s contracts your total cost of the options is: %s" %(strikeprice, contractSize, contractSize*contractPrice)
		print "the cost of the stocks themselves are %s individually or %s with your %s contract(s)" %(StockPrice, StockPrice*contractSize, contractSize)
		print "therefor if we use the formula of (strikePrice * contractSize) - ((StockPrice*contractSize) + (contractPrice* contractSize)) we get the following profit: "
		while StockPrice > .50:
			print "with a stockPrice of %s you would make a profit of %s (minus the cost to get the contract of course):" %(StockPrice, (strikeprice * contractSize) - ((StockPrice*contractSize) + (contractPrice* contractSize)))
			StockPrice = StockPrice- StockPrice%.50
			StockPrice = StockPrice -.50


	if putCall == 1:
		print "with a strike price of %s * %s contracts your total cost of the options is: %s" %(strikeprice, contractSize, contractSize*contractPrice)
		print "the cost of the stocks themselves are %s individually or %s with your %s contract(s)" %(StockPrice, StockPrice*contractSize, contractSize)
		print "therefor if we use the formula of  ((StockPrice*contractSize) + (contractPrice* contractSize)) - (strikePrice * contractSize)  we get the following profit: "
		while StockPrice < 20.00:
			print "with a stockPrice of %s you would make a profit of %s (minus the cost to get the contract of course):" %(StockPrice, (((StockPrice*contractSize) + (contractPrice* contractSize)) - (strikeprice * contractSize)) )
			StockPrice = StockPrice- StockPrice%.50
			StockPrice = StockPrice +.50