# Ciencia de datos abierta y reproducible

**Problema físico: gráfica de índice de color vs redshift y análisis de distribución de galaxias**

![Resultado del Análisis](resultado.png)

El eje horizontal muestra el Redshift (z), el cual mide qué tan rápido se aleja un objeto, mientras que el eje vertical muestra el Índice de Color (g-r), la diferencia de magnitud entre los filtros verde y rojo.

### Galaxias Locales (Naranja)
Las galaxias se concentran mayoritariamente en la parte izquierda del gráfico a un z < 1, forman un grupo denso porque son objetos extendidos que se vuelven muy difíciles de detectar a medida que el redshift aumenta. La amplia dispersión vertical cerca de z = 0.5 representa la variedad de poblaciones estelares y el efecto de la Corrección-K necesaria dado que el universo se está expandiendo. Ya que la luz de la galaxia se "estira" en su camino hacia la Tierra, esto hace que una luz que originalmente salió siendo azul o verde, se estire tanto que termine entrando por el filtro rojo en el telescopio, alterando el color que calculamos.

### Quásares Primordiales (Azul claro)
Los Quásares dominan a partir de z > 1 y se extienden hasta z = 7. Al ser núcleos galácticos activos extremadamente brillantes, podemos verlos a distancias donde una galaxia normal sería invisible, es notable cómo su color se mantiene relativamente azul con g-r cercano a 0 hasta z = 3.5, donde se vuelve más rojo. Esto actúa como una forma de extinción debido al enrojecimiento que producen las nubes de hidrógeno que absorben parte de la luz azul en su camino hacia nosotros.

### Comparativa: Galaxias vs. Quásares
* Rango de Redshift: Galaxias mayormente 0 < z < 1,  y  Quásares desde 0 hasta 7.
* Color dominante: Galaxias más "rojas" g-r > 0, y Quásares más "azules" en z bajo.
* Interpretamos eso como que las galaxias son la población local del universo y los Quásares son faros distantes del universo temprano.

### Valores Atípicos 
* Los Súper Rojos (g-r > 10): En muchos casos no es un color real, sino ruido o errores de medición cuando el objeto es casi invisible en el filtro verde (g).
* El Quásar en z = 4 con (g-r = 12): A este redshift, la absorción del hidrógeno es tan fuerte que "borra" la luz en el filtro g, haciendo que parezca extremadamente rojo para el sensor aunque intrínsecamente sea azul.

### Conclusión
El hecho de que los quásares lleguen hasta z = 7 indica que observamos objetos de cuando el universo era una fracción de lo que es hoy. La clara separación demuestra que el Índice de Color es una herramienta de diagnóstico poderosa para clasificar estructuras cosmológicas.
