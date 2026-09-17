# Contrato de datos y transformaciones para la consultoría

Versión 2.0. Corte analítico: años completos hasta 2024. Zona de referencia: Colombia, día de 24 horas. Los archivos son copias inmutables del material recibido, atribuido a la API pública de XM. No se dispone del script original de descarga ni de todos los metadatos de consulta; la validez externa de cada extracción debe verificarse antes de un uso profesional. Los controles nuevos verifican esquema, aritmética y cobertura local, no certifican el origen.

| Archivo/entrada | Transformación nueva | Variable resultante | Decisión y alerta |
|---|---|---|---|
| `xm_precio_bolsa_raw.csv`, 24 columnas horarias | Conversión numérica estricta, media de 24 cotizaciones/día y media en años completos | Precio medio nominal COP/kWh, sin ponderar por energía | Describe cotizaciones. No representa precio capturado, tarifa final ni costo social |
| `xm_generacion_raw.csv`, energía horaria kWh | Sumar 24 horas y días completos; dividir por 1.000.000 | Energía anual GWh | Describe generación del universo reportado. Una suma no mide capacidad instalada |
| Energía anual y días válidos | GWh × 1000 / (días × 24) | Potencia media MW | No es disponibilidad ni margen de reserva; se usa duración de calendario, incluyendo bisiestos |
| `xm_demanda_max_raw.csv`, `Value` kW | Máximo anual y división por 1000 una vez | Demanda máxima MW | No conservar el nombre heredado MW de un CSV que contenía kW |
| `xm_demanda_comercial_raw.csv` | Suma de columnas horarias, ignorando la suma precalculada heredada como fuente de verdad | Demanda comercial GWh | Comparar universos con generación, pérdidas e intercambios antes de interpretar diferencias |
| Generación menos demanda comercial | Unión por año validada uno-a-uno y resta | Diferencia contable GWh | No nombrarla déficit ni reserva; requiere reconciliación de fronteras |
| `xm_embalses_pct_raw.csv`, fracción 0–1 | Validar rango y multiplicar por 100 | Indicador de embalse % | No es MWh disponibles. Se necesita denominador y metodología para otra conversión |
| Precio/embalse mensual | Promedios separados por mes y unión de meses comunes | Asociación exploratoria | Correlación no identifica causalidad; precios nominales, regímenes y estacionalidad siguen presentes |
| `xm_capacidad_por_recurso.csv` | Renombrar máximo observado, retirar factor de planta heredado y conservar `SIN_CLASIFICAR` | Máxima producción horaria observada MW y producción 2024 GWh | No es CEN. No sumar máximos no coincidentes como capacidad firme nacional |
| `CompanyCode` y producción por recurso | Agrupar conservando `SIN_IDENTIFICAR` | Participaciones del extracto observado | Código de agente no equivale automáticamente a grupo económico; universo incompleto |
| Precio horario y producción horaria alineada | Suma de precio × energía / suma energía | Precio capturado COP/kWh | Requiere perfil propio validado; la práctica usa perfiles sintéticos identificados |

## Cobertura y versiones

Los extractos de precio llegan a julio de 2025; generación, demanda y embalses llegan a agosto de 2025. No se mezclan esos cortes para calcular crecimiento anual. `cobertura()` muestra días observados, días calendario y condición de completitud; las funciones de resumen excluyen años incompletos por defecto.

El catálogo de plantas tiene 2.293 registros y el extracto de producción por recurso 364 filas. El archivo auxiliar `test_recursos.csv` está fechado en 2026; no se usa como censo de plantas operativas de 2024. El cruce heredado de atributos puede contener conocimiento posterior. `operación` o `registro` tampoco certifican por sí solos capacidad o energía de un año histórico.

El total directo del proxy y el agrupado deben coincidir incluyendo la categoría sin clasificar. Ningún control rellena silenciosamente filas faltantes. Si una fecha se duplica, falta una hora o aparece una magnitud no finita, se detiene el cálculo para investigar; no se interpreta una media parcial como día completo.

## Cómo incorporar una nueva fuente

Registrar entidad, URL e identificador del indicador, descripción, unidad original, fecha de consulta, período, filtros, paginación y licencia/condiciones de uso. Guardar el extracto con checksum; conservar el script de obtención y la transformación como pasos separados. Validar una cifra agregada contra una publicación oficial comparable; explicar discrepancias de corte antes de sustituir datos.

Para convertir precios a COP constantes falta una serie de deflactor explícita. Para CEN falta capacidad declarada por recurso y fecha. Para ENFICC/OEF faltan metodología y asignaciones aplicables. Para poder de mercado faltan definición de mercado, grupos y condiciones de oferta. Estas brechas se registran como información necesaria, no se cubren con una constante pedagógica presentada como medición.
