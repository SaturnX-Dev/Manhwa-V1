import os

# Directorio de origen
source_directory = r'Y:\Folders'

# Caracteres y símbolos a eliminar y reemplazar
caracteres_a_eliminar = ["𓃠", "cbz", "cbr", "pdf", "[烌]", "烌", "💮", "(", ")", "[", "]", "烌", "龙"]
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

# Función para renombrar carpetas y fusionar carpetas con el mismo nombre
def renombrar_y_fusionar_carpetas(directorio):
    carpetas = set()

    def procesar_nombre(nombre):
        # Eliminar caracteres y símbolos no deseados
        for caracter in caracteres_a_eliminar:
            nombre = nombre.replace(caracter, '')

        for signo in signos_a_eliminar:
            nombre = nombre.replace(signo, '')

        for acento, reemplazo in acentos_a_reemplazar.items():
            nombre = nombre.replace(acento, reemplazo)

        # Eliminar guiones y números al final del nombre
        nombre = nombre.rstrip('_')
        while nombre[-1].isdigit() and nombre[-2:] != '__':
            nombre = nombre[:-1]

        # Capitalizar palabras
        nombre = ' '.join(word.capitalize() for word in nombre.split())

        return nombre

    for foldername in os.listdir(directorio):
        if os.path.isdir(os.path.join(directorio, foldername)):
            nuevo_nombre = procesar_nombre(foldername)

            if not nuevo_nombre.startswith(('+', '-')) and nuevo_nombre[:3].isdigit():
                nuevo_nombre = nuevo_nombre.lstrip('0123456789')

            vieja_ruta = os.path.join(directorio, foldername)
            nueva_ruta = os.path.join(directorio, nuevo_nombre)

            if nuevo_nombre in carpetas:
                nueva_ruta_existente = os.path.join(directorio, nuevo_nombre)
                for root, dirs, files in os.walk(vieja_ruta):
                    for file in files:
                        file_path = os.path.join(root, file)
                        new_file_path = os.path.join(nueva_ruta_existente, os.path.relpath(file_path, vieja_ruta))
                        os.makedirs(os.path.dirname(new_file_path), exist_ok=True)
                        os.rename(file_path, new_file_path)
                os.rmdir(vieja_ruta)
            else:
                carpetas.add(nuevo_nombre)
                os.rename(vieja_ruta, nueva_ruta)

# Menú
while True:
    print("Menú:")
    print("1. Listar carpetas en la carpeta")
    print("2. Renombrar y fusionar carpetas")
    print("3. Salir")

    opcion = input("Selecciona una opción (1/2/3): ")

    if opcion == '1':
        print("Carpetas en la carpeta:")
        listar_carpetas(source_directory)
    elif opcion == '2':
        print("Renombrando y fusionando carpetas en la carpeta...")
        renombrar_y_fusionar_carpetas(source_directory)
        print("Carpetas renombradas y fusionadas.")
    elif opcion == '3':
        break
    else:
        print("Opción no válida. Por favor, selecciona una opción válida (1/2/3).")