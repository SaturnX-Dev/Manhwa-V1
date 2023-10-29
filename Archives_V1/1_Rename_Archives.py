import os
import re

# Directorio de origen
source_directory = r'Y:\Archives'

# Caracteres y símbolos a eliminar y reemplazar
caracteres_a_eliminar = ["𓃠", "[烌]", "烌", "💮", "(", ")", "[", "]", "烏", "龙"]
signos_a_eliminar = ["?", "¡", "¿", "!", "-", "_"]
acentos_a_reemplazar = {
    "á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u",
    "Á": "A", "É": "E", "Í": "I", "Ó": "O", "Ú": "U"
}

# Función para listar los archivos
def listar_archivos(directorio):
    for filename in os.listdir(directorio):
        if os.path.isfile(os.path.join(directorio, filename)):
            print(filename)

# Función para renombrar los archivos
def renombrar_archivos(directorio):
    for filename in os.listdir(directorio):
        if os.path.isfile(os.path.join(directorio, filename)):
            nuevo_nombre = filename

            # Eliminar caracteres y símbolos no deseados
            for caracter in caracteres_a_eliminar:
                nuevo_nombre = nuevo_nombre.replace(caracter, '')

            # Reemplazar signos
            for signo in signos_a_eliminar:
                nuevo_nombre = nuevo_nombre.replace(signo, '')

            # Reemplazar acentos
            for acento, reemplazo in acentos_a_reemplazar.items():
                nuevo_nombre = nuevo_nombre.replace(acento, reemplazo)

            # Capitalizar palabras
            nuevo_nombre = ' '.join(word.capitalize() for word in nuevo_nombre.split())

            # Ruta completa de los archivos
            vieja_ruta = os.path.join(directorio, filename)
            nueva_ruta = os.path.join(directorio, nuevo_nombre)

            # Renombrar el archivo, evitando duplicados
            if nueva_ruta != vieja_ruta:
                i = 1
                while os.path.exists(nueva_ruta):
                    base, extension = os.path.splitext(nuevo_nombre)
                    nuevo_nombre = f"{base}_{i}{extension}"
                    nueva_ruta = os.path.join(directorio, nuevo_nombre)
                    i += 1
                os.rename(vieja_ruta, nueva_ruta)

# Menú
while True:
    print("Menú:")
    print("1. Listar archivos en la carpeta")
    print("2. Renombrar archivos en la carpeta")
    print("3. Salir")
    
    opcion = input("Selecciona una opción (1/2/3): ")
    
    if opcion == '1':
        print("Archivos en la carpeta:")
        listar_archivos(source_directory)
    elif opcion == '2':
        print("Renombrando archivos en la carpeta...")
        renombrar_archivos(source_directory)
        print("Archivos renombrados.")
    elif opcion == '3':
        break
    else:
        print("Opción no válida. Por favor, selecciona una opción válida (1/2/3).")