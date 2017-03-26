import numpy as np
import numpy.random

def LoadGrowthFromHistory(history_prices):
  growth_rates = []
  for i in xrange(len(history_prices) - 1):
    growth_rates.append(history_prices[i+1] / history_prices[i])
  return growth_rates

class NormalGrowthF:
  def __init__(self, history):
    self.mean = np.mean(history)
    self.std = np.std(history)
  def call(self, i):
    return numpy.random.normal(self.mean, self.std)

class ConstantGrowthF:
  def __init__(self, constant):
    self.constant = constant
  def call(self, i):
    return self.constant

class Item:
  # g_f = growth ratio per cycle
  # i_f = delta increase per cycle
  def __init__(self, init_amount, g_f, i_f):
    self.init_amount = init_amount
    self.g_f = g_f
    self.i_f = i_f

  # Next cycle amount = this cycle amount * growth rate + delta increase.
  def run(self, cycles):
    amounts = []
    amount = self.init_amount
    for i in xrange(cycles):
      amount = self.g_f(i) * amount + self.i_f(i)
      amounts.append(amount)
    return amounts

class Composite:
  def __init__(self, items):
    self.items = items

  def Sum(self, array_of_amounts):
    N = len(array_of_amounts[0])
    sum_amounts = []
    for i in xrange(N):
      s = sum([amounts[i] for amounts in array_of_amounts])
      sum_amounts.append(s)
    return sum_amounts

  def run(self, cycles):
    array_of_amounts = []
    for item in self.items:
      array_of_amounts.append(item.run(cycles))
    return self.Sum(array_of_amounts)
