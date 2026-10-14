# Registro de Entorno y Conexión NoSQL - Unidad de Emprendimiento SENA

## 1. Versiones de Herramientas del Sistema
* **Sistema Operativo:** Windows (Entorno local con PowerShell / Virtualenv)
* **Python:** Python 3.14.6
* **Git:** git version 2.53.0.windows.1
* **MongoDB Shell (mongosh):** mongosh 2.13.0
* **Servidor MongoDB:** MongoDB Server (Instancia local ejecutándose como Servicio de Windows)

## 2. Comando de Conexión Segura
Se realizó la conexión al laboratorio local utilizando la cuenta técnica sin exponer contraseñas en texto plano en la línea de comandos:

```bash
mongosh "mongodb://127.0.0.1:27017/emprendimiento_sena_lab" \
  --username aprendiz_nosql \
  --authenticationDatabase emprendimiento_sena_lab