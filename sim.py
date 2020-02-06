'''
    virtual stonk trading simulator 
'''

from dataclasses import dataclass


@dataclass
class Portfolio:

    def __init__(self):
        self.value = 0
        self.stocks = []


@dataclass
class Agent:

    money = None
    portfolio = None

    def __init__(self):
        self.money = 0
        self.portfolio = Portfolio

    def initialize(self, m=100000):
        self.money = m
        self.portfolio = []

    def buy(self, stock):
        self.money -= stock.price
        self.portfolio.append(stock.name)

    def sell(self, stock):
        if stock.name in self.portfolio:
            self.money += stock.price
            self.portfolio.remove(stock.name)

    def reset(self):
        self.money = 0
        self.portfolio = Portfolio


@dataclass
class Stock:

    def __init__(self, n, p):
        self.name = n
        self.price = p

    def update_price(self, p):
        self.price = p


joe = Agent
msft = Stock(0, 0)
msft.name = 'msft'
msft.update_price(69.0)
joe.initialize(690000)
joe.buy(msft)
print(joe.money)
print(joe.portfolio)
