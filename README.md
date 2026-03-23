# Ciencia de datos abierta y reproducible

**Problema fisico: grafica de indice de color vs redshift y analisis de distribucion de galaxias**

![Resultado del Análisis](resultado.png)

## Análisis Físico: Índice de Color vs Redshift

Este gráfico es una excelente representación de cómo la astronomía utiliza la fotometría para distinguir entre diferentes tipos de objetos celestes a distancias cosmológicas. El eje horizontal muestra el Redshift ($z$), que mide qué tan rápido se aleja un objeto, mientras que el eje vertical muestra el Índice de Color ($g-r$), la diferencia de magnitud entre los filtros verde y rojo.

### 1. Galaxias Locales (Naranja)
Las galaxias se concentran mayoritariamente en la parte izquierda del gráfico, con un $z < 1$. Forman un "bulbo" denso porque son objetos extendidos que se vuelven muy difíciles de detectar a medida que el redshift aumenta. La amplia dispersión vertical cerca de $z \approx 0.5$ (la "panza") representa la variedad de poblaciones estelares y el efecto de la Corrección-K al cambiar las líneas de emisión de filtro.

### 2. Quásares Primordiales (Azul claro)
Los Quásares (QSO) dominan a partir de $z > 1$ y se extienden hasta $z \approx 7$. Al ser núcleos galácticos activos extremadamente brillantes, podemos verlos a distancias donde una galaxia normal sería invisible. Es notable cómo su color se mantiene relativamente azul ($g-r \approx 0$) hasta $z \approx 3.5$, donde se vuelve más rojo debido a que el bosque Lyman-$\alpha$ (absorción de hidrógeno intergaláctico) entra en los filtros de observación.

### Comparativa: Galaxias vs. Quásares
| Característica | Galaxias (GALAXY) | Quásares (QSO) |
| :--- | :--- | :--- |
| **Rango de Redshift** | Mayormente $0 < z < 1.0$ | Amplio, desde $0$ hasta $7.0$ |
| **Color dominante** | Más "rojas" ($g-r > 0$) | Más "azules" en $z$ bajo |
| **Interpretación** | Población local del universo | Faros distantes del universo temprano |

### Análisis de Valores Atípicos (Outliers)
* **Los "Súper Rojos" ($g-r > 10$):** En muchos casos no es un color real, sino ruido o errores de medición cuando el objeto es casi invisible en el filtro $g$.
* **El Quásar solitario en $z \approx 4$ ($g-r \approx 12$):** A este redshift, la absorción del hidrógeno es tan fuerte que "borra" la luz en el filtro $g$, haciendo que parezca extremadamente rojo para el sensor aunque intrínsecamente sea azul.

### Conclusión
El hecho de que los quásares lleguen hasta $z=7$ indica que observamos objetos de cuando el universo era una fracción de lo que es hoy. La clara separación demuestra que el Índice de Color es una herramienta de diagnóstico poderosa para clasificar estructuras cosmológicas.



