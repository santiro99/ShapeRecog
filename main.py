from imageShape import *


if __name__ == '__main__':
    height = int(input('Ingrese altura de la imagen '))
    width = int(input('Ingrese ancho de la imagen  '))      #Pide parametros de entrada al usuario.
    imagen = imageShape(width, height)                      #Se crea el objeto imagen, llamando la clase imageShape.
    imagen.generateShape()
    imagen.showShape()
    generada, nombre = imagen.getShape()                    #Se guarda la imagen generada y el nombre de la figura generada.
    clasificacion = imagen.whatShape(generada)
    
    
    if nombre == clasificacion:
        print('La clasificacion es correcta.')
    else:
        print('La clasificacion es incorrecta')             #Compara el nombre con la clasificacion, indica si es correcta o no.

    image_draw = generada.copy()                            #Genera una copia de la imagen para escribir en ella.
    x = int(width/2)
    y = int(height/2)
    font = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 2                                           #Se definen parametros del texto que se escribira en la imagen.
    color = (255, 255, 255)
    thickness = 2
    cv2.putText(image_draw, clasificacion, (x, y), font, fontScale, color, thickness) #Escribe texto en la imagen.
    cv2.imshow('Clasificada', image_draw)                   #Muestra la imagen con el texto
    cv2.waitKey(0)
