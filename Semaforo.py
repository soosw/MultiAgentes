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

    def __init__(self, dim, obj, pos, destino, luz):
        self.obj = obj
        self.pos = pos
        self.cars = None
        self.destino = destino
        self.state = "rojo"
        self.luz = luz
        self.radio = 50
        self.radioGeneral = 200
        self.DimBoard = dim
        self.rotationAngle = -90.0
        self.newAngle = 0.0
        self.Position = [0.0, 0.0, 0.0]
        self.giveposition()
        self.adjustrotation()
    def cambiarCarros(self, carros):
        self.cars = carros
    def cambiarEstado(self, estado):
        self.state = estado
    def update(self):
        #Change state here?
        var = 0
    def punto_en_area_circular(self, punto):
        distancia = math.sqrt((punto[0] - self.Position[0])**2 + (punto[1] - self.Position[1])**2 + (punto[2] - self.Position[2])**2)
        return distancia <= self.radio
    def calcularCarrosAlrededor(self):
        contador = 0
        for carro in self.cars:
            posicionCarro = carro.getPosition()
            distancia = math.sqrt((posicionCarro[0] - self.Position[0])**2 + (posicionCarro[1] - self.Position[1])**2 + (posicionCarro[2] - self.Position[2])**2)
            if distancia <= self.radio:
                contador += 1
        return contador
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