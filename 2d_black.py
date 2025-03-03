import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

# Constants
G = 6.67430e-11  # Gravitational constant (m^3/kg/s^2)
c = 3e8  # Speed of light (m/s)
# Mass of the black hole (kg) - Approx. Sun's mass

try:
    user_mass = float(input("Enter the mass of the blackhole (in terms of solar masses; e.g, 5): "))
    M = user_mass * 1.989e30 #converting the solar masses to kgs

except ValueError:
    print("Invalid! taking the default mass (5 solar masses)")
    M = 5e30 #mass in kgs(default)


# Calculate Schwarzschild radius
Rs = 2 * G * M / c**2

# Create a figure
fig, ax = plt.subplots(figsize=(6, 6))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')

# Draw Event Horizon
black_hole = plt.Circle((0, 0), Rs, color='black', label="Event Horizon")
ax.add_patch(black_hole)

# Simulate light bending effect (gravitational lensing)
'''theta = np.linspace(0, 2 * np.pi, 300)
r = Rs * 2  # Set initial radius for lensing effect
for i in range(5):  # Create multiple light paths
    r += Rs * 0.5
    x = r * np.cos(theta)
    y = r * np.sin(theta) * (1 + 0.3 * np.exp(-r/Rs))  # Warping effect
    ax.plot(x, y, color='yellow', alpha=0.6, linewidth=0.7)'''

#Accretion Disk
theta_disk = np.linspace(0, 2*np.pi, 300)
r_inner = 1.5*Rs
r_outer = 3.5*Rs

for r in np.linspace(r_inner, r_outer, 30):
    x_disk = r * np.cos(theta_disk)
    y_disk = r * np.sin(theta_disk)
    ax.plot(x_disk, y_disk, color=(1,0,0,0.5), linewidth = 0.5)

#stars in the background
num_stars = 30000

x_stars = []
y_stars = []

for _ in range(num_stars):
    while True:
        x = np.random.uniform(-100 * Rs, 100 * Rs)
        y = np.random.uniform(-100 * Rs, 100 * Rs)
        r = np.sqrt(x**2 + y**2)

        #avoid getting stars on the event horizon and in front
        if r > Rs * 3.5:
            x_stars.append(x)
            y_stars.append(y)
            break


ax.scatter(x_stars, y_stars, color = 'white', s=1)

#warping effect of light around the black hole
theta = np.linspace(0, 2*np.pi, 300)

def light_bending_path(r, theta, Rs):

    #Deflection using Einstein's Formula

    deflection = 1 / (1 + np.exp((r - 1.5 * Rs) / Rs))
    x = r * np.cos(theta)
    y = r * np.sin(theta) * deflection
    return x, y

for i in range(8):
    r = Rs * (2 + i*0.4)
    x,y = light_bending_path(r, theta, Rs)
    ax.plot(x, y, color = 'yellow', alpha = 0.7, linewidth = 0.8)

# Custom gradient colormap for disk
colors = ["red", "orange", "yellow"]
cmap = LinearSegmentedColormap.from_list("accretion", colors, N=100)

# Apply gradient to accretion disk
for i, r in enumerate(np.linspace(r_inner, r_outer, 50)):
    x_disk = r * np.cos(theta_disk)
    y_disk = r * np.sin(theta_disk)
    ax.plot(x_disk, y_disk, color=cmap(i / 30), linewidth=0.6, alpha=0.8)




# Labels and visualization setup
ax.set_xlim(-5 * Rs, 5 * Rs)
ax.set_ylim(-5 * Rs, 5 * Rs)
ax.set_xlabel("Distance (m)", color = 'white')
ax.set_ylabel("Distance (m)", color = 'white')
ax.set_title("2D Black Hole Visualization", color = 'white')
ax.set_aspect('equal', adjustable='datalim')
ax.set_xticks([])
ax.set_yticks([])
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

# Show the plot
plt.show()