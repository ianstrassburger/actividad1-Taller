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
    "GDECCFR": {"tipo": "int", "completitud": 88},
    "NIVEL_ED": {"tipo": "int", "completitud": 88}
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
    },

    "economista": {
        "columnas": [
            "PONDERA",
            "ESTADO",
            "CAT_OCUP",
            "REGION",
            "AGLOMERADO",
            "ANO4",
            "TRIMESTRE",
            "ITF",
            "GDECCFR"
        ],
        "criterio": "nombre",
        "orden": "A",
        "minimo": 90
    }
}


def generar_informe(rol=None):
    """
    Genera un informe de columnas según el rol indicado.

    Si no se indica un rol, devuelve todas las columnas
    ordenadas por completitud de forma descendente.
    Si el rol no existe o su criterio es inválido, informa
    el problema sin fallar.
    """

    if rol is None:
        columnas = list(COLUMNAS.items())
        return sorted(
            columnas,
            key=lambda x: x[1]["completitud"],
            reverse=True
        )

    if rol not in ROLES:
        print(f"El rol '{rol}' no existe.")
        return []

    configuracion = ROLES[rol]

    columnas = [
        (nombre, COLUMNAS[nombre])
        for nombre in configuracion["columnas"]
    ]

    minimo = configuracion.get("minimo")
    if minimo is not None:
        columnas = list(
            filter(
                lambda x: x[1]["completitud"] >= minimo,
                columnas
            )
        )

    criterio = configuracion["criterio"]
    descendente = configuracion["orden"] == "B"

    if criterio not in ("nombre", "completitud"):
        print(f"Criterio '{criterio}' inválido para el rol '{rol}'.")
        return columnas

    if criterio == "nombre":
        columnas = sorted(
            columnas,
            key=lambda x: x[0],
            reverse=descendente
        )

    else:
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
