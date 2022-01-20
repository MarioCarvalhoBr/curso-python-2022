from matplotlib import colors
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["Segunda", "Terça", "Quarta", "Quinta"])
y = np.array([3, 8, 1, 10])

plt.bar(x,y)
plt.ylabel("KM percorrido")
plt.xlabel("Dia da semana")
plt.show()