import pandas as pd
import numpy as np 
import sqlite3

echo = "Creando base de datos" 

df= pd.read_csv('datos_sdss.csv', skiprows=1)
df_limpio = df.dropna()

conexion = sqlite3.connect('datos_mision.db')
df_limpio.to_sql('Galaxias',conexion, if_exists='replace', index='False')
conexion.close()

print("Base de datos 'datos_mision.db' creada")
