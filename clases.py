import numpy as np
import matplotlib.pyplot as plt
import os
import requests
import cv2
import pydicom


def Conteo_celulas(ruta):
    imagen = cv2.imread(ruta)
    imagen[:,:,1]=0
    imagen[:,:,0]=0
    img_1 = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    img_2 = cv2.GaussianBlur(img_1, (5, 5), 0)
    umb, img_3 = cv2.threshold(img_2, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    kernel = np.ones((25,25), np.uint8)
    img_4 = cv2.morphologyEx(img_3, cv2.MORPH_CLOSE, kernel, iterations=1)
    img_5 = cv2.morphologyEx(img_4, cv2.MORPH_OPEN, kernel, iterations=1)
    elem,mask=cv2.connectedComponents(img_5)
    print(f"Se contaron {elem} celulas en la imagen")

def cargar_dicom(ruta):
    list_img= []
    archivos = os.listdir(ruta)
    archivos_dicom = sorted([archivo for archivo in archivos if archivo.endswith('.dcm')])
    for archivo in archivos_dicom:
        ruta__dicom = os.path.join(ruta, archivo)
        imagen = pydicom.dcmread(ruta__dicom).pixel_array
        list_img.append(imagen)
    return list_img

def imagenes_en_bucle(list_img):
    fig = plt.figure()
    cont = 0
    while cont < 4:
        for image in list_img:
            plt.imshow(image, cmap=plt.cm.gray)
            plt.title("Imagen en bucle")
            plt.axis( 'off')
            plt.pause(0.05) 
            plt.clf()
        for image in list_img[::-1]:
            plt.imshow(image, cmap=plt.cm.gray)
            plt.title("Imagen en bucle")
            plt.axis( 'off' )
            plt.pause(0.05) 
            plt.clf() 
        cont += 1

