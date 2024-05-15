from clases import *

print("Bienvenido al sistema de conteo de celulas y visualizacion de imagenes dicom".center(100,"-"))
def main():
    while True:
        opcion = int(input("1. Conteo de celulas\n2. Visualizacion de imagenes dicom\n3. Salir\n"))
        if opcion == 1:
            ruta = input("Ingrese la ruta de la imagen: ")
            Conteo_celulas(ruta)
        elif opcion == 2:
            ruta = input("Ingrese la ruta de la carpeta con los archivos dicom: ")
            list_img = cargar_dicom(ruta)
            display_dicon_images(list_img)
        elif opcion == 3:
            print("Gracias por usar el sistema")
            break
        else:
            print("Opcion no valida")
            main()

if __name__ == '__main__':
    main()