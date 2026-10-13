# Parte A. Diagnóstico teórico: 10 preguntas

## 1. ¿Qué representan una tabla, una fila y una clave primaria? Utiliza un ejemplo relacionado con las iniciativas de emprendimiento.

* **Tabla:** Organiza información en columnas (campos) y filas (registros) que almacenan información sobre una entidad específica.
* **Fila:** Representa una instancia o registro único dentro de una tabla. *Ejemplo:* La iniciativa `"INI-001"` con nombre `"EcoEmpaque"`.
* **Clave primaria (Primary Key):** Campo o conjunto de campos cuyo valor es único e irrepetible para cada fila, garantizando su identificación. También permite establecer relaciones con otras tablas a través de claves foráneas. *Ejemplo:* El campo `id` o `codigo` dentro de la tabla `iniciativas`.

## 2. ¿Para qué sirve una clave foránea? ¿Qué problema genera una iniciativa que referencia a un emprendedor inexistente?

* **Clave foránea:** Es un campo en una tabla que hace referencia a la clave primaria de otra tabla, estableciendo una relación de integridad referencial.
* **Problema de referencia inexistente:** Genera una *inconsistencia referencial* (datos huérfanos). Al intentar consultar el emprendedor de dicha iniciativa, las consultas tipo `JOIN` no encontrarán un registro relacionado, lo que puede dificultar el seguimiento de la responsabilidad del proyecto.

## 3. Explica qué devuelve `SELECT codigo FROM iniciativas WHERE sector = 'tecnologia';`. ¿Modifica los registros?

* **Devuelve:** Un conjunto de resultados con únicamente el campo `codigo` de todos los registros de la tabla `iniciativas` cuyo valor en la columna `sector` sea exactamente `'tecnologia'`.
* **¿Modifica registros?:** **No.** Las sentencias `SELECT` son exclusivamente de lectura y consulta.

## 4. Diferencia una lista y un diccionario en Python. ¿Qué estructura utilizarías para una iniciativa y para varias iniciativas?

* **Lista (`list`):** Colección ordenada cuyos elementos se identifican mediante índices numéricos. Ejemplo: `[elem1, elem2]`. Es útil para almacenar **varias iniciativas**.
* **Diccionario (`dict`):** Colección de pares clave-valor. Ejemplo: `{"clave": "valor"}`. Es útil para estructurar los atributos de **una iniciativa individual**.

## 5. ¿Son equivalentes `false` y `"false"` en JSON? Explica el tipo de cada valor.

**No son equivalentes.**

* `false`: Es un valor **booleano** nativo en JSON.
* `"false"`: Es una cadena de texto (**string**).

## 6. Diferencia un campo ausente, un campo con `null` y un campo con una cadena vacía. Propón un ejemplo.

* **Campo ausente:** La clave no existe en la estructura del documento u objeto.

  Ejemplo:

  ```json
  {
    "nombre": "EcoEmpaque"
  }
  ```

  En este caso, el campo `sector` no fue definido.

* **Campo con `null`:** La clave existe, pero su valor es explícitamente nulo o desconocido.

  Ejemplo:

  ```json
  {
    "nombre": "EcoEmpaque",
    "sector": null
  }
  ```

* **Cadena vacía (`""`):** La clave existe y tiene un valor de tipo texto, pero carece de caracteres.

  Ejemplo:

  ```json
  {
    "nombre": "EcoEmpaque",
    "sector": ""
  }
  ```

## 7. ¿Qué ventaja tiene una función que retorna datos frente a otra que únicamente los imprime?

Una función que retorna un valor permite reutilizar ese resultado en otras partes del programa, pasarlo a otras funciones o procesarlo mediante operaciones lógicas. En cambio, una función que solo imprime muestra la información en pantalla, pero no devuelve ese valor para utilizarlo directamente en el flujo de ejecución.

## 8. Si falla la lectura de un archivo JSON, ¿qué revisarías antes de cambiar el programa?

Revisaría los siguientes aspectos antes de modificar el código Python:

