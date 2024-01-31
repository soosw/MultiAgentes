#Autor: Ivan Olmos Pineda
#Curso: Multiagentes - Graficas Computacionales

import pygame
import math
from pygame.locals import *

# Cargamos las bibliotecas de OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# Import obj loader
from loaders.objloader import *

# Se carga el archivo de la clase Cubo
import sys
sys.path.append('..')
from Cubo import Cubo

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
objetos = []
#Variables para el control del observador
theta = 0.0 # Posicion angular con respecto al eje y
radius = 300

pygame.init()

#cubo = Cubo(DimBoard, 1.0)
cubos = []
ncubos = 0

#Arreglo para el manejo de texturas
textures = []
texturaFondo = "textures/textura3.bmp"
texturaCalle = "textures/Asphalt_Intersect.bmp"

def Axis():
    glShadeModel(GL_FLAT)
    glLineWidth(3.0)
    #X axis in red
    glColor3f(1.0,0.0,0.0)
    glBegin(GL_LINES)
    glVertex3f(X_MIN,0.0,0.0)
    glVertex3f(X_MAX,0.0,0.0)
    glEnd()
    #Y axis in green
    glColor3f(0.0,1.0,0.0)
    glBegin(GL_LINES)
    glVertex3f(0.0,Y_MIN,0.0)
    glVertex3f(0.0,Y_MAX,0.0)
    glEnd()
    #Z axis in blue
    glColor3f(0.0,0.0,1.0)
    glBegin(GL_LINES)
    glVertex3f(0.0,0.0,Z_MIN)
    glVertex3f(0.0,0.0,Z_MAX)
    glEnd()
    glLineWidth(1.0)

def Init():
    screen = pygame.display.set_mode(
        (screen_width, screen_height), DOUBLEBUF | OPENGL)
    pygame.display.set_caption("OpenGL: cubos")

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(FOVY, screen_width/screen_height, ZNEAR, ZFAR)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(EYE_X,EYE_Y,EYE_Z,CENTER_X,CENTER_Y,CENTER_Z,UP_X,UP_Y,UP_Z)
    glClearColor(0,0,0,0)
    glEnable(GL_DEPTH_TEST)
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    
    # !!! esto ha cambiado
    Texturas(texturaFondo)
    Texturas(texturaCalle)

    for i in range(ncubos):
        cubos.append(Cubo(DimBoard, 1.0))
    
    glLightfv(GL_LIGHT0, GL_POSITION,  (0, 200, 0, 0.0))
    glLightfv(GL_LIGHT0, GL_AMBIENT, (0.5, 0.5, 0.5, 1.0))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.5, 0.5, 0.5, 1.0))
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)
    glShadeModel(GL_SMOOTH)   
    
    objetos.append(OBJ("models/Lowpoly_tree_sample.obj", swapyz=True))
    objetos[0].generate()

    


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

def displayobj():
    glPushMatrix()  
    #correcciones para dibujar el objeto en plano XZ
    #esto depende de cada objeto
    glRotatef(-90.0, 1.0, 0.0, 0.0)
    glTranslatef(0.0, 0.0, 15.0)
    glScale(3.0,3.0,3.0)
    objetos[0].render()  
    glPopMatrix()

