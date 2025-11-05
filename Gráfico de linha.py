#Gráfico de linha - Tendência de Estoque Diário
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7]
y = [100, 95, 110, 105, 120, 115, 130]

plt.plot(x, y)
plt.title("Quantidade de maçãs ao longo de uma semana")
plt.xlabel("Tempo (dias da semana)")
plt.ylabel("Valor (estoque)")
plt.show()
