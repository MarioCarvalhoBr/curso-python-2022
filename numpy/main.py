import numpy as np

print("Versão do NumPy: ", np.__version__)

listaM = [1985, 2000, 3000, 4000, 5000, 1500, 60000]
listaH = [1500, 1985, 2000, 3000, 4000, 5000, 60000]

# str, float, int
salariosM = np.array(listaM)
salariosH = np.array(listaH)
quant = len(salariosM)
print("Quantidade de salários: ", quant)

media = np.mean(salariosM)
mediana = np.median(salariosM)
desvio_padrao = np.std(salariosM)

print("Média dos salários: ", round(media, 2))
print("Mediana dos salários: ", round(mediana, 2))
print("Desvio padrão dos salários: ", round(desvio_padrao, 2))
print("Menor: ", np.min(salariosM))
print("Maior: ", np.max(salariosM))
