#Gráfico de barras - Comparação de Produtos
import matplotlib.pyplot as plt

produtos = ['Teclado', 'Mouse', 'Monitor', 'Webcam']
quantidades = [50, 75, 30, 60]

# Criando o gráfico 
plt.bar(produtos, quantidades, color=['skyblue', 'gold', 'lightgreen', 'mediumpurple'])

# Adicionando título e rótulos aos eixos
plt.title("Estoque Atual por Categoria de Produto")
plt.xlabel("Categorias de Produto")
plt.ylabel("Quantidade em Estoque")

# Rotacionar os rótulos do eixo X se necessário
plt.xticks(rotation=45, ha='right')

# Layout ajustado para evitar sobreposição
plt.tight_layout()

# Exibir o gráfico
plt.show()
