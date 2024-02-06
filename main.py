

import pygame
import agentpy as ap
import math
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from loaders.objloader import *
import sys
sys.path.append('..')

from Carro import Carro

screen_width = 500
screen_height = 500
#vc para el obser.
FOVY=60.0
ZNEAR=1.0
ZFAR=900.0
#Variables para definir la posicion del observador
#gluLookAt(EYE_X,EYE_Y,EYE_Z,CENTER_X,CENTER_Y,CENTER_Z,UP_X,UP_Y,UP_Z)
EYE_X=300.0
EYE_Y=200.0
EYE_Z=300.0
CENTER_X=0
CENTER_Y=0
CENTER_Z=0
UP_X=0
UP_Y=1
UP_Z=0
#Variables para dibujar los ejes del sistema
X_MIN=-500
X_MAX=500
Y_MIN=-500
Y_MAX=500
Z_MIN=-500
Z_MAX=500
#Dimension del plano
DimBoard = 200
DimFloor = 500
objetos = []
#Variables para el control del observador
theta = 0.0 # Posicion angular con respecto al eje y
radius = 300

pygame.init()

carros = []
ncarros = 3

#Arreglo para el manejo de texturas
textures = []
texturaFondo = "textures/textura3.bmp"
texturaCalle = "textures/Asphalt_Intersect.bmp"

def Init():
    screen = pygame.display.set_mode(
        (screen_width, screen_height), DOUBLEBUF | OPENGL)
    pygame.display.set_caption("OpenGL: carros")

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(FOVY, screen_width/screen_height, ZNEAR, ZFAR)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(EYE_X,EYE_Y,EYE_Z,CENTER_X,CENTER_Y,CENTER_Z,UP_X,UP_Y,UP_Z)
    glClearColor(0,0,0,0)
    glEnable(GL_DEPTH_TEST)
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    
    Texturas(texturaFondo)
    Texturas(texturaCalle)

    glLightfv(GL_LIGHT0, GL_POSITION, (0, 200, 0, 0.0))
    glLightfv(GL_LIGHT0, GL_AMBIENT, (0.5, 0.5, 0.5, 1.0))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.5, 0.5, 0.5, 1.0))
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)
    glShadeModel(GL_SMOOTH)

    objetos.append(OBJ("models/Lowpoly_tree_sample.obj", swapyz=True))
    objetos.append(OBJ("models/House.obj", swapyz=True))
    objetos.append(OBJ("models/Treelow.obj", swapyz=True))
    objetos.append(OBJ("models/building2.obj", swapyz=True))
    objetos.append(OBJ("models/Chevrolet_Camaro_SS_Low.obj", swapyz=True))
    objetos.append(OBJ("models/traffi_light.obj", swapyz=True))
    objetos[0].generate()

    for i in range(ncarros):
        carros.append(Carro(DimBoard, 1.0, objetos[4]))
    


def Texturas(filepath):
    textures.append(glGenTextures(1))
    id = len(textures) - 1
    glBindTexture(GL_TEXTURE_2D, textures[id])
    glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    image = pygame.image.load(filepath).convert()
    w, h = image.get_rect().size
    image_data = pygame.image.tostring(image,"RGBA")
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, w, h, 0, GL_RGBA, GL_UNSIGNED_BYTE, image_data)
    glGenerateMipmap(GL_TEXTURE_2D)

def lookat():
    global EYE_X
    global EYE_Z
    global radius
    EYE_X = radius * (math.cos(math.radians(theta)) + math.sin(math.radians(theta)))
    EYE_Z = radius * (-math.sin(math.radians(theta)) + math.cos(math.radians(theta)))
    glLoadIdentity()
    gluLookAt(EYE_X,EYE_Y,EYE_Z,CENTER_X,CENTER_Y,CENTER_Z,UP_X,UP_Y,UP_Z)

def displayCar():
    glPushMatrix()
    glRotatef(-90.0, 1.0, 0.0, 0.0)
    glTranslatef(0.0, 0.0, -10.0)
    glScale(5.0,5.0,5.0)
    objetos[4].render()
    glPopMatrix()

