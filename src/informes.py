COLUMNAS = {
    "PONDERA": {"tipo": "int", "completitud": 100},
    "ESTADO": {"tipo": "int", "completitud": 98},
    "CAT_OCUP": {"tipo": "int", "completitud": 92},
    "EDAD": {"tipo": "int", "completitud": 100},
    "REGION": {"tipo": "int", "completitud": 100},
    "AGLOMERADO": {"tipo": "int", "completitud": 100},
    "ANO4": {"tipo": "int", "completitud": 100},
    "TRIMESTRE": {"tipo": "int", "completitud": 100},
    "ITF": {"tipo": "int", "completitud": 85},
    "MAS_500": {"tipo": "string", "completitud": 100},
    "GDECCFR": {"tipo": "int", "completitud": 88}
}


ROLES = {
    "docente": {
        "columnas": ["EDAD", "ESTADO", "CAT_OCUP", "REGION"],
        "criterio": "nombre",
        "orden": "A"
    },

    "investigador": {
        "columnas": ["EDAD", "REGION", "AGLOMERADO", "ITF", "GDECCFR"],
        "criterio": "completitud",
        "orden": "B",
        "minimo": 90
    },

    "analista": {
        "columnas": ["PONDERA", "ESTADO", "ITF", "ANO4", "TRIMESTRE"],
        "criterio": "completitud",
        "orden": "B"
    }
}


def generar_informe(rol=None):
    """
    Genera un informe de columnas según el rol indicado.

    Si no se indica un rol, devuelve todas las columnas
    ordenadas por completitud de forma descendente.
    """

    if rol is None:
        columnas = list(COLUMNAS.items())
        return sorted(
            columnas,
            key=lambda x: x[1]["completitud"],
            reverse=True
        )

    if rol not in ROLES:
        return []

    configuracion = ROLES[rol]

    columnas = [
        (nombre, COLUMNAS[nombre])
        for nombre in configuracion["columnas"]
    ]

    if "minimo" in configuracion:
        minimo = configuracion["minimo"]

        columnas = list(
            filter(
                lambda x: x[1]["completitud"] >= minimo,
                columnas
            )
        )

    criterio = configuracion["criterio"]
    descendente = configuracion["orden"] == "B"

    if criterio == "nombre":
        columnas = sorted(
            columnas,
            key=lambda x: x[0],
            reverse=descendente
        )

    elif criterio == "completitud":
        columnas = sorted(
            columnas,
            key=lambda x: x[1]["completitud"],
            reverse=descendente
        )

    return columnas


def mostrar_informe(rol=None):
    """
    Muestra por pantalla el informe generado para un rol.
    """

    informe = generar_informe(rol)

    for nombre, datos in informe:
        print(
            nombre,
            "- Tipo:", datos["tipo"],
            "- Completitud:", str(datos["completitud"]) + "%"
        )
