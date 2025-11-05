#Gráfico de dispersão _ Preço vs. Quantidade
import matplotlib.pyplot as plt
import numpy as np

# Dados simulados: Horas de estudo e notas finais de alunos
np.random.seed(42) # Para reprodutibilidade dos resultados
preco_uni = (50, 120, 300, 80, 20)
estoque = (80, 25, 10, 70, 150)

# Criando o gráfico de dispersão
plt.figure(figsize=(10, 6)) # Define o tamanho da figura
plt.scatter(preco_uni, estoque, color='blue', alpha=1.0) # alpha para transparência

# Adicionando título e rótulos aos eixos
plt.title("Relação entre o preço unitário e a quantidade em estoques", fontsize=15)
plt.xlabel("Preço dos produtos", fontsize=12)
plt.ylabel("Quantidade no estoque", fontsize=12)

# Adicionando grade
plt.grid(True, linestyle='--', alpha=0.6)

# Exibir o gráfico
plt.tight_layout()
plt.show()
