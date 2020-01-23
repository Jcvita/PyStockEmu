'''
    virtual stonk trading simulator 
'''

from dataclasses import dataclass

@dataclass
class Agent:
    def __init__(self, m, p):
        self.money = m
        self.portfolio = p

    def initialize(self, m=100000):
        self.money = m
        self.portfolio = []
    
    def buy(self, stock):
        self.money -= stock.price
        self.portfolio.append(stock.name)
    
    def sell(self, stock):
        if stock.name in portfolio:
            self.money += stock.price
            self.portfolio.remove(stock.name)
        

@dataclass
class Stock:
    def __init__(self, n, p):
        self.name = n
        self.price = p


""" 

def initialize(agent, startamt, realtime = False):
    if isinstance(agent, Agent):
        agent.money = startamt
        agent.portfolio = []
    return agent

def buy(agent, stock):
    if isinstance(agent, Agent) and isinstance(stock, Stock):
        agent.money -= stock.price
    else:
        print('Cannot buy. Type error')
"""

joe = Agent(0,0)
msft = Stock(0,0)
msft.name = 'msft'
msft.price = 69.0
joe.initialize(690000)
joe.buy(msft)
print(joe.money)
print(joe.portfolio)