def displayTree1():
    glPushMatrix()  
    glRotatef(-90.0, 1.0, 0.0, 0.0)
    glTranslatef(100.0, 0.0, 0)
    glScale(2.0,2.0,2.0)
    objetos[0].render()
    glTranslatef(25.0, -10.0, 0.0)
    objetos[0].render()
    glTranslatef(10.0, 15.0, 0.0)
    objetos[0].render()
    glTranslatef(-50.0, 0.0, 0.0)
    objetos[0].render()
    glTranslatef(0.0, -15.0, 0.0)
    objetos[0].render()
    glPopMatrix()
    
def displayTree2():
    glPushMatrix()  
    glRotatef(-90.0, 1.0, 0.0, 0.0)
    glTranslatef(150.0, -150.0, 0.0)
    glScale(2.0,2.0,2.0)
    objetos[0].render()
    glTranslatef(-20.0, 10.0, 0.0)
    objetos[0].render()
    glTranslatef(0.0, -15.0, 0.0)
    objetos[0].render()
    glTranslatef(-20.0, 10.0, 0.0)
    objetos[0].render()
    glPopMatrix()

def displayTree3():
    glPushMatrix()  
    glRotatef(-90.0, 1.0, 0.0, 0.0)
    glTranslatef(-55.0, 175.0, 0.0)
    glScale(0.8,0.8,0.8)
    objetos[2].render()
    glPopMatrix()

def displayHouse():
    glPushMatrix()  
    glRotatef(-90.0, 1.0, 0.0, 0.0)
    glTranslatef(-125.0, 150.0, 0.0)
    glScale(5.5,5.5,5.5)
    objetos[1].render()  
    glPopMatrix()
    
def displayBuilding1():
    glPushMatrix()
    glTranslatef(-125.0, -12.0, 20.0)
    glRotatef(-90.0, 1.0, 0.0, 0.0)
    glScale(2.5,2.5,2.5)
    objetos[3].render()  
    glPopMatrix()

def displayBuilding2():
    glPushMatrix()
    glTranslatef(-125.0, -13.0, 150.0)
    glRotatef(-90.0, 1.0, 0.0, 0.0)
    glScale(2.5,2.5,2.5)
    objetos[3].render()  
    glPopMatrix()

def displayBuilding3():
    glPushMatrix()
    glTranslatef(125.0, -13.0, -145.0)
    glRotatef(270.0, 1.0, 0.0, 0.0)
    glScale(2.5,2.5,2.5)
    objetos[3].render()  
    glPopMatrix()
    
def displayTrafficLight(x, y, z):
    glPushMatrix()
    glTranslatef(x, y, z)
    glRotatef(-90.0, 1.0, 0.0, 0.0)
    glScale(2.5,2.5,2.5)
    objetos[5].render()  
    glPopMatrix()
    
