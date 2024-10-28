
# Proyecto4-AnalisisFacua (sin terminar)

Este proyecto tiene como objetivo recolectar y analizar datos sobre los precios de productos en diferentes supermercados de España a través de la página web FACUA: Precios Supermercados. Utilizando herramientas de scraping, procesamiento y análisis de datos, se busca obtener insights sobre la variabilidad de precios entre supermercados y detectar posibles tendencias o anomalías en los precios.

## Descripción del Proyecto
La página FACUA: Precios Supermercados ofrece datos actualizados sobre los precios de productos básicos en seis supermercados grandes de España: Alcampo, Carrefour, Dia, Eroski, Hipercor y Mercadona. La plataforma permite a los usuarios comparar precios de productos como aceite y leche, observar la evolución de precios en distintas fechas y monitorear las mayores subidas de precios recientes. Este proyecto se enfoca en aprovechar estos datos para realizar un análisis exhaustivo de los precios en diferentes supermercados.

## Objetivos Específicos
- **Scraping de datos**: Extraer información detallada de todos los productos disponibles en la web de FACUA para cada uno de los supermercados listados.
- **Almacenamiento en base de datos**: Crear una base de datos en SQL que almacene la información de manera estructurada.
- **Análisis de Datos**:
  - Comparar precios entre supermercados.
  - Analizar la evolución de precios a lo largo del tiempo.
  - Detectar anomalías o cambios significativos en los precios.
  - Evaluar la dispersión de precios y calcular el precio promedio por producto en cada supermercado.
- **Visualización de datos**: Generar gráficos y visualizaciones que presenten los resultados del análisis de forma clara y comprensible.

## Estructura del Proyecto
La estructura del proyecto es la siguiente:

```
├── .gitignore
├── datos
│   ├── extractos
│   ├── jsons
│   ├── tablas
│   ├── df_historico2024-10-26.csv
│   └── df_productos_2024-10-26.csv
├── notebooks
│   ├── 1_scrapping_de_datos.ipynb
│   ├── 2_creacion_base_de_datos.ipynb
│   └── 3_analisis_visualizacion_datos.ipynb
├── src
│   ├── support_base_de_datos.py
│   └── support_scrapping_datos.py
└── README.md
```

### Descripción de Carpetas y Archivos
- **datos**: Contiene los archivos CSV y subcarpetas como `extractos`, `jsons` y `tablas`, donde se almacena la información recolectada y procesada.
- **notebooks**: Incluye los notebooks de Jupyter que abarcan diferentes etapas del proyecto:
  - `1_scrapping_de_datos.ipynb`: Realiza el scraping de los precios de productos desde la web de FACUA.
  - `2_creacion_base_de_datos.ipynb`: Crea y estructura la base de datos en SQL con los datos recolectados.
  - `3_analisis_visualizacion_datos.ipynb`: Realiza el análisis exploratorio de los datos y genera visualizaciones.
- **src**: Contiene los scripts de soporte para scraping y manipulación de la base de datos, incluyendo:
  - `support_scrapping_datos.py`: Funciones de scraping para obtener datos de FACUA.
  - `support_base_de_datos.py`: Funciones para manejar la base de datos SQL.


## Requisitos
Este proyecto requiere Python 3.12 y las siguientes bibliotecas:

- `pandas`
- `numpy`
- `matplotlib`
- `selenium`
- `requests`
- `BeautifulSoup4`
- `sqlalchemy`
- `psycopg2`

Para instalar estas dependencias, puedes ejecutar el siguiente comando:

```bash
pip install -r requirements.txt
```

## Descripción de los Notebooks
- **1_scrapping_de_datos.ipynb**: Este notebook utiliza Selenium y BeautifulSoup para realizar scraping de datos desde FACUA, obteniendo precios y detalles de productos en los diferentes supermercados.
- **2_creacion_base_de_datos.ipynb**: Crea una base de datos SQL y organiza los datos recolectados en una estructura relacional. Utiliza `psycopg2` y `sqlalchemy` para la gestión y carga de datos.
- **3_analisis_visualizacion_datos.ipynb**: Realiza un análisis exploratorio de los precios, comparando entre supermercados y visualizando patrones y tendencias de precios a lo largo del tiempo.

## Funcionalidades Clave
- **Scraping Automatizado**: Recopilación de datos de precios y productos de la página FACUA.
- **Almacenamiento en Base de Datos**: Organización de datos en una base de datos SQL estructurada.
- **Análisis de Precios**: Comparaciones y análisis de la evolución y dispersión de precios.
- **Visualización de Resultados**: Gráficos y visualizaciones para facilitar la interpretación de los datos.

## Ejecución del Proyecto
1. Ejecutar el script de scraping (`support_scrapping_datos.py`) para recolectar los datos.
2. Utilizar el notebook `2_creacion_base_de_datos.ipynb` para cargar los datos en la base de datos SQL.
3. Ejecutar el notebook `3_analisis_visualizacion_datos.ipynb` para realizar el análisis y visualizar los resultados.

## Nexts Steps
Se que las tablas se podrian normalizar mucho mas en la tabla de productos para las columnas, supermercado, categoria y subcategoria, pero por temas de tiempo, lo he dejado como está.
