# Análisis de Modelos NoSQL, Reglas y Consultas - Unidad de Emprendimiento SENA

## 1. Matriz Comparativa de Escenarios y Justificación

| Caso | Modelo propuesto | Razón vinculada a una consulta | Límite o costo | Alternativa |
| :--- | :--- | :--- | :--- | :--- |
| **Iniciativas de varios sectores** (tecnología, alimentos, economía circular con atributos variables)[cite: 1] | **Documental** (MongoDB)[cite: 1] | Permite almacenar atributos dinámicos y específicos por sector en un mismo documento JSON/BSON sin alterar esquemas rígidos, facilitando consultas de la iniciativa completa (`Q02`)[cite: 1]. | Si no se definen contratos o esquemas de validación claros en los campos comunes, se puede perder la consistencia de los datos[cite: 1]. | **SQL (Relacional):** Se usaría si los sectores comparten más del 90% de los atributos y se requiere una normalización estricta mediante tablas EAV o múltiples tablas hijas[cite: 1]. |
| **Sesiones temporales** (Acceso a un portal que expiran)[cite: 1] | **Clave-Valor** (Redis)[cite: 1] | Optimiza la recuperación ultrarrápida de tokens de sesión y tokens de autenticación mediante una clave directa (`key-value`) con expiración automática (`TTL`)[cite: 1]. | No permite realizar consultas complejas, filtros cruzados, agregaciones o búsquedas por múltiples atributos secundarios[cite: 1]. | **SQL (Relacional):** Una tabla transaccional con un campo de fecha de expiración, requiriendo un proceso periódico de limpieza (`cron job`) para eliminar registros vencidos[cite: 1]. |
| **Recorridos de relaciones** (Red de emprendedores, mentores y habilidades)[cite: 1] | **Grafos** (Neo4j)[cite: 1] | Permite modelar nodos y relaciones directas para consultar caminos cortos, conexiones de mentoría e influencias de forma eficiente mediante algoritmos de grafos[cite: 1]. | Alto consumo de memoria RAM y curva de aprendizaje más pronunciada para consultas operativas tradicionales[cite: 1]. | **SQL (Relacional):** Mediante tablas intermedias de muchos a muchos (`n:m`), aunque las consultas de múltiples saltos (`JOINs` recursivos) se vuelven muy costosas y lentas al escalar[cite: 1]. |
| **Lecturas por dispositivo/periodo** (Iniciativa agroindustrial a gran escala con sensores)[cite: 1] | **Familias de Columnas** (Cassandra)[cite: 1] | Diseñado para escrituras masivas distribuidas y consultas optimizadas por intervalos de tiempo particionados por dispositivo[cite: 1]. | Flexibilidad de consultas muy limitada; requiere conocer de antemano el patrón exacto de consulta (Primary Key / Clustering Key)[cite: 1]. | **SQL (Relacional):** Bases de datos relacionales particionadas, aunque experimentan cuellos de botella severos en inserciones masivas concurrentes de telemetría[cite: 1]. |

### Justificación Detallada Basada en Consultas y Límites
* **Iniciativas de Varios Sectores (Documental):** Responde de forma óptima a la consulta **Q02** (*Detalle de una iniciativa con su propuesta de valor y atributos específicos*) agrupando campos heterogéneos en una sola lectura nativa[cite: 1]. Su límite es el riesgo de esquemas descontrolados si no se establecen reglas de validación comunes[cite: 1].
* **Sesiones Temporales (Clave-Valor):** Satisface la recuperación de tokens con velocidad máxima gracias a claves directas, aunque carece de capacidades para reportes analíticos complejos[cite: 1].
* **Recorridos y Relaciones (Grafos):** Resuelve interconexiones complejas entre mentores, habilidades y emprendedores de manera eficiente frente al alto costo de `JOINs` recursivos relacionales[cite: 1].
* **Lecturas por Dispositivo (Familias de Columnas):** Garantiza escrituras masivas distribuidas para telemetría agroindustrial, exigiendo un diseño estricto y predefinido de las llaves de partición[cite: 1].

---

