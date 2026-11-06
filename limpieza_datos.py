import pandas as pd 

ruta = "https://raw.githubusercontent.com/VMjavier/claseAnalisisDatos/refs/heads/main/veterinaria_colombia.csv"

df = pd.read_csv(ruta)

print("="*50)
print(df.head())
print("-"*50)

print("="*50)
print(df.info())
print("="*50)


print("="*50)
print(df.describe())
print("="*50)


print("="*50)
print(df.columns)
print("="*50)


print("="*50)
print(df.insull().sum())
print("="*50)


print("="*50)
print(df.shape) #filas columnas)
print("="*50)


print("="*50)
print(df["Raza"])
print("="*50)


print("="*50)
print(df[["Raza","Especie"]])
print("="*50)


print("="*50)
print(df[df["Raza"] == "Criollo"])
print("="*50)

