import numpy as np
import matplotlib.pyplot as plt

# total population
greyhounds = 500
labs = 500

# dog height, using +/- 4 inches
grey_height = 28 + 4 * np.random.randn(greyhounds)
lab_height = 24 + 4 * np.random.randn(labs)

plt.hist([grey_height, lab_height], stacked=True, color=['g', 'b'])
plt.show()