import os
import re
import shutil

# Directorio de carpetas
source_directory_folders = r'Z:\Library\Reader'

# Función para listar carpetas en 'Z:\Library\Reader'
def listar_carpetas_en_folders():
    carpetas_en_folders = [foldername for foldername in os.listdir(source_directory_folders) if os.path.isdir(os.path.join(source_directory_folders, foldername))]
    return carpetas_en_folders

# Función para combinar carpetas con nombres comunes
def combinar_carpetas_con_nombres_comunes():
    carpetas_en_folders = listar_carpetas_en_folders()

    # Crear un diccionario para rastrear carpetas con nombres comunes
    carpetas_comunes = {}

    for carpeta in carpetas_en_folders:
        # Extraer palabras del nombre de la carpeta
        palabras = re.findall(r'\b\w+\b', carpeta)

        # Filtrar palabras que no son números
        palabras = [palabra for palabra in palabras if not palabra.isnumeric()]

        # Unir las palabras para crear el nombre común
        nombre_comun = ' '.join(palabras)

        if nombre_comun in carpetas_comunes:
            # Si ya existe una carpeta con este nombre común, mueve el contenido de la carpeta actual a la existente
            carpeta_existente = carpetas_comunes[nombre_comun]
            ruta_carpeta_actual = os.path.join(source_directory_folders, carpeta)
            ruta_carpeta_existente = os.path.join(source_directory_folders, carpeta_existente)

            for archivo in os.listdir(ruta_carpeta_actual):
                ruta_archivo = os.path.join(ruta_carpeta_actual, archivo)
                shutil.move(ruta_archivo, ruta_carpeta_existente)

            # Elimina la carpeta actual
            os.rmdir(ruta_carpeta_actual)
            print(f"Contenido de '{carpeta}' combinado con '{carpeta_existente}'.")

        else:
            carpetas_comunes[nombre_comun] = carpeta

# Menú
while True:
    print("Menú:")
    print("1. Listar carpetas en Reader")
    print("2. Combinar carpetas con nombres comunes")
    print("3. Salir")

    opcion = input("Selecciona una opción (1/2/3): ")

    if opcion == '1':
        print("Carpetas en eader:")
        carpetas_en_folders = listar_carpetas_en_folders()
        for carpeta in carpetas_en_folders:
            print(carpeta)
    elif opcion == '2':
        print("Combinando carpetas con nombres comunes...")
        combinar_carpetas_con_nombres_comunes()
        print("Combinación de carpetas completada.")
    elif opcion == '3':
        break
    else:
        print("Opción no válida. Por favor, selecciona una opción válida (1/2/3).")