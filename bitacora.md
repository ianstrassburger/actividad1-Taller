# Bitácora - Actividad 1

**Alumno:** Ian Strassburger  
**Legajo:** 018833/6

## Decisiones de diseño

Usé dos diccionarios principales: `COLUMNAS` y `ROLES`.

En `COLUMNAS` guardé el nombre de cada columna junto con su tipo y porcentaje
de completitud. En `ROLES` guardé las columnas de interés, el criterio de
ordenamiento, el orden y, cuando corresponde, el porcentaje mínimo.

Elegí diccionarios porque permiten acceder fácilmente a la información usando
el nombre de una columna o de un rol como clave. Para las columnas de interés
usé listas porque se pueden recorrer, filtrar y ordenar.

Un diccionario de diccionarios tiene ventaja sobre una lista de tuplas porque
permite buscar una columna por nombre sin recorrer toda la lista, y sobre un
conjunto porque conserva el tipo y la completitud de cada columna. Las listas
de columnas de cada rol mantienen un orden y son fáciles de recorrer.

Separé `ROLES` de la lógica del informe para poder modificar o agregar roles
sin tener que cambiar las funciones.

Parámetros con valor por defecto: `rol=None` en `generar_informe()` y
`mostrar_informe()` (informe general). Dentro de cada rol, `minimo` es
opcional y se lee con `get("minimo")`; si falta, no se filtra.

## Valores y pruebas

Elegí diferentes porcentajes de completitud para poder probar los umbrales.
Por ejemplo, `ITF` tiene 85 %, lo que permite comprobar que queda excluida
cuando un rol exige un mínimo del 90 %.

La función `generar_informe()` obtiene la configuración correspondiente al rol,
por lo que puede trabajar con diferentes columnas, criterios y umbrales.

Si no se indica un rol, el parámetro `rol` vale `None` y se genera el informe
general ordenado por completitud descendente.

## Nuevas columnas y validaciones

Si se agrega una nueva columna, solamente hay que incorporarla a `COLUMNAS`.
Si también se quiere mostrar para un rol, se agrega su nombre a las columnas
de interés de ese rol.

Si se recibe un criterio distinto de `nombre` o `completitud`, el programa
lo detecta y muestra un mensaje en lugar de intentar utilizar un criterio
desconocido.

Si se pide un rol que no existe, el programa muestra un mensaje y devuelve una
lista vacía en lugar de fallar.

Si el informe por defecto tuviera que corresponder a un rol, se podría cambiar
el valor por defecto de `rol` o seleccionar ese rol cuando `rol` sea `None`.

## Modificaciones de la evaluación

### 1. Rol economista

Agregué el rol `economista` con las columnas solicitadas, orden por nombre
ascendente y un mínimo de completitud del 90 %.

`ITF` (85 %) y `GDECCFR` (88 %) no alcanzan el mínimo de 90 %, por lo que
quedan excluidas. El informe resultante muestra 7 columnas ordenadas
alfabéticamente.

**Prueba realizada:** ejecuté `mostrar_informe("economista")` y verifiqué que
`ITF`, `GDECCFR` y `NIVEL_ED` no aparecen.

### 2. NIVEL_ED

Agregué `NIVEL_ED` como `int` con 88 % de completitud sin modificar los roles.

Por eso aparece en el informe general, que considera todas las columnas, pero
no aparece en los informes por rol, ya que cada rol utiliza solamente sus
columnas de interés.

**Prueba realizada:** `mostrar_informe()` incluye `NIVEL_ED`, mientras que los
informes de `docente`, `investigador`, `analista` y `economista` no la incluyen.

### 3. Uso de filter()

Utilicé `filter()` para conservar las columnas cuya completitud sea mayor o
igual al mínimo requerido.

Esto reemplaza un posible `for` con `if` y `append`, y expresa directamente
que se está filtrando una colección según una condición.

## Errores y resolución

Una dificultad fue diferenciar las columnas generales de las columnas de cada
rol. Lo resolví manteniendo `COLUMNAS` y `ROLES` separados.

También tuve que contemplar que no todos los roles tienen un porcentaje mínimo.
Para resolverlo uso `get("minimo")`, que devuelve `None` cuando ese valor no
está configurado.
