# report.py
#
# Exercise 24
# Define a function to read portfolio file
# Define a function to read prices file
import csv
def read_portfolio(filename):

    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            stock = {
                'name': row[0], 'shares': int(row[1]), 'price': float(row[2])
            }
            portfolio.append(stock)

    return portfolio

def read_prices(filename):
    prices = {}
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass

    return prices

def make_report(portfolio, prices):
    rows = []
    for stock in portfolio:
        name = stock['name']
        shares = stock['shares']
        current_price = prices[name]
        change = current_price - stock['price']
        row = (name, shares, current_price, change)
        rows.append(row)
    return rows

portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')
report = make_report(portfolio, prices)


header = ('Name', 'Shares', 'Price', 'Change')
print('%10s %10s %10s %10s' % header)
print(('-' * 10 + ' ') * len(header))
for r in report:
    print('%10s %10d %10.2f %10.2f' % r)
