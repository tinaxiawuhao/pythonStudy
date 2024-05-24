import matplotlib.pyplot as plt
import numpy as np

x = np.array(["html", "python", "c/c++", "java"])
y = np.array([12, 22, 6, 18])

plt.bar(x, y,  color = ["#4CAF50","red","hotpink","#556B2F"],width = 0.1)
plt.show()

plt.barh(x, y, height = 0.1,color = ["#4CAF50","red","hotpink","#556B2F"])
plt.show()