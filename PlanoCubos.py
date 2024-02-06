#Autor: Ivan Olmos Pineda
#Curso: Multiagentes - Graficas Computacionales

import pygame
from pygame.locals import *
import agentpy as ap

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
ncubos = 20

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
    Axis()
    #Se dibuja el plano gris
    glColor3f(0.3, 0.3, 0.3)
    glBegin(GL_QUADS)
    glVertex3d(-DimBoard, 0, -DimBoard)
    glVertex3d(-DimBoard, 0, DimBoard)
    glVertex3d(DimBoard, 0, DimBoard)
    glVertex3d(DimBoard, 0, -DimBoard)
    glEnd()
    #Se dibuja cubos
    #cubo.draw()
    #cubo.Update()
    #for obj in cubos:
    #    obj.drawCube()
    #    obj.update()
        
        
#Clase del agente Cubo:
class CuboAgent(ap.Agent):
    
    def setup(self):
    
        self.cuboGraphic = None
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
        self.cuboGraphic.drawCube()
        self.cuboGraphic.update()
        pass
    
    def getCuboGraphic(self):
        #Por si en algún momento se necesita el Cubo Gráfico externamente
        return self.cuboGraphic
    
    
#Clase del modelo
class CuboModel(ap.Model):
    
    def setup(self):
        self.done = False
        #Importante llamar a Init() para inicializar el Cubo Gráfico antes del Agente Cubo
        Init()
        
        #Inicializar los agentes Cubos
        self.cuboslist = ap.AgentList(self,self.p.cubos_n,CuboAgent)
        #Agregar los Cubos Gráficos (definidos globalmente al inicio del código) a la lista de agentes Cubo.
        self.cuboslist.cuboGraphic = ap.AttrIter(cubos)
        pass
    
    def step(self):
        #Llamar a Step de los agentes
        self.cuboslist.step()
        pass
    
    def update(self):
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True
        display()
        self.cuboslist.update()
        pygame.display.flip()
        pygame.time.wait(10)
        
        if self.done:
            pygame.quit()
            self.stop()
        pass
    
    def end(self):
        pass
    
parameters ={
    "cubos_n" : ncubos,
    "steps" : 3000,
    "seed" : 21
    }

model = CuboModel(parameters)
model.run()


