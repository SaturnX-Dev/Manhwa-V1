import os
import shutil

# Directorio de origen
source_directory = r'Z:\Library\Reader'

# Caracteres y símbolos a eliminar y reemplazar
caracteres_a_eliminar = ["𓃠", "[烌]", "烌", "💮", "(", ")", "[", "]", "烏", "龙", "×͜×", "❬", "❭"]
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
    try:
        carpetas_procesadas = {}

        def procesar_nombre(nombre):
            # Eliminar caracteres y símbolos no deseados
            for caracter in caracteres_a_eliminar:
                nombre = nombre.replace(caracter, '')
            for signo in signos_a_eliminar:
                nombre = nombre.replace(signo, '')
            for acento, reemplazo in acentos_a_reemplazar.items():
                nombre = nombre.replace(acento, reemplazo)

            # Eliminar guiones y números al principio y al final del nombre
            nombre = nombre.lstrip('_')
            while nombre and nombre[0].isdigit():
                nombre = nombre[1:]

            nombre = nombre.rstrip('_')
            while nombre and nombre[-1].isdigit() and nombre[-2:] != '__':
                nombre = nombre[:-1]

            # Capitalizar palabras
            nombre = ' '.join(word.capitalize() for word in nombre.split())

            return nombre.strip()

        for foldername in os.listdir(directorio):
            if os.path.isdir(os.path.join(directorio, foldername)):
                nuevo_nombre = procesar_nombre(foldername)

                if nuevo_nombre in carpetas_procesadas:
                    ruta_existente = carpetas_procesadas[nuevo_nombre]
                    ruta_actual = os.path.join(directorio, foldername)

                    # Mover archivos a la carpeta existente
                    for archivo in os.listdir(ruta_actual):
                        shutil.move(os.path.join(ruta_actual, archivo), ruta_existente)

                    # Eliminar la carpeta vacía
                    os.rmdir(ruta_actual)
                else:
                    ruta_nueva = os.path.join(directorio, nuevo_nombre)
                    # Renombrar solo si el nuevo nombre es diferente
                    if ruta_nueva.lower() != os.path.join(directorio, foldername).lower():
                        os.rename(os.path.join(directorio, foldername), ruta_nueva)
                    carpetas_procesadas[nuevo_nombre] = ruta_nueva

        logging.info("Carpetas renombradas y fusionadas.")

    except Exception as e:
        logging.error(f"Error durante el procesamiento: {e}")

# Menú de usuario
while True:
    print("Menú:")
    print("1. Listar carpetas en la carpeta")
    print("2. Renombrar y fusionar carpetas")
    print("3. Mostrar opciones del menú")
    print("4. Salir")

    opcion = input("Selecciona una opción (1/2/3/4): ")

    if opcion == '1':
        print("Carpetas en la carpeta:")
        listar_carpetas(source_directory)
    elif opcion == '2':
        print("Renombrando y fusionando carpetas en la carpeta...")
        renombrar_y_fusionar_carpetas(source_directory)
    elif opcion == '3':
        print("Menú:")
        print("1. Listar carpetas en la carpeta")
        print("2. Renombrar y fusionar carpetas")
        print("3. Mostrar opciones del menú")
        print("4. Salir")
    elif opcion == '4':
        print("Saliendo...")
        break
    else:
        print("Opción no válida. Por favor, selecciona una opción válida (1/2/3/4).")