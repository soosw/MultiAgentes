import pygame
from pygame.locals import *

# Cargamos las bibliotecas de OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import random
import math
import numpy as np

class Carro:
    
    def __init__(self, dim, vel, obj, pos, destino):
        self.obj = obj
        self.pos = pos
        self.DimBoard = dim
        self.vel = vel
        self.rotationAngle = -90.0
        self.newAngle = 0.0
        self.destino = destino
        # Placeholder position
        self.Position = [0.0,0.0,0.0]
        # Placeholder direction
        self.Direction = [0.0,0.0,0.0]
        self.giveposition()
        self.adjustrotation()
        self.detenido = False
        self.cars = None
        
    def getPosition(self):
        return self.Position
    def cambiarCarros(self, carros):
        self.cars = carros

    def update(self):
        if not self.detenido:
            new_x = self.Position[0] + self.Direction[0]
            new_z = self.Position[2] + self.Direction[2]
            self.adjustrotation()

        # if self.currentRotation != self.rotationAngle:
        #     if self.currentRotation < self.rotationAngle:
        #         self.currentRotation += 5
        #     else:
        #         self.currentRotation -= 5

        #detecc de que el objeto no se salga del area de navegacion
            if abs(new_x) <= self.DimBoard and abs(new_z) <= self.DimBoard:
                self.Position[0] = new_x
                self.Position[2] = new_z
            else:
                self.giveposition()

    def adjustrotation(self):
        if self.pos == 1:
            self.rotationAngle = -90.0
        else:
            self.rotationAngle = -90.0
            self.newAngle = -90.0

    def giveposition(self):
             #Calle principal
        if self.pos == 1:
            self.Position[0] = 0.0
            self.Position[1] = 5.0
            self.Position[2] = 190.0
            self.Direction[0] = 0.0
            self.Direction[1] = 5.0
            self.Direction[2] = -100.0
            #Primera interseccion
        elif self.pos == 2:
            self.Position[0] = -190.0
            self.Position[1] = 5.0
            self.Position[2] = 90.0
            self.Direction[0] = 100.0
            self.Direction[1] = 5.0
            self.Direction[2] = 0.0
            #Segunda interseccion
        elif self.pos == 3:
            self.Position[0] = -190.0
            self.Position[1] = 5.0
            self.Position[2] = -70.0
            self.Direction[0] = 100.0
            self.Direction[1] = 5.0
            self.Direction[2] = 0.0

        # Se normaliza el vector de direccion
        m = math.sqrt(self.Direction[0] * self.Direction[0] + self.Direction[2] * self.Direction[2])
        self.Direction[0] /= m
        self.Direction[2] /= m
        # Se cambia la maginitud del vector direccion
        self.Direction[0] *= self.vel
        self.Direction[2] *= self.vel
        self.rotationAngle = 0

    def draw(self):
        glPushMatrix()
        glTranslatef(self.Position[0], self.Position[1], self.Position[2])
        glRotatef(self.rotationAngle, 1.0, 0.0, 0.0)
        glRotatef(self.newAngle, 0.0, 0.0, 1.0)
        glScaled(2,2,2)
        glColor3f(1.0, 1.0, 1.0)
        self.obj.render()
        glPopMatrix()