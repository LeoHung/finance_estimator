from classes import Item, NormalGrowthF, ConstantGrowthF, Composite, LoadNormalGrowthFFromPath
import numpy as np
import matplotlib.pyplot as plt

def main():
  cycles = 36 # 3 years
  N = 50 # sampling 100 lines

  # Save 10k per month into certificate deposite (Assuming APR = 1.115%)
  saving_item = Item(0.0, ConstantGrowthF(1.000915), ConstantGrowthF(10000.0))

  # Buy 10k taiwan 50 etf per month.
  taiwan_50_growthf = LoadNormalGrowthFFromPath("data/taiwan50.p")
  taiwan_50_item = Item(0.0, taiwan_50_growthf, ConstantGrowthF(10000.0))

  composite = Composite([saving_item, taiwan_50_item])

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
