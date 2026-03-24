#!/bin/bash

echo = " Iniciando descarga archivo CSV"
URL="https://skyserver.sdss.org/dr18/SkyServerWS/SearchTools/SqlSearch?format=csv&cmd=SELECT%20TOP%2050000%20s.class,s.z,p.g,p.r%20FROM%20SpecObj%20s%20JOIN%20PhotoObj%20p%20ON%20s.bestObjID=p.objID%20WHERE%20s.class=%27QSO%27%20OR%20s.class=%27GALAXY%27"
wget -q -O datos_sdss.csv "$URL"
echo = "Catalogo SDSS DR18 descargado" 
head -n 5 datos_sdss.csv

echo = "Creando base de datos"
python3 constructor_db.py

echo = "Generando analisis"
python3 analisis_visual.py




