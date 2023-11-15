import os
import shutil
from difflib import SequenceMatcher

# Directorio de origen
source_directory = r'Z:\Library\Reader'

# Caracteres y símbolos a eliminar y reemplazar
caracteres_a_eliminar = ["𓃠", "[烌]", "烌", "💮", "(", ")", "[", "]", "烏", "龙", "×͜×", "❬", "❭"]
signos_a_eliminar = ["?", "¡", "¿", "!", "-", "_"]
acentos_a_reemplazar = {
    "á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u",
    "Á": "A", "É": "E", "Í": "I", "Ó": "O", "Ú": "U"
}

def limpiar_nombre(nombre):
    # Eliminar caracteres no deseados
    for caracter in caracteres_a_eliminar:
        nombre = nombre.replace(caracter, "")

    # Eliminar signos de puntuación
    for signo in signos_a_eliminar:
        nombre = nombre.replace(signo, "")

    # Reemplazar acentos
    for acento, sin_acento in acentos_a_reemplazar.items():
        nombre = nombre.replace(acento, sin_acento)

    return nombre

def similaridad_nombres(nombre1, nombre2):
    return SequenceMatcher(None, nombre1, nombre2).ratio()

def procesar_carpetas(directorio):
    carpetas = os.listdir(directorio)

    for i, carpeta1 in enumerate(carpetas):
        # Construir la ruta completa de la carpeta
        ruta_completa1 = os.path.join(directorio, carpeta1)

        # Verificar si es una carpeta
        if os.path.isdir(ruta_completa1):
            # Obtener el nuevo nombre limpio
            nuevo_nombre = limpiar_nombre(carpeta1)

            # Intentar combinar con carpetas similares
            for j, carpeta2 in enumerate(carpetas[i+1:]):
                indice_original = i + 1 + j  # Ajustar el índice según el bucle interno
                ruta_completa2 = os.path.join(directorio, carpeta2)

                # Verificar si es una carpeta
                if os.path.isdir(ruta_completa2):
                    # Obtener el nuevo nombre limpio de la segunda carpeta
                    nuevo_nombre2 = limpiar_nombre(carpeta2)

                    # Calcular la similitud entre los nombres
                    similitud = similaridad_nombres(nuevo_nombre, nuevo_nombre2)

                    # Definir un umbral de similitud para combinar
                    umbral_similitud = 0.8

                    if similitud >= umbral_similitud:
                        # Fusionar las carpetas
                        nueva_ruta_completa = os.path.join(directorio, nuevo_nombre)
                        shutil.move(ruta_completa2, nueva_ruta_completa)
                        print(f"Fusionado: {carpeta2} con {carpeta1}")

def listar_carpetas(directorio):
    print("Carpetas en la carpeta:")
    for carpeta in os.listdir(directorio):
        if os.path.isdir(os.path.join(directorio, carpeta)):
            print(carpeta)

# Menú de usuario
while True:
    print("Menú:")
    print("1. Listar carpetas en la carpeta")
    print("2. Renombrar y fusionar carpetas")
    print("3. Salir")

    opcion = input("Selecciona una opción (1/2/3): ")

    if opcion == '1':
        listar_carpetas(source_directory)
    elif opcion == '2':
        print("Renombrando y fusionando carpetas en la carpeta...")
        procesar_carpetas(source_directory)
        print("Carpetas renombradas y fusionadas.")
    elif opcion == '3':
        print("Saliendo...")
        break
    else:
        print("Opción no válida. Por favor, selecciona una opción válida (1/2/3).")