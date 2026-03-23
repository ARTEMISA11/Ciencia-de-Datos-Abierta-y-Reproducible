import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("Iniciando analisis fisico")

conexion = sqlite3.connect('datos_mision.db')
consulta = "SELECT class, z, g, r FROM Galaxias"
df= pd.read_sql_query(consulta,conexion)
conexion.close()

#Indice de color
df['Indice_color']= df['g'] - df['r']

#grafica
plt.style.use('dark_background')
plt.figure(figsize=(10,6))

sns.scatterplot(data=df, x='z', y='Indice_color', hue='class', palette='coolwarm', s=10, alpha=0.7)

plt.title("Indice de color (g-r) vs Redshift (z)")
plt.xlabel("Redshift (z)")
plt.ylabel("Indice de color (g-r)")
plt.tight_layout()
plt.savefig('resultado.png')

print("Grafica creada")