## 2. Reglas del Negocio del Caso
* **Identificadores únicos:** Cada emprendedor, iniciativa y asesoría cuenta con un código único e irrepetible (ej. `INI-001`, `ASE-DEMO-001`)[cite: 1].
* **Relación Emprendedor-Iniciativa:** Cada iniciativa tiene un único emprendedor responsable existente; una persona puede representar y liderar múltiples iniciativas[cite: 1].
* **Vínculo de Asesorías:** Cada asesoría se vincula obligatoriamente con una iniciativa existente y registra el código ficticio del asesor que la atiende[cite: 1].
* **Sectores y Etapas válidas:** Sectores permitidos: `tecnologia`, `alimentos`, `economia_circular`. Etapas didácticas: `idea`, `validacion`, `puesta_en_marcha` (convenciones de la simulación didáctica)[cite: 1].
* **Estados operativos:** Estado de iniciativa: `activa` o `archivada`. Estado de asesoría: `programada`, `realizada` o `cancelada`[cite: 1].
* **Gestión temporal de asesorías:** Se registra obligatoriamente la `fecha_programada` y, al realizarse la sesión, la `fecha_realizacion`, conservando la historia real sin sobrescribir registros[cite: 1].
* **Control de agenda:** No programar de forma simultánea dos asesorías para el mismo asesor en la misma franja horaria definida para el laboratorio[cite: 1].
* **Impacto del archivo:** Archivar una iniciativa no elimina automáticamente ni oculta su historial de asesorías previas[cite: 1].

---

## 3. Definición de las Seis Consultas Previstas (Q01 – Q06)

### Q01: Iniciativas activas por sector y etapa didáctica[cite: 1]
* **Actor:** Gestor o instructor de la unidad[cite: 1].
* **Filtros:** `estado: "activa"`, sector específico y etapa didáctica[cite: 1].
* **Campos de salida:** Código de iniciativa, nombre, alias del emprendedor responsable[cite: 1].
* **Orden:** Por código de iniciativa ascendente[cite: 1].
* **Frecuencia estimada:** Alta (diaria)[cite: 1].

### Q02: Detalle de una iniciativa con su propuesta de valor y atributos específicos[cite: 1]
* **Actor:** Emprendedor o asesor[cite: 1].
* **Filtros:** Código de iniciativa único (`codigo: "INI-001"`)[cite: 1].
* **Campos de salida:** Datos generales y atributos específicos según su sector (ej. canal de venta o plataforma digital)[cite: 1].
* **Orden:** N/A (documento único)[cite: 1].
* **Frecuencia estimada:** Media[cite: 1].

### Q03: Iniciativas de un emprendedor responsable por estado[cite: 1]
* **Actor:** Emprendedor o administrador[cite: 1].
* **Filtros:** Alias del emprendedor y estado (`activa` / `archivada`)[cite: 1].
* **Campos de salida:** Código, nombre, sector y etapa de la iniciativa[cite: 1].
* **Orden:** Por fecha o código de iniciativa descendente[cite: 1].
* **Frecuencia estimada:** Baja (semanal/mensual)[cite: 1].

### Q04: Asesorías programadas pendientes por rango de fechas y modalidad[cite: 1]
* **Actor:** Asesor o coordinador de agenda[cite: 1].
* **Filtros:** `estado: "programada"`, modalidad (`"virtual"` o `"presencial"`), y rango de `fecha_programada`[cite: 1].
* **Campos de salida:** ID de asesoría, fecha programada, código/nombre de iniciativa, temas[cite: 1].
* **Orden:** Cronológico ascendente por fecha programada[cite: 1].
* **Frecuencia estimada:** Alta (diaria)[cite: 1].

### Q05: Historial de asesorías de una iniciativa[cite: 1]
* **Actor:** Asesor o emprendedor[cite: 1].
* **Filtros:** Código de iniciativa de referencia[cite: 1].
* **Campos de salida:** ID de asesoría, estado, temas, fecha programada, fecha de realización y código del asesor[cite: 1].
* **Orden:** Cronológico descendente por fecha[cite: 1].
* **Frecuencia estimada:** Media[cite: 1].

### Q06: Cantidad de asesorías realizadas por sector de iniciativa y mes[cite: 1]
* **Actor:** Director de la unidad de emprendimiento (para reportes estadísticos)[cite: 1].
* **Filtros:** Estado `realizada` y rango de meses/años[cite: 1].
* **Campos de salida:** Sector de la iniciativa, mes del reporte y conteo total de asesorías[cite: 1].
* **Orden:** Agrupado por sector y mes[cite: 1].
* **Frecuencia estimada:** Baja (mensual/trimestral)[cite: 1].
* **Nota de diseño:** Se debe decidir si el sector consultado corresponde al valor actual de la iniciativa o al histórico registrado al momento de la asesoría[cite: 1].

---

## 4. Preguntas Clave al Responsable y Riesgo Identificado

### Preguntas para el responsable
1. ¿Una iniciativa archivada puede reactivarse bajo el mismo código o requiere crear una nueva?[cite: 1]
2. ¿Los informes mensuales de asesorías requieren conservar el sector histórico de la iniciativa aunque esta haya cambiado de sector con el tiempo?[cite: 1]

### Riesgo identificado
* **Inconsistencia por concurrencia de agendas:** Que dos asesores diferentes programen de manera simultánea una asesoría para el mismo asesor en una franja horaria idéntica antes de que el motor valide restricciones de índice único (mecanismo transaccional formal que se abordará más adelante en el curso)[cite: 1].