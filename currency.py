import random
def generate_currency():
	i=0
	file = open('currency.txt', 'w')
	while i < 3000:
		currencys = ['AUD/CHF', 'AUD/JPY', 'AUD/NZD', 'AUD/JPY', 'AUD/JPY', 'AUD/JPY', 'AUD/JPY', 'CAD/JPY','CHF/JPY','EUR/AUD','EUR/CAD','EUR/CHF','EUR/GBP','EUR/JPY','EUR/NZD','GBP/AUD','GBP/CHF','GBP/JPY','NZD/JPY','EUR/USD','GBP/USD','AUD/USD','NZD/USD','USD/JPY','USD/CHF','USD/CAD']

		currency = currencys[random.randint(0,21)]
		file.write(currency + '\n')
		i = i + 1
	file.close()