def display():  
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    # Axis()
    
    # Establecer el modo de relleno para el plano
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)

    # Activar el uso de texturas
    glEnable(GL_TEXTURE_2D)
    # Se dibuja el plano con textura de asfalto
    glBindTexture(GL_TEXTURE_2D, textures[1])
    glColor3f(1.0, 1.0, 1.0)  # Color blanco para que la textura se muestre en su color original
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
    glDisable(GL_TEXTURE_2D)

    # Restaurar el modo de línea para otros elementos
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)

    
    # Dibujar el plano de la calle
    glColor3f(1.0, 1.0, 1.0)  # Color para los prismas rectangulares

    # Cambiar valor de y de las calles a ~1 cuando se termine la colocacion de edificios
    
    # calle 1
    glBegin(GL_QUADS)
    glVertex3d(-30, 30, -90)
    glVertex3d(-30, 30, -200)
    glVertex3d(-30, 0, -200)
    glVertex3d(-30, 0, -90)
    glEnd()
    
    # calle 1.1
    glBegin(GL_QUADS)
    glVertex3d(-200, 30, -90)
    glVertex3d(-30, 30, -90)
    glVertex3d(-30, 0, -90)  
    glVertex3d(-200, 0, -90)
    glEnd()

    # calle 2
    glBegin(GL_QUADS)
    glVertex3d(-30, 30, 50)
    glVertex3d(-30, 30, -20)
    glVertex3d(-30, 0, -20)
    glVertex3d(-30, 0, 50)
    glEnd()
    
    #calle 2.1
    glBegin(GL_QUADS)
    glVertex3d(-200, 30, -20)
    glVertex3d(-30, 30, -20)
    glVertex3d(-30, 0, -20)
    glVertex3d(-200, 0, -20)
    glEnd()
    
    #calle 2.2
    glBegin(GL_QUADS)
    glVertex3d(-200, 30, 50)
    glVertex3d(-30, 30, 50)
    glVertex3d(-30, 0, 50)
    glVertex3d(-200, 0, 50)
    glEnd()
    
    # calle 6
    glBegin(GL_QUADS)
    glVertex3d(-40, 30, 200)
    glVertex3d(-40, 30, 120)
    glVertex3d(-40, 0, 120)
    glVertex3d(-40, 0, 200)
    glEnd()

    #calle 6.1
    glBegin(GL_QUADS)
    glVertex3d(-200, 30, 120)
    glVertex3d(-40, 30, 120)
    glVertex3d(-40, 0, 120)
    glVertex3d(-200, 0, 120)
    glEnd()

    # calle 3
    glBegin(GL_QUADS)
    glVertex3d(40, 30, -90)
    glVertex3d(40, 30, -200)
    glVertex3d(40, 0, -200)
    glVertex3d(40, 0, -90)
    glEnd()

    # calle 3.1
    glBegin(GL_QUADS)
    glVertex3d(200, 30, -90)
    glVertex3d(40, 30, -90)
    glVertex3d(40, 0, -90)
    glVertex3d(200, 0, -90)
    glEnd()

    # calle 4
    glBegin(GL_QUADS)
    glVertex3d(40, 30, 50)
    glVertex3d(40, 30, -20)
    glVertex3d(40, 0, -20)
    glVertex3d(40, 0, 50)
    glEnd()

    #calle 4.1
    glBegin(GL_QUADS)
    glVertex3d(200, 30, -20)
    glVertex3d(40, 30, -20)
    glVertex3d(40, 0, -20)
    glVertex3d(200, 0, -20)
    glEnd()

    #calle 4.2
    glBegin(GL_QUADS)
    glVertex3d(200, 30, 50)
    glVertex3d(40, 30, 50)
    glVertex3d(40, 0, 50)
    glVertex3d(200, 0, 50)
    glEnd()
    
    # calle 5
    glBegin(GL_QUADS)
    glVertex3d(40, 30, 200)
    glVertex3d(40, 30, 120)
    glVertex3d(40, 0, 120)
    glVertex3d(40, 0, 200)
    glEnd()
    
    #calle 5.1
    glBegin(GL_QUADS)
    glVertex3d(200, 30, 120)
    glVertex3d(40, 30, 120)
    glVertex3d(40, 0, 120)
    glVertex3d(200, 0, 120)
    glEnd()
    
    # Restaurar el modo de línea para otros elementos
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)

    
    glColor3f(0.2, 0.6, 0.2)  # Color para las paredes


    # Establecer el modo de relleno para las paredes
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)


    # Se dibujan las paredes con textura de ciudad?
    # glEnable(GL_TEXTURE_2D)
    # glBindTexture(GL_TEXTURE_2D, textures[0])
    # glColor3f(1.0, 1.0, 1.0)

    # Pared frontal
    glBegin(GL_QUADS)
    glVertex3d(-DimBoard, 30, DimBoard)
    glVertex3d(DimBoard, 30, DimBoard)
    glVertex3d(DimBoard, 0, DimBoard)
    glVertex3d(-DimBoard, 0, DimBoard)
    glEnd()
    glDisable(GL_TEXTURE_2D)
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
    # Restaurar el modo de línea para otros elementos
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)

    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)

    for obj in cubos:
        obj.draw()
        obj.update()
    
    displayobj()
    
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