import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
import random

# Constants
G = 6.674e-11  # Gravitational constant
c = 3e8  # Speed of light
SOLAR_MASS = 1.989e30  # Mass of the Sun in kg
angle = 0 #rotation angle
num_segments = 100

# Get user input for black hole mass
mass = float(input("Enter black hole mass in solar masses: ") or 10)  # Default: 10 solar masses
mass_kg = mass * SOLAR_MASS  # Convert to kg
radius = (2 * G * mass_kg) / (c ** 2)  # Schwarzschild radius

print(f"Schwarzschild Radius: {radius:.2f} meters (scaled for visualization)")

# Scaling factor for visualization (since real radius is too small)
scaled_radius = 1.5  # Adjust as needed

# Sphere resolution
SPHERE_SLICES = 60
SPHERE_STACKS = 60

# Generate starfield
NUM_STARS = 1000
stars = [(random.uniform(-6, 6), random.uniform(-6, 6), random.uniform(-10, -3)) for _ in range(NUM_STARS)]

def draw_starfield():
    glColor3f(1, 1, 1)
    glPointSize(1.5)
    glBegin(GL_POINTS)
    for star in stars:
        glVertex3f(*star)
    glEnd()

def draw_sphere(radius, slices, stacks):
    for i in range(stacks):
        lat0 = np.pi * (-0.5 + (i / stacks))
        lat1 = np.pi * (-0.5 + ((i + 1) / stacks))
        z0, zr0 = np.sin(lat0), np.cos(lat0)
        z1, zr1 = np.sin(lat1), np.cos(lat1)

        glBegin(GL_TRIANGLE_STRIP)
        for j in range(slices + 1):
            lng = 2 * np.pi * (j / slices)
            x, y = np.cos(lng), np.sin(lng)

            glColor3f(0, 0, 0)
            glVertex3f(x * zr0 * radius, y * zr0 * radius, z0 * radius)
            glVertex3f(x * zr1 * radius, y * zr1 * radius, z1 * radius)
        glEnd()

def draw_border(radius):
    glColor3f(0.9, 0.2, 0.2)
    glLineWidth(0.2)
    glBegin(GL_LINE_LOOP)
    for i in range(360):
        angle = np.radians(i)
        glVertex3f(np.cos(angle) * radius * 1.02, np.sin(angle) * radius * 1.02, 0)
    glEnd()

def resize(width, height):
    global stars
    if height == 0:
        height = 1
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(50, (width / height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslatef(0.0, 0.0, -7)

    stars = [(random.uniform(-width/100, width/100), random.uniform(-height/100, height/100), random.uniform(-10, -3)) for _ in range(NUM_STARS)]

def draw_accretion_disk():
    global angle
    glPushMatrix()
    glRotatef(angle, 0, 1, 0)  # Rotate around Y-axis
    
    glBegin(GL_TRIANGLE_STRIP)
    for i in range(num_segments + 1):
        theta = (i / num_segments) * 2 * np.pi
        outer_x = 3.5 * np.cos(theta)
        outer_z = 3.5 * np.sin(theta)
        inner_x = 1.5 * 1.2 * np.cos(theta)
        inner_z = 1.5 * 1.2 * np.sin(theta)
        
        # Color gradient effect
        glColor3f(1, 0.5, 0)  # Orange outer ring
        glVertex3f(outer_x, 0, outer_z)
        glColor3f(1, 1, 1)  # White inner ring (hotter region)
        glVertex3f(inner_x, 0, inner_z)
    
    glEnd()
    glPopMatrix()

def main():
    pygame.init()
    display = (1000, 800)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL | RESIZABLE)
    resize(*display)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == VIDEORESIZE:
                resize(event.w, event.h)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        draw_starfield()
        draw_sphere(scaled_radius, SPHERE_SLICES, SPHERE_STACKS)
        draw_border(scaled_radius)
        draw_accretion_disk()

        angle += 1 
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