* **Sintaxis del archivo JSON:** Comprobaría el uso de comillas dobles, comas sobrantes o faltantes y corchetes o llaves mal cerrados.
* **Ruta del archivo:** Verificaría que la ruta especificada sea correcta y que el archivo exista en esa ubicación.
* **Permisos de acceso:** Comprobaría que el programa tenga permisos para leer el archivo.

## 9. ¿Qué información reconoces en `2026-10-06T13:00:00Z`? ¿Qué ambigüedades evita frente a `06/10/26 8:00`?

La fecha y hora `2026-10-06T13:00:00Z` contiene la siguiente información:

* **Año:** `2026`
* **Mes:** `10` (octubre).
* **Día:** `06`.
* **Hora:** `13:00:00`.
* **Zona horaria:** UTC, indicada por la letra `Z`.

**Ambigüedades que evita:**

* Elimina la confusión entre el orden del día y el mes.
* Especifica el año completo, evitando dudas sobre el siglo.
* Define la zona horaria, permitiendo interpretar correctamente el momento del evento.

En cambio, `06/10/26 8:00` puede interpretarse de distintas maneras según el formato de fecha y la zona horaria utilizada.

## 10. Se publicó por error una contraseña en Git. ¿Qué acciones propondrías? ¿Es suficiente borrarla del archivo actual?

Propondría las siguientes acciones:

1. **Cambiar inmediatamente la contraseña expuesta** en el servicio o sistema correspondiente para impedir que siga siendo utilizada por terceros.
2. **Eliminar el secreto del historial de Git:** No basta con borrarlo del archivo actual, ya que puede permanecer en commits anteriores. Se pueden utilizar herramientas como `git-filter-repo` o BFG Repo-Cleaner para limpiar el historial.
3. **Revisar el acceso al repositorio:** Si otras personas pudieron acceder a la contraseña, se deben evaluar los riesgos y revisar los registros de acceso cuando corresponda.
4. **Añadir los archivos sensibles a `.gitignore`:** Esto ayuda a evitar que se incluyan accidentalmente en futuros commits. Sin embargo, `.gitignore` no elimina archivos que ya están siendo rastreados por Git.
5. **Utilizar variables de entorno o un gestor de secretos:** Así se evita almacenar contraseñas directamente en el código fuente.

**Conclusión:** Borrar la contraseña del archivo actual no es suficiente. Es necesario cambiar la credencial expuesta y gestionar su eliminación del historial del repositorio.

# Parte B. Diagnóstico práctico

## Autoevaluacion: Por mi parte necesitaria recordar operadores y funciones de SQL y python para trabajar con bases de datos. 

## Parte A3.

# 1. Definición de las reglas del negocio del caso

* **Identificadores únicos:** Cada emprendedor, iniciativa y asesoría cuenta con un código único e irrepetible. Ejemplos: `INI-001`, `ASE-DEMO-001`.

* **Relación emprendedor-iniciativa:** Cada iniciativa tiene un único emprendedor responsable existente al momento del registro. Una persona puede representar y liderar múltiples iniciativas.

* **Vínculo de asesorías:** Cada asesoría se asocia obligatoriamente con una iniciativa existente y registra el código ficticio del asesor que la atiende.

* **Sectores y etapas válidas:**

  * Sectores permitidos: `tecnologia`, `alimentos`, `economia_circular`.
  * Etapas didácticas permitidas: `idea`, `validacion`, `puesta_en_marcha`.
  * Estas convenciones corresponden a la simulación didáctica.

* **Estados operativos:**

  * Estado de iniciativa: `activa` o `archivada`.
  * Estado de asesoría: `programada`, `realizada` o `cancelada`.

* **Gestión temporal de asesorías:** Se registra obligatoriamente la `fecha_programada`. Cuando la sesión se lleva a cabo, se registra la `fecha_realizacion`. Si hay reprogramaciones, la fecha real puede diferir de la programada, conservando la historia real y sin sobrescribir el registro original.

* **Control de agenda de asesores:** No se deben programar simultáneamente dos asesorías para el mismo asesor en una misma franja horaria definida para el laboratorio.

* **Impacto del archivo:** Archivar una iniciativa (`estado: "archivada"`) no elimina automáticamente ni oculta su historial de asesorías previas.

---

