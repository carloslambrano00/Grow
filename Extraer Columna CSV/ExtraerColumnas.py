# Importa la biblioteca 'csv' para trabajar con archivos CSV.
import csv

# Define la ruta del archivo de entrada y salida.
ruta_entrada = 'AQUI DEBEN ESCRIBIR LA RUTA DONDE ESTA EL ARCHIVO'
ruta_salida = 'AQUI DEBEN ESCRIBIR LA RUTA DONDE VA CREARSE EL NUEVO ARCHIVO CON LAS COLUMNAS EXTRADIDAS'

# Lista de nombres de las columnas que se desean extraer del archivo de entrada.
# AQUI COLOCAN EL NOMBRE DE LAS COLUMNAS QUE QUIEREN EXTRAER DEL ARCHIVO CSV
columnas_deseadas = ['Movie Name', 'Year of Release', 'Movie Rating', 'Votes']

# Lista para almacenar las filas extraídas del archivo de entrada.
filas_extraidas = []

# Abre el archivo de entrada en modo lectura y especifica la codificación UTF-8.
with open(ruta_entrada, 'r', encoding='utf-8') as archivo_entrada:

    # Crea un objeto lector de CSV.
    lector = csv.DictReader(archivo_entrada)

    # Itera a través de las filas del archivo de entrada.
    for fila in lector:
        # Crea un nuevo diccionario con solo las columnas deseadas y lo agrega a la lista.
        fila_extraida = {columna: fila[columna] for columna in columnas_deseadas}
        filas_extraidas.append(fila_extraida)

# Abre el archivo de salida en modo escritura y especifica que no se agregarán líneas en blanco.
with open(ruta_salida, 'w', newline='') as archivo_salida:

    # Encabezado del archivo de salida, que son las columnas deseadas.
    encabezado = columnas_deseadas

    # Crea un objeto escritor de CSV.
    escritor = csv.DictWriter(archivo_salida, fieldnames=encabezado)

    # Escribe el encabezado en el archivo de salida.
    escritor.writeheader()

    # Itera a través de las filas extraídas y las escribe en el archivo de salida.
    for fila in filas_extraidas:
        escritor.writerow(fila)

# Imprime un mensaje en la consola para indicar que se ha creado el archivo con los datos deseados.
print('Ya se creó el archivo con los datos deseados')



