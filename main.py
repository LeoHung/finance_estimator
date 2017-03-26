from item import Item, NormalGrowthF, ConstantGrowthF, LoadGrowthFromHistory, Composite
import numpy as np
import matplotlib.pyplot as plt

def LoadHistoryPrices(path):
  return [price for price in reversed([float(l) for l in open(path)])]

def main():
  cycles = 36 # 3 years
  N = 100 # sampling 50 lines

  # saving account
  saving_item = Item(30000.0, ConstantGrowthF(1.00083).call, ConstantGrowthF(0.0).call)
  saving_amounts = saving_item.run(cycles)

  # GOOG stocks
  goog_growth = NormalGrowthF(LoadGrowthFromHistory(LoadHistoryPrices("data/goog.p")))
  goog_item = Item(12216.45, goog_growth.call, ConstantGrowthF(800.0).call)
  goog_amounts = goog_item.run(cycles)

  # ETF - VOO
  voo_growth = NormalGrowthF(LoadGrowthFromHistory(LoadHistoryPrices("data/voo.p")))
  voo_item = Item(860.0, voo_growth.call, ConstantGrowthF(2000.0).call)
  voo_amounts = voo_item.run(cycles)

  # ETF - VDC
  vdc_growth = NormalGrowthF(LoadGrowthFromHistory(LoadHistoryPrices("data/vdc.p")))
  vdc_item = Item(0.0, vdc_growth.call, ConstantGrowthF(0.0).call)
  vdc_amounts = vdc_item.run(cycles)

  compo = Composite([saving_item, goog_item, voo_item, vdc_item])

  sum_amounts = compo.run(cycles)

  array_of_sum_amounts = []
  for i in xrange(N):
    array_of_sum_amounts.append(compo.run(cycles))

  # Composite
  t = np.arange(0, len(array_of_sum_amounts[0]), 1)

  for i in xrange(N):
    plt.plot(t, array_of_sum_amounts[i])

  plt.ylim((40000, 270000))
  plt.show()

if __name__ == "__main__":
  main()
