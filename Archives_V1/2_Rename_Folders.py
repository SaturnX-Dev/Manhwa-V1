import os

# Directorio de origen
source_directory = r'Y:\Folders'

# Caracteres y símbolos a eliminar y reemplazar
caracteres_a_eliminar = ["𓃠", "cbz", "cbr", "pdf", "[烌]", "烌", "💮", "(", ")", "[", "]", "烏", "龙"]
signos_a_eliminar = ["?", "¡", "¿", "!", "-", "_"]
acentos_a_reemplazar = {
    "á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u",
    "Á": "A", "É": "E", "Í": "I", "Ó": "O", "Ú": "U"
}

# Función para listar las carpetas
def listar_carpetas(directorio):
    for foldername in os.listdir(directorio):
        if os.path.isdir(os.path.join(directorio, foldername)):
            print(foldername)

# Función para renombrar las carpetas
def renombrar_carpetas(directorio):
    for foldername in os.listdir(directorio):
        if os.path.isdir(os.path.join(directorio, foldername)):
            nuevo_nombre = foldername

            # Eliminar caracteres y símbolos no deseados
            for caracter in caracteres_a_eliminar:
                nuevo_nombre = nuevo_nombre.replace(caracter, '')

            # Reemplazar signos
            for signo in signos_a_eliminar:
                nuevo_nombre = nuevo_nombre.replace(signo, '')

            # Reemplazar acentos
            for acento, reemplazo in acentos_a_reemplazar.items():
                nuevo_nombre = nuevo_nombre.replace(acento, reemplazo)

            # Eliminar números
            nuevo_nombre = ''.join(filter(lambda x: not x.isdigit(), nuevo_nombre))

            # Capitalizar palabras
            nuevo_nombre = ' '.join(word.capitalize() for word in nuevo_nombre.split())

            # Ruta completa de las carpetas
            vieja_ruta = os.path.join(directorio, foldername)
            nueva_ruta = os.path.join(directorio, nuevo_nombre)

            # Renombrar la carpeta, evitando duplicados
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
    print("1. Listar carpetas en la carpeta")
    print("2. Renombrar carpetas en la carpeta")
    print("3. Salir")
    
    opcion = input("Selecciona una opción (1/2/3): ")
    
    if opcion == '1':
        print("Carpetas en la carpeta:")
        listar_carpetas(source_directory)
    elif opcion == '2':
        print("Renombrando carpetas en la carpeta...")
        renombrar_carpetas(source_directory)
        print("Carpetas renombradas.")
    elif opcion == '3':
        break
    else:
        print("Opción no válida. Por favor, selecciona una opción válida (1/2/3).")