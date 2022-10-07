# código de geração do gráfico

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('gasolina.csv')

dia = df['dia']
preco = df['venda']

sns.lineplot(x=dia, y=preco, color = 'b', label = 'Preço')

# Configurando título e rótulos dos eixos.
plt.title('Preço da gasolina por dia', fontsize=14)
plt.xlabel('Dia', fontsize=12)
plt.ylabel('Preço (R$)', fontsize=12)

# Mudando a grossura dos eixos.
plt.tick_params(axis='both', labelsize=10)

# Legenda no gráfico
plt.legend()

plt.savefig('gasolina.png')
plt.show() # Para 'desenhar' o gráfico
