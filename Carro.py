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
    
    def __init__(self, dim, vel, obj):
        #vertices del cubo
        # self.points = np.array([[-1.0,-1.0, 1.0], [1.0,-1.0, 1.0], [1.0,-1.0,-1.0], [-1.0,-1.0,-1.0],
        #                         [-1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [1.0, 1.0,-1.0], [-1.0, 1.0,-1.0]])
        self.obj = obj
        self.DimBoard = dim
        self.rotationAngle = 0.0
        self.currentRotation = 0.0
        #Se inicializa una posicion aleatoria en el tablero
        # self.Position = []
        # self.Position.append(random.randint(-1 * self.DimBoard, self.DimBoard))
        # self.Position.append(5.0)
        # self.Position.append(random.randint(-1 * self.DimBoard, self.DimBoard))
        # Placeholder position
        self.Position = []
        self.Position.append(0.0)
        self.Position.append(5.0)
        self.Position.append(120.0)
        #Se inicializa un vector de direccion aleatorio
        # self.Direction = []
        # self.Direction.append(random.random())
        # self.Direction.append(5.0)
        # self.Direction.append(random.random())
        # Placeholder direction
        self.Direction = []
        self.Direction.append(0)
        self.Direction.append(5.0)
        self.Direction.append(-100)
        #Se normaliza el vector de direccion
        m = math.sqrt(self.Direction[0]*self.Direction[0] + self.Direction[2]*self.Direction[2])
        self.Direction[0] /= m
        self.Direction[2] /= m
        #Se cambia la maginitud del vector direccion
        self.Direction[0] *= vel
        self.Direction[2] *= vel
        self.rotationAngle = 0
        

    def update(self):
        new_x = self.Position[0] + self.Direction[0]
        new_z = self.Position[2] + self.Direction[2]

        if self.currentRotation != self.rotationAngle:
            if self.currentRotation < self.rotationAngle:
                self.currentRotation += 5
            else:
                self.currentRotation -= 5

        #detecc de que el objeto no se salga del area de navegacion
        if(abs(new_x) <= self.DimBoard):
            self.Position[0] = new_x
        else:
            self.Direction[0] *= -1.0
            self.Direction[2] *= -1.0
            self.Position[0] += self.Direction[0]
            if self.currentRotation + 180 >= 360:
                self.rotationAngle = self.currentRotation + 180 - 360
            else:
                self.rotationAngle = 180
        
        if(abs(new_z) <= self.DimBoard):
            self.Position[2] = new_z
        else:
            self.Direction[1] *= -1.0
            self.Direction[2] *= -1.0
            self.Position[2] += self.Direction[2]
            if self.currentRotation + 180 >= 360:
                self.rotationAngle = self.currentRotation + 180 - 360
            else:
                self.rotationAngle = 180

    def draw(self):
        glPushMatrix()
        glTranslatef(self.Position[0], self.Position[1], self.Position[2])
        glRotatef(-90.0, 1.0, 0.0, 0.0)
        glScaled(3,3,3)
        glColor3f(1.0, 1.0, 1.0)
        glRotatef(self.currentRotation, 0.0, 0.0, 1.0)
        self.obj.render()
        glPopMatrix()