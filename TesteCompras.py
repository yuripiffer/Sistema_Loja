import pandas as pd

prod = pd.read_csv("Produto.csv", delimiter = ";")
df = pd.DataFrame(prod)
#print(df)
print(df["Nome_Produto"])