def display():  
    glClearColor(0.6, 0.8, 1.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Activar el uso de texturas
    glEnable(GL_TEXTURE_2D)

    # Se dibuja el plano con textura de asfalto
    glBindTexture(GL_TEXTURE_2D, textures[1])
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0)
    glVertex3d(-DimBoard, 0, -DimBoard)
    glTexCoord2f(1.0, 0.0)
    glVertex3d(-DimBoard, 0, DimBoard)
    glTexCoord2f(1.0, 1.0)
    glVertex3d(DimBoard, 0, DimBoard)
    glTexCoord2f(0.0, 1.0)
    glVertex3d(DimBoard, 0, -DimBoard)
    glEnd()

    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, textures[1])
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0)
    glVertex3d(-DimFloor, 0, -DimFloor)
    glTexCoord2f(1.0, 0.0)
    glVertex3d(-DimFloor, 0, DimFloor)
    glTexCoord2f(1.0, 1.0)
    glVertex3d(DimFloor, 0, DimFloor)
    glTexCoord2f(0.0, 1.0)
    glVertex3d(DimFloor, 0, -DimFloor)
    glEnd()

    # Clear the texture unit and disable textures
    glDisable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, 0)
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)

    # Dibujar el plano de la calle
    glColor3f(1.0, 1.0, 1.0)  # Color para los prismas rectangulares

    # Cambiar valor de y de las calles a ~1 cuando se termine la colocacion de edificios
    
    # calle 1
    glBegin(GL_QUADS)
    glVertex3d(-30, 1, -90)
    glVertex3d(-30, 1, -200)
    glVertex3d(-30, 0, -200)
    glVertex3d(-30, 0, -90)
    glEnd()
    
    # calle 1.1
    glBegin(GL_QUADS)
    glVertex3d(-200, 1, -90)
    glVertex3d(-30, 1, -90)
    glVertex3d(-30, 0, -90)  
    glVertex3d(-200, 0, -90)
    glEnd()

    # calle 2
    glBegin(GL_QUADS)
    glVertex3d(-30, 1, 50)
    glVertex3d(-30, 1, -20)
    glVertex3d(-30, 0, -20)
    glVertex3d(-30, 0, 50)
    glEnd()
    
    #calle 2.1
    glBegin(GL_QUADS)
    glVertex3d(-200, 1, -20)
    glVertex3d(-30, 1, -20)
    glVertex3d(-30, 0, -20)
    glVertex3d(-200, 0, -20)
    glEnd()
    
    #calle 2.2
    glBegin(GL_QUADS)
    glVertex3d(-200, 1, 50)
    glVertex3d(-30, 1, 50)
    glVertex3d(-30, 0, 50)
    glVertex3d(-200, 0, 50)
    glEnd()
    
    # calle 6
    glBegin(GL_QUADS)
    glVertex3d(-40, 1, 200)
    glVertex3d(-40, 1, 120)
    glVertex3d(-40, 0, 120)
    glVertex3d(-40, 0, 200)
    glEnd()

    #calle 6.1
    glBegin(GL_QUADS)
    glVertex3d(-200, 1, 120)
    glVertex3d(-40, 1, 120)
    glVertex3d(-40, 0, 120)
    glVertex3d(-200, 0, 120)
    glEnd()

    # calle 3
    glBegin(GL_QUADS)
    glVertex3d(40, 1, -90)
    glVertex3d(40, 1, -200)
    glVertex3d(40, 0, -200)
    glVertex3d(40, 0, -90)
    glEnd()

    # calle 3.1
    glBegin(GL_QUADS)
    glVertex3d(200, 1, -90)
    glVertex3d(40, 1, -90)
    glVertex3d(40, 0, -90)
    glVertex3d(200, 0, -90)
    glEnd()

    # calle 4
    glBegin(GL_QUADS)
    glVertex3d(40, 1, 50)
    glVertex3d(40, 1, -20)
    glVertex3d(40, 0, -20)
    glVertex3d(40, 0, 50)
    glEnd()

    #calle 4.1
    glBegin(GL_QUADS)
    glVertex3d(200, 1, -20)
    glVertex3d(40, 1, -20)
    glVertex3d(40, 0, -20)
    glVertex3d(200, 0, -20)
    glEnd()

    #calle 4.2
    glBegin(GL_QUADS)
    glVertex3d(200, 1, 50)
    glVertex3d(40, 1, 50)
    glVertex3d(40, 0, 50)
    glVertex3d(200, 0, 50)
    glEnd()
    
    # calle 5
    glBegin(GL_QUADS)
    glVertex3d(40, 1, 200)
    glVertex3d(40, 1, 120)
    glVertex3d(40, 0, 120)
    glVertex3d(40, 0, 200)
    glEnd()
    
    #calle 5.1
    glBegin(GL_QUADS)
    glVertex3d(200, 1, 120)
    glVertex3d(40, 1, 120)
    glVertex3d(40, 0, 120)
    glVertex3d(200, 0, 120)
    glEnd()
    
    # Restaurar el modo de línea para otros elementos
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)

    glColor3f(0.2, 0.6, 0.2)  # Color para las paredes

    # Establecer el modo de relleno para las paredes
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)

    # Se dibujan las paredes con textura de ciudad (revisar)
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, textures[0])
    glColor3f(1.0, 1.0, 1.0)

    # Pared frontal
    glBegin(GL_QUADS)
    glVertex3d(-DimBoard, 30, DimBoard)
    glVertex3d(DimBoard, 30, DimBoard)
    glVertex3d(DimBoard, 0, DimBoard)
    glVertex3d(-DimBoard, 0, DimBoard)
    glEnd()
    # Pared trasera
    glBegin(GL_QUADS)
    glVertex3d(-DimBoard, 30, -DimBoard)
    glVertex3d(DimBoard, 30, -DimBoard)
    glVertex3d(DimBoard, 0, -DimBoard)
    glVertex3d(-DimBoard, 0, -DimBoard)
    glEnd()

    # Pared izquierda
    glBegin(GL_QUADS)
    glVertex3d(-DimBoard, 30, -DimBoard)
    glVertex3d(-DimBoard, 30, DimBoard)
    glVertex3d(-DimBoard, 0, DimBoard)
    glVertex3d(-DimBoard, 0, -DimBoard)
    glEnd()

    # Pared derecha
    glBegin(GL_QUADS)
    glVertex3d(DimBoard, 30, -DimBoard)
    glVertex3d(DimBoard, 30, DimBoard)
    glVertex3d(DimBoard, 0, DimBoard)
    glVertex3d(DimBoard, 0, -DimBoard)
    glEnd()
    glDisable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, 0)

    # Restaurar el modo de línea para otros elementos
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)

    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    glColor3f(1.0, 1.0, 1.0)
    for obj in carros:
        obj.draw()
        obj.update()

    # Se despliegan todos los objetos e el plano
    displayTree1()
    displayTree2()
    displayTree3()
    displayHouse()
    displayBuilding1()
    displayBuilding2()
    displayBuilding3()
    displayTrafficLight(-40, 0, 120)
    displayTrafficLight(-40, 0, -90)
    # No borrar (temp fix)
    displayCar()

#Clase del agente Cubo:
class carAgent(ap.Agent):
    
    def setup(self):
    
        self.carGraphic = None
        pass
    
    def step(self):
        #Ejemplo de manipulación gráfica desde el agente Cubo:
        #self.cuboGraphic.Position[0] *=1.1
        #self.cuboGraphic.Position[0] %= 200
        #self.cuboGraphic.Position[2] *=1.1
        #self.cuboGraphic.Position[2] %= 200
        pass
    
    #Update para el agente
    def update(self):
        #Llamar a las funciones de dibujado del Cubo Grafico
        self.carGraphic.draw()
        self.carGraphic.update()
        pass
    
    def getCarGraphic(self):
        #Por si en algún momento se necesita el Cubo Gráfico externamente
        return self.carGraphic
    
    
#Clase del modelo
class trafficModel(ap.Model):
    
    def setup(self):
        self.done = False
        #Importante llamar a Init() para inicializar el Cubo Gráfico antes del Agente Cubo
        Init()
        
        #Inicializar los agentes Cubos
        self.carlist = ap.AgentList(self,self.p.carros_n,carAgent)
        #Agregar los Cubos Gráficos (definidos globalmente al inicio del código) a la lista de agentes Cubo.
        self.carlist.carGraphic = ap.AttrIter(carros)
        pass
    
    def step(self):
        #Llamar a Step de los agentes
        self.carlist.step()
        pass
    
    def update(self):
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True
        display()
        self.carlist.update()
        pygame.display.flip()
        pygame.time.wait(10)
        
        if self.done:
            pygame.quit()
            self.stop()
        pass
    
    def end(self):
        pass
    
parameters ={
    "carros_n" : ncarros,
    "steps" : 3000,
    "seed" : 21
    }

model = trafficModel(parameters)
model.run()


done = False
Init()

while not done:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        if theta > 359.0:
            theta = 0
        else:
            theta += 1.0
        lookat()
    if keys[pygame.K_LEFT]:
        if theta < 1.0:
            theta = 360.0
        else:
            theta += -1.0
        lookat()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    display()

    pygame.display.flip()
    pygame.time.wait(10)

pygame.quit()