from classes import Item, NormalGrowthF, ConstantGrowthF, Composite, LoadNormalGrowthFFromPath
import numpy as np
import matplotlib.pyplot as plt

def main():
  cycles = 36 # 3 years
  N = 50 # sampling 100 lines

  # saving account
  saving_item = Item(30000.0, ConstantGrowthF(1.00083), ConstantGrowthF(0.0))

  # GOOG stocks
  goog_growth = LoadNormalGrowthFFromPath("data/goog.p")
  goog_item = Item(12216.45, goog_growth, ConstantGrowthF(800.0))

  # ETF - VOO
  voo_growth = LoadNormalGrowthFFromPath("data/voo.p")
  voo_item = Item(860.0, voo_growth, ConstantGrowthF(2000.0))

  # ETF - VDC
  vdc_growth = LoadNormalGrowthFFromPath("data/vdc.p")
  vdc_item = Item(0.0, vdc_growth, ConstantGrowthF(0.0))

  composite = Composite([saving_item, goog_item, voo_item, vdc_item])

  array_of_sum_amounts = []
  for i in xrange(N):
    array_of_sum_amounts.append(composite.Run(cycles))

  # Composite
  t = np.arange(0, len(array_of_sum_amounts[0]), 1)

  # Show Matplot
  for i in xrange(N):
    plt.plot(t, array_of_sum_amounts[i])

  plt.show()

if __name__ == "__main__":
  main()
