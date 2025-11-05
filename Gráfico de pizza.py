#Gráfico de pizza - Proporção de Categorias
import matplotlib.pyplot as plt

# Dados simulados de giro de estoque (exemplo em porcentagem)
categorias = ['Eletrônicos', 'Vestuário', 'Alimentos']
percentuais_valores = [55, 28, 17] # Soma deve ser 100%

# Configuração para destacar uma fatia (opcional)
explode = (0.025, 0.05, 0.05)  # Destaca a primeira fatia

# Criando o gráfico de pizza
fig1, ax1 = plt.subplots()
ax1.pie(percentuais_valores, 
        explode=explode, 
        labels=categorias, 
        autopct='%1.1f%%',
        shadow=True, 
        startangle=90,
        wedgeprops={"edgecolor":"black", 'linewidth': 1, 'antialiased': True})

# Assegura que o gráfico seja um círculo
ax1.axis('equal')  

# Adicionando título
plt.title("Distribuição do Giro de Estoque", fontsize=14)

# Exibindo a legenda (opcional, pois os rótulos já estão presentes)
# plt.legend(categorias_giro, title="Categorias", loc="center left", bbox_to_anchor=(1, 0, 0.5))

plt.show()