# 2. Definición de las seis consultas previstas (Q01–Q06)

## Q01. Iniciativas activas por sector y etapa didáctica

* **Actor:** Gestor o instructor de la unidad.
* **Filtros:**

  * `estado: "activa"`.
  * Sector específico (ejemplo: `"tecnologia"`).
  * Etapa didáctica (ejemplo: `"validacion"`).
* **Campos de salida:**

  * Código de iniciativa.
  * Nombre de la iniciativa.
  * Nombre o alias del emprendedor responsable.
* **Orden:** Por código de iniciativa de forma ascendente.
* **Frecuencia estimada:** Alta (diaria durante el comité de seguimiento).

## Q02. Detalle de una iniciativa con su propuesta de valor y atributos específicos

* **Actor:** Emprendedor o asesor.
* **Filtros:** Código de iniciativa único (ejemplo: `codigo: "INI-001"`).
* **Campos de salida:**

  * Todos los campos generales.
  * Atributos específicos correspondientes a su sector (ejemplo: canal de venta para alimentos o plataforma de entrega para software).
* **Orden:** No aplica (documento único).
* **Frecuencia estimada:** Media (por cada sesión de asesoría).

## Q03. Iniciativas de un emprendedor responsable por estado

* **Actor:** Emprendedor o administrador.
* **Filtros:**

  * Alias o identificador del emprendedor.
  * Estado de la iniciativa: `activa` o `archivada`.
* **Campos de salida:**

  * Código de iniciativa.
  * Nombre de la iniciativa.
  * Sector.
  * Etapa didáctica.
* **Orden:** Por fecha o código de iniciativa descendente.
* **Frecuencia estimada:** Baja (semanal o mensual).

## Q04. Asesorías programadas pendientes por rango de fechas y modalidad

* **Actor:** Asesor o coordinador de agenda.
* **Filtros:**

  * `estado: "programada"`.
  * Modalidad: `"virtual"` o `"presencial"`.
  * Rango de `fecha_programada`.
* **Campos de salida:**

  * ID de asesoría.
  * Fecha programada.
  * Código y nombre de la iniciativa.
  * Temas a tratar.
* **Orden:** Cronológico ascendente por `fecha_programada`.
* **Frecuencia estimada:** Alta (diaria).

## Q05. Historial de asesorías de una iniciativa

* **Actor:** Asesor o emprendedor.
* **Filtros:** Código de iniciativa de referencia.
* **Campos de salida:**

  * ID de asesoría.
  * Estado.
  * Temas tratados.
  * Fecha programada.
  * Fecha de realización.
  * Código del asesor.
* **Orden:** Cronológico descendente por fecha de asesoría.
* **Frecuencia estimada:** Media.

## Q06. Cantidad de asesorías realizadas por sector de iniciativa y mes

* **Actor:** Director de la unidad de emprendimiento (para reportes estadísticos).
* **Filtros:**

  * Estado de asesoría: `realizada`.
  * Rango de meses y años.
* **Campos de salida:**

  * Sector de la iniciativa.
  * Mes del reporte.
  * Conteo total de asesorías.
* **Orden:** Agrupado por sector y mes.
* **Frecuencia estimada:** Baja (mensual o trimestral).

**Nota de diseño:** Se debe decidir si el sector consultado corresponde al valor actual de la iniciativa o al histórico registrado en el momento en que se prestó la asesoría.

### 3. Preguntas clave para la persona responsable de la unidad y riesgos identificados

#### Preguntas para el responsable

1. ¿Una iniciativa archivada puede reactivarse posteriormente bajo el mismo código o requiere la creación de una nueva iniciativa?

2. ¿Los informes mensuales de asesorías requieren conservar el sector histórico de la iniciativa, aunque esta haya cambiado de sector con el tiempo?

#### Riesgo identificado

* **Inconsistencia por concurrencia de agendas:** Existe el riesgo de que dos asesores diferentes programen simultáneamente una asesoría para el mismo asesor en una franja horaria idéntica, antes de que el motor de base de datos valide las restricciones de índice único o transaccionalidad.

  Este mecanismo de control transaccional formal se abordará en fases avanzadas del curso.
