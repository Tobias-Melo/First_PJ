df = pd.read_csv('gasolina.csv')

line_plot = sns.lineplot(x=df['dia'], y=df['venda']).get_figure()
line_plot.savefig('gasolina.png')
