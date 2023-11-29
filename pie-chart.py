# Lets create a pie chart👇

# With Pyplot, you can use the pie() function to draw pie charts.

# A simple pie chart:

import matplotlib.pyplot as plt 
import numpy as np

y = np.array([35,25,25,15])

mylabels = ["Apples", "Bananas", "Mangoes", "Pears"]

myeplode = [0.2,0,0.0,0.0]

plt.pie(y, labels=mylabels, explode=myeplode)
plt.legend()
plt.show()