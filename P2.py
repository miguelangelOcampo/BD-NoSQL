# Completa la función y propone dos pruebas: una con resultados y otra sin resultados. 
# Explica cómo tratas el campo ausente y por qué no debes confundir una cadena con un booleano. 
# "pendiente" se utiliza en este diagnóstico; no obliga a conservar ese campo derivado en el modelo final; 
# representa necesidad de seguimiento únicamente en este diagnóstico.

# iniciativas = [
#     {"codigo": "INI-001", "sector": "tecnologia", "pendiente": True},
#     {"codigo": "INI-002", "sector": "alimentos", "pendiente": True},
#     {"codigo": "INI-003", "sector": "tecnologia", "pendiente": False},
#     {"codigo": "INI-004", "sector": "tecnologia"}
# ]
# def seleccionar_pendientes(registros, sector):
#     # Retorna códigos del sector indicado con pendiente exactamente True.
#     # No modifiques la lista recibida. Define qué ocurre si falta el campo (pendiente).
#     

#============================================================================

#* Sera nuestro registro
iniciativas = [
    {"codigo": "INI-001", "sector": "tecnologia", "pendiente": True},
    {"codigo": "INI-002", "sector": "alimentos", "pendiente": True},
    {"codigo": "INI-003", "sector": "tecnologia", "pendiente": False},
    {"codigo": "INI-004", "sector": "tecnologia"}
]

#* Funcion para devolver un codigo en base a un sector y que el campo pendiente sea True en un registro
def seleccionar_pendientes(registros, sector_buscado):
    codigos_filtrados = [] #Lista para almacenar los codigos filtrados
    for reg in registros: #Bucle for each para recorrer registros uno por uno
        # Se verifica que la clave 'pendiente' exista, que su valor sea booleano y exactamente True
        if reg.get("sector") == sector_buscado and reg.get("pendiente") is True:
            codigos_filtrados.append(reg["codigo"]) #agregamos a la lista lo que necesitamos en este caso el codigo
    return codigos_filtrados #retornamos solo la lista

# Pruebas
print("Prueba 1 (con resultados):", seleccionar_pendientes(iniciativas, "tecnologia")) # Esperado: ['INI-001']
print("Prueba 2 (sin resultados):", seleccionar_pendientes(iniciativas, "economia_circular")) # Esperado: []

# Explicación del tratamiento de campo ausente:
# Se utiliza el método .get("pendiente"), el cual devuelve None si el campo no existe. 
# La comparación estricta `is True` evita clasificar un valor ausente (None) o una cadena "true" como un valor booleano True.