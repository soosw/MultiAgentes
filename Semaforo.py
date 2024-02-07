import pygame
from pygame.locals import *

# Cargamos las bibliotecas de OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import random
import math
import numpy as np


class Semaforo:

    def __init__(self, dim, obj, pos, cars, destino,estado):
        self.obj = obj
        self.pos = pos
        self.cars = cars
        self.destino = "Norte"
        self.state = estado
        self.radio = 50
        self.DimBoard = dim
        self.rotationAngle = -90.0
        self.newAngle = 0.0
        self.Position = [0.0, 0.0, 0.0]
        self.giveposition()
        self.adjustrotation()

    def update(self):
        #Change state here?
        var = 0
    def punto_en_area_circular(self, punto):
        distancia = math.sqrt((punto[0] - self.Position[0])**2 + (punto[1] - self.Position[1])**2 + (punto[2] - self.Position[2])**2)
        return distancia <= self.radio
    # Adjust rotation of object being drawn depending on position
    def adjustrotation(self):
        if self.pos == 1 or self.pos == 2:
            self.rotationAngle = -90.0
            self.newAngle = 180.0
        else:
            self.rotationAngle = -90.0
            self.newAngle = 90.0

    def giveposition(self):
        # Calle principal
        if self.pos == 1:
            self.Position[0] = -40.0
            self.Position[1] = 0.0
            self.Position[2] = 120.0
            self.direction = "Norte"
        # Calle principal
        elif self.pos == 2:
            self.Position[0] = -35.0
            self.Position[1] = 0.0
            self.Position[2] = -20.0
            self.direction = "Norte"
        # Primera interseccion
        elif self.pos == 3:
            self.Position[0] = -40.0
            self.Position[1] = 0.0
            self.Position[2] = 50.0
            self.direction = "Este"
        # Segunda interseccion
        elif self.pos == 4:
            self.Position[0] = -40.0
            self.Position[1] = 0.0
            self.Position[2] = -90.0
            self.direction = "Este"

    def draw(self):
        glPushMatrix()
        glTranslatef(self.Position[0], self.Position[1], self.Position[2])
        glRotatef(self.rotationAngle, 1.0, 0.0, 0.0)
        glRotatef(self.newAngle, 0.0, 0.0, 1.0)
        glScaled(3, 3, 3)
        glColor3f(1.0, 1.0, 1.0)
        self.obj.render()
        if self.state == "rojo":
            glColor3f(1.0,0.0,0.0)
        elif self.state == "amarillo":
            glColor3f(1.0,1.0,0.0)
        else:
            glColor3f(0.0,1.0,0.0)
        glTranslatef(0.0, 0.0, 29.0)
        gluSphere(gluNewQuadric(),1.7,16,16)
        glPopMatrix()
