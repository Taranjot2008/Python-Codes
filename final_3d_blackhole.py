import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
import random

rotation_angle = 0  # Track rotation
max_rotation = 45   # Stop rotating after 45 degrees

# Define the vertices of the accretion disk
def create_accretion_disk(num_particles):
    particles = []
    for _ in range(num_particles):
        angle = random.uniform(0, 2 * np.pi)
        radius = random.uniform(0.5, 1.0)  # Random radius for variation
        x = radius * np.cos(angle)
        y = radius * np.sin(angle)
        z = random.uniform(-0.1, 0.1)  # Small variation in height
        particles.append((x, y, z))
    return particles

# Function to generate stars
def generate_stars(num_stars):
    stars = []
    for _ in range(num_stars):
        # Randomly position stars in a 3D space
        x = random.uniform(-5, 5)
        y = random.uniform(-5, 5)
        z = random.uniform(-10, 0)  # Start further back
        stars.append([x, y, z])
    return stars

# Function to draw stars
def draw_stars(stars):
    glBegin(GL_POINTS)
    glColor3f(0.6, 0.6, 0.6)  # White color for stars
    for star in stars:
        glVertex3f(star[0], star[1], star[2])
    glEnd()


# Function to draw the black hole
def draw_black_hole():
    glColor3f(0, 0, 0)  # Black color
    quadric = gluNewQuadric()
    gluSphere(quadric, 0.30, 32, 32)  # Draw a sphere for the black hole
    gluDeleteQuadric(quadric)

# Function to draw the event horizon glow
def draw_event_horizon():
    glColor3f(1, 1, 0)  # Yellow color for the glow
    glBegin(GL_LINE_LOOP)
    num_segments = 100
    radius = 0.31  # Radius of the event horizon
    for i in range(num_segments):
        angle = 2 * np.pi * i / num_segments
        x = radius * np.cos(angle)
        y = radius * np.sin(angle)
        glVertex3f(x, y, 0)  # Draw in the XY plane
    glEnd()

# Function to draw the accretion disk using gluDisk
def draw_accretion_disk():
    quadric = gluNewQuadric()
    gluQuadricNormals(quadric, GLU_SMOOTH)

    #disk in XY plane
    glColor3f(0.9, 0.2, 0)  # Forbius color for the accretion disk
    glPushMatrix()
    glTranslatef(0.0, 0.0, 0)  # Position the disk at the center
    gluDisk(quadric, 0.31, 0.65, 32, 1)  # Draw a disk with inner radius 0.45 and outer radius 0.90
    glPopMatrix()

    #disk in XZ plane
    glColor3f(0.9, 0.5, 0)  # sorbus color for the accretion disk
    glPushMatrix()
    glRotatef(90, 1, 0, 0) #rotating the disk by an angle of 90 about the x-axis
    glTranslatef(0.0, 0.0, 0)  # Position the disk at the center
    gluDisk(quadric, 0.65, 1.40, 32, 1)  # Draw a disk with inner radius 0.45 and outer radius 0.90
    glPopMatrix()
    
    gluDeleteQuadric(quadric)

'''# Function to draw the accretion disk
def draw_accretion_disk(particles):
    glColor3f(1, 1, 0)  # Yellow color for the disk
    glBegin(GL_POINTS)
    for particle in particles:
        glVertex3fv(particle)
    glEnd()'''

#Avoid the stretching of the black hole with full screen
'''def resize_window(width, height):
    if height == 0:  # Prevent division by zero
        height = 1
    glViewport(0, 0, width, height)  # Update the viewport
    glMatrixMode(GL_PROJECTION)  # Switch to the projection matrix
    glLoadIdentity()  # Load the identity matrix
    gluPerspective(45, (width / height), 0.1, 50.0)  # Update the perspective
    glMatrixMode(GL_MODELVIEW)  # Switch back to the modelview matrix'''
    
def resize(width, height):
    size = min(width, height)
    glViewport((width - size) // 2, (height - size) // 2, size, size)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, 1.0, 0.1, 100.0)  # Keep aspect ratio fixed at 1.0
    glMatrixMode(GL_MODELVIEW)


# Main function to set up the OpenGL context and run the loop
def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL | RESIZABLE)
    glTranslatef(0.0, 0.0, -5)

    glEnable(GL_DEPTH_TEST)

    num_stars = 1000  # Number of stars in the starfield
    stars = generate_stars(num_stars)

    num_particles = 500
    particles = create_accretion_disk(num_particles)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == VIDEORESIZE: #handle window resize
                resize(event.w, event.h)

        #clear color and depth buffers
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)


        glRotatef(0.001,1,0,0)

        draw_stars(stars)  # Draw the starfield
        draw_black_hole()  # Draw the black hole
        draw_event_horizon()  # Draw the event horizon glow
        draw_accretion_disk()

        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()