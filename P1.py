# import json

# texto = '{"codigo":"INI-001", "activa":True, "intereses":["Validar mercado",]}'

# # 1 Intenta cargar texto con json loads 
# # 2 Registra el error y corrige la sintaxis sin cambiar su intención 
# # 3 Muestra codigo activa y los tipos de ambos valores 
# # 4 Explica las correcciones realizadas 

import json

# 1. Intento inicial de carga (con errores sintácticos de JSON)
# texto_invalido = '{"codigo":"INI-001", "activa": True, "intereses":["Validar mercado",]}'
# Error capturado: json.decoder.JSONDecodeError 
# Motivo del error: En JSON los booleanos se escriben en minúscula (true) y no se permiten comas finales en listas.

# 2. Sintaxis corregida
texto_corregido = '{"codigo":"INI-001", "activa": true, "intereses":["Validar mercado"]}'

# Carga de JSON
datos = json.loads(texto_corregido)

# 3. Mostrar campos y tipos
codigo = datos["codigo"]
activa = datos["activa"]

print(f"Código: {codigo} (Tipo: {type(codigo).__name__})")
print(f"Activa: {activa} (Tipo: {type(activa).__name__})")

# 4. Explicación de las correcciones:
# - Se cambió True por true (booleano nativo en JSON).
# - Se eliminó la coma sobrante (trailing comma) al final de la lista "intereses".