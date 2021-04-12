import pandas as pd

delCategoria = "ROUPA FEMININA"
df2 = pd.read_csv("Produto.csv", delimiter=";")
df2.set_index('Codigo_Produto', inplace=True)
print(df2.Categoria_Produto.replace(delCategoria, "None", inplace = True))
