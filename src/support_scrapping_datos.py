import re

def extraer_cantidad_unidad(texto):
    """
    Extrae una cantidad numérica y su unidad de medida de un texto dado.

    La función utiliza una expresión regular para buscar una cantidad (número) 
    seguida de una unidad de medida en el texto. Si encuentra una coincidencia, 
    devuelve la cantidad y la unidad en minúsculas, sin ningún '.' al final;
    en caso contrario, devuelve `None, None`.

    Parámetros:
    -----------
    texto : str
        El texto del cual se quiere extraer la cantidad y la unidad.

    Retorna:
    --------
    tuple
        Una tupla con dos elementos:
        - cantidad (str): La cantidad extraída del texto.
        - unidad (str): La unidad de medida extraída del texto en minúsculas 
          y sin un '.' al final. 
        Si no hay coincidencia, retorna `(None, None)`.

    Ejemplo:
    --------
    >>> extraer_cantidad_unidad("250 ml. de agua")
    ('250', 'ml')
    >>> extraer_cantidad_unidad("sin cantidad")
    (None, None)
    """
    
    regex = r"(\d+(?:[.,]?\d*)?)\s?([Ll]|[Mm]l|[Cc]l|[Gg]r|[Kk]g|[Ll]itro[s]?)\.?"

    match = re.search(regex, texto)
    if match:
        cantidad = match.group(1)
        unidad = match.group(2).lower().rstrip('.')  # Eliminamos '.' al final de la unidad si lo tiene
        return cantidad, unidad
    return None, None
