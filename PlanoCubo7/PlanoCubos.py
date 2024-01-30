#Autor: Ivan Olmos Pineda
#Curso: Multiagentes - Graficas Computacionales

import pygame
from pygame.locals import *

# Cargamos las bibliotecas de OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# Se carga el archivo de la clase Cubo
import sys
sys.path.append('..')
from Cubo import Cubo

screen_width = 500
screen_height = 500
#vc para el obser.
FOVY=60.0
ZNEAR=0.01
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

pygame.init()

#cubo = Cubo(DimBoard, 1.0)
cubos = []
ncubos = 50

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
    
    for i in range(ncubos):
        cubos.append(Cubo(DimBoard, 1.0))

def display():  
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    # Axis()

    # Establecer el modo de relleno para el plano
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)

    # Activar el uso de texturas
    glEnable(GL_TEXTURE_2D)
    # glBindTexture(GL_TEXTURE_2D, loadTexture())
    # Se dibuja el plano con textura de madera
    glColor3f(0.5, 0.5, 0.5)  # Color blanco para que la textura se muestre en su color original
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
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)

    
    glColor3f(0.8, 0.8, 0.8)  # Color gris claro para las paredes

    # Establecer el modo de relleno para las paredes
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)

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

    # Dibujar puerta de color café fuera del plano
    glColor3f(0.4, 0.2, 0.0)  # Color café oscuro para la puerta
    glBegin(GL_QUADS)
    glVertex3d(-50, 0, DimBoard + 10)  # Ajustar la posición en Z para colocar la puerta fuera del plano
    glVertex3d(-50, 0, DimBoard - 20)  # Ajustar la posición en Z para colocar la puerta fuera del plano
    glVertex3d(50, 0, DimBoard - 20)   # Ajustar la posición en Z para colocar la puerta fuera del plano
    glVertex3d(50, 0, DimBoard + 10)   # Ajustar la posición en Z para colocar la puerta fuera del plano
    glEnd()

    # Restaurar el modo de línea para otros elementos
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)

    # Dibujar cubos con relleno 
    glColor3f(0.2, 0.4, 0.6)  # Color azul para los cubos
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    #Se dibuja cubos
    for obj in cubos:
        obj.draw()
        obj.update()
    
done = False
Init()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    display()

    pygame.display.flip()
    pygame.time.wait(10)

pygame.quit()