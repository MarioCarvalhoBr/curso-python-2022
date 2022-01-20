import matplotlib.pyplot as plt
import numpy as np
x1 = np.array([80, 85, 90, 95, 100])
x2 = np.array([105, 110, 115, 120, 125])
y1 = np.array([240, 250, 260, 270, 280])
y2 = np.array([290, 300, 310, 320, 330])

plt.subplot(1, 2, 1)
plt.plot(x1, y1)
plt.grid()
plt.xlabel("Média do Pulso")
plt.ylabel("Calorias")


plt.subplot(1, 2, 2)
plt.plot(x2, y2)
plt.grid()
plt.xlabel("Média do Pulso")
plt.ylabel("Calorias")

plt.title("Meu Gráfico")

plt.show()

plt.savefig("graficos/grafico.pdf")