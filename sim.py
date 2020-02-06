'''
    virtual stonk trading simulator 
'''

import os
from dataclasses import dataclass

if 'saves' not in os.listdir():
    createdir = input("No saves directory detected. Create one? (y/n)")
    while not (createdir is not 'y' or createdir is not 'n'):
        print('Invalid Response.')
        createdir = input("No saves directory detected. Create one? (y/n)")
    if createdir == 'y':
        os.mkdir('saves')
        print('Created directory "saves"')
    else:
        print("Ok. Continuing in no-save mode.")


class Stock:

    def __init__(self, name='', price=0):
        self.n = name
        self.p = price

    def update_price(self, price):
        self.p = price


class Portfolio:

    def __init__(self, stocks=None):
        if stocks is None:
            stocks = []

        val = 0
        if len(stocks) == 0:
            self.value = 0
        else:
            for stock in self.stocks:
                val += stock.p

        self.value = val
        self.stocks = stocks

    def add_stock(self, stock):
        self.stocks.append(stock)

    def remove_stock(self, stock):
        self.stocks.remove(stock)

    def list_stocks(self):
        for stock in self.stocks:
            print(stock.name)


class Agent:

    def __init__(self, money=100000, name='trader', portfolio=Portfolio(), agentfile=None):
        self.file = agentfile
        self.nam = name
        self.mon = money
        self.port = portfolio

    def load(self, money=100000, portfolio=Portfolio(), agentfile=None):
        self.mon = money
        self.port = portfolio
        self.file = agentfile

    def save(self, outfile):
        pass

    def buy(self, stock):
        if stock.p == 0:
            print("Warning: Stock price is not loaded or 0")

        self.mon -= stock.p
        self.port.add_stock(stock)

    def sell(self, stock):
        if stock.name in self.port:
            self.mon += stock.price
            self.port.remove_stock(stock)

    def reset(self, start_cash=100000):
        del self.port
        self.mon = start_cash
        self.port = Portfolio()

    def update_portfolio(self):
        # must be called when stock prices change
        self.port.value = 0
        for stock in self.port.stocks:
            self.port.value += stock.p

    def net_worth(self):
        worth = self.mon
        for stock in self.port.stocks:
            worth += stock.p

        return worth



joe = Agent()
msft = Stock()
msft.name = 'msft'
msft.update_price(69.0)
joe.buy(msft)
print(joe.port.value)
joe.update_portfolio()
print(joe.port.value)
print(joe.net_worth())