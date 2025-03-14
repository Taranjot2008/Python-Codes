import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
import random

# Function to generate stars
def generate_stars(num_stars):
    stars = []
    for _ in range(num_stars):
        # Randomly position stars in a 3D space, ensuring they are not too close to the black hole
        x = random.uniform(-5, 5)
        y = random.uniform(-5, 5)
        z = random.uniform(-10, -3)  # Start further back
        stars.append([x, y, z])
    return stars

# Function to draw stars
def draw_stars(stars):
    glBegin(GL_POINTS)
    glColor3f(1, 1, 1)  # White color for stars
    for star in stars:
        glVertex3f(star[0], star[1], star[2])
    glEnd()

# Function to draw the black hole
def draw_black_hole():
    glColor3f(0, 0, 0)  # Black color
    quadric = gluNewQuadric()
    gluSphere(quadric, 0.2, 32, 32)  # Draw a sphere for the black hole
    gluDeleteQuadric(quadric)

# Function to draw the event horizon glow
def draw_event_horizon():
    glColor3f(1, 1, 0)  # Yellow color for the glow
    glBegin(GL_LINE_LOOP)
    num_segments = 100
    radius = 0.25  # Radius of the event horizon
    for i in range(num_segments):
        angle = 2 * np.pi * i / num_segments
        x = radius * np.cos(angle)
        y = radius * np.sin(angle)
        glVertex3f(x, y, 0)  # Draw in the XY plane
    glEnd()

# Function to draw the accretion disk in the XY plane
def draw_accretion_disk_xy():
    glColor3f(1, 1, 0)  # Yellow color for the accretion disk
    quadric = gluNewQuadric()
    gluQuadricNormals(quadric, GLU_SMOOTH)

    # Draw the disk in the XY plane
    glPushMatrix()
    glTranslatef(0.0, 0.0, 0)  # Position the disk at the center
    gluDisk(quadric, 0.25, 0.35, 32, 1)  # Draw a disk with inner radius 0.25 and outer radius 0.35
    glPopMatrix()

    gluDeleteQuadric(quadric)

# Function to draw the accretion disk in the XZ plane
def draw_accretion_disk_xz():
    glColor3f(1, 1, 0)  # Yellow color for the accretion disk
    quadric = gluNewQuadric()
    gluQuadricNormals(quadric, GLU_SMOOTH)

    # Draw the disk in the XZ plane
    glPushMatrix()
    glRotatef(90, 1, 0, 0)  # Rotate 90 degrees around the X-axis to position in the XZ plane
    glTranslatef(0.0, 0.0, 0)  # Position the disk at the center
    gluDisk(quadric, 0.25, 0.35, 32, 1)  # Draw a disk with inner radius 0.25 and outer radius 0.35
    glPopMatrix()

    gluDeleteQuadric(quadric)

# Main function to set up the OpenGL context and run the loop
def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    num_stars = 1000  # Number of stars in the starfield
    stars = generate_stars(num_stars)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        draw_stars(stars)  # Draw the starfield
        draw_black_hole()  # Draw the black hole
        draw_event_horizon()  # Draw the event horizon glow
        draw_accretion_disk_xy()  # Draw the solid accretion disk in the XY plane
        draw_accretion_disk_xz()  # Draw the solid accretion disk in the XZ plane

        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()