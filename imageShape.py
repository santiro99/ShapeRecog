import cv2
import numpy as np
import math

class imageShape:
    def __init__(self, width, height):
        self.width = width
        self.height = height                #Constructor de la clase, se inicializan variables de entrada.

    def generateShape(self):
        self.figura = np.random.random_integers(0, 3, None)             #Se obtiene un num aleatorio entre 0 y 3. Uniformemente distribuido.
        self.shape = np.zeros((self.height, self.width, 3), np.uint8)   #Se genera imagen negra del tamaño indicado.
        cyan = (255, 255, 0)                                            #Se determina el color cyan.
        if self.figura == 0:
            lado = int(min(self.width, self.height)/2)                  #Se establece longitud de los lados.
            altura = int((math.sqrt(3)*lado)/2)                         #Se establece altura del triángulo
            pt1 = (int(self.width/2), int(self.height/2) - int(altura/2))
            pt2 = (self.width/2 - int(lado/2), int(self.height/2) - int(altura/2) + altura)
            pt3 = (self.width/2 + int(lado/2), int(self.height/2) - int(altura/2) + altura) #Se establece posición de los vertices.
            pts = np.array([pt1, pt2, pt3], np.int32)
            self.shape = cv2.fillPoly(self.shape, [pts], cyan)          #Se genera triangulo equilatero.

        if self.figura == 1:
            lado = int(min(self.width, self.height) / 2)                 #Se establece longitud de los lados.
            pt1 = (int(self.width/2), int(self.height/2) - int(lado/2))
            pt2 = (int(self.width/2) + int(lado/2), int(self.height/2))
            pt3 = (int(self.width/2), int(self.height/2) + int(lado/2))
            pt4 = (int(self.width/2) - int(lado/2), int(self.height/2))  #Se establece posición de los vertices.
            pts = np.array([pt1, pt2, pt3, pt4], np.int32)
            self.shape = cv2.fillPoly(self.shape, [pts], cyan)           #Se genera cuadrado.

        if self.figura == 2:
            lado_horizontal = int(self.width/2)                          #Se establece longitud del lado horizontal.
            lado_vertical = int(self.height/2)                           #Se establece longitud del lado vertical.
            pt1 = (int(self.width/2) - int(lado_horizontal/2), int(self.height/2) - int(lado_vertical/2))
            pt2 = (int(self.width/2) + int(lado_horizontal/2), int(self.height/2) - int(lado_vertical/2))
            pt3 = (int(self.width/2) + int(lado_horizontal/2), int(self.height/2) + int(lado_vertical/2))
            pt4 = (int(self.width/2) - int(lado_horizontal/2), int(self.height/2) + int(lado_vertical/2)) #Se establece posición de los vertices.
            pts = np.array([pt1, pt2, pt3, pt4], np.int32)
            self.shape = cv2.fillPoly(self.shape, [pts], cyan)          #Se genera rectangulo.

        if self.figura == 3:
            center = (int(self.width/2), int(self.height/2))        #Se establece posición del centro del circulo.
            radius = int(min(self.width, self.height)/4)            #Se establece longitud del radio.
            self.shape = cv2.circle(self.shape, center, radius, cyan, -1) #Se genera circulo.

    def showShape(self):
        if hasattr(self, 'shape'):
            cv2.imshow('Figura', self.shape)
            cv2.waitKey(5000)                               #Si la clase tiene atributo shape, muestra imagen por 5 segundos.
        else:
            cv2.imshow('Vacío', np.zeros((self.height, self.width, 3), np.uint8))
            cv2.waitKey(5000)                               #Sino, muestra imagen negra por 5 segundos.

    def getShape(self):
        if self.figura == 0:
            nombre = 'Triangle'
        if self.figura == 1:
            nombre = 'Square'
        if self.figura == 2:
            nombre = 'Rectangle'
        if self.figura == 3:
            nombre = 'Circle'              #Asigna nombre a la imagen generada, de acuerdo al numero aleatorio almacenado en self.figura.
        return self.shape, nombre          #Retorna imagen generada y nombre de la figura

    def whatShape(self, entrada):
        image_gray = cv2.cvtColor(entrada, cv2.COLOR_BGR2GRAY)      #Convierte la imagen a escala de grises.
        ret, umbralizada = cv2.threshold(image_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)   #Umbraliza la imagen, binaria y con el umbral de OTSU.
        contours, hierarchy = cv2.findContours(umbralizada, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE) #Encuentra contornos de la imagen y se almacenan en contours.
        for cnt in contours:                #Se mantiene el for para que la solución sea genérica, en este caso solo hay un contorno.
            approx = cv2.approxPolyDP(cnt, 0.01 * cv2.arcLength(cnt, True), True)   #Se encuentran vertices del polígono aproximado.
            if len(approx) == 3:
                clasificacion = 'Triangle'          #Si hay tres vertices, es un triángulo.
            elif len(approx) == 4:                  #Si hay cuatro vertices, puede ser un cuadrado o un rectángulo.
                (x, y, w, h) = cv2.boundingRect(approx)  #Crea un rectángulo que encierra la figura, w y h son height y width del rectangulo.
                if ((float(w) / h) == 1):               #Si la relación entre width y height es 1, es un cuadrado.
                    clasificacion = 'Square'
                else:                                   #Sino, es un rectangulo.
                    clasificacion = 'Rectangle'
            else:
                clasificacion = 'Circle'          #De otra manera es un círculo.

        return clasificacion                      #Retorna la clasificacion realizada.


