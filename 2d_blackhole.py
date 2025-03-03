import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.colors import LinearSegmentedColormap

# Constants
G = 6.67430e-11  # Gravitational constant (m^3/kg/s^2)
c = 3e8  # Speed of light (m/s)

# Black hole mass (kg)
try:
    user_mass = float(input("Enter the mass of the black hole (in terms of solar masses; e.g, 5): "))
    M = user_mass * 1.989e30 #converting solar mass to kgs

except ValueError:
    print("Invalid! Taking the default mass (5 solar masses)")
    M = 5e30 #default solar mass


Rs = 2 * G * M / c**2  # Schwarzschild radius

# Create a figure
fig, ax = plt.subplots(figsize=(6, 6))
fig.patch.set_facecolor('black')  
ax.set_facecolor('black')  

# Function to create a smooth glow effect around the event horizon
def create_event_horizon(ax, Rs):
    for i in range(1, 6):  # 5 layers for soft gradient effect
        glow = plt.Circle((0, 0), Rs * (1 + i * 0.02), color='darkred', alpha=0.05 * (6 - i), zorder=2)
        ax.add_patch(glow)

    # Actual event horizon (black)
    black_hole = plt.Circle((0, 0), Rs, color='black', zorder=3)
    ax.add_patch(black_hole)

# Add the event horizon with a glow
create_event_horizon(ax, Rs)

# Create Accretion Disk with Gradient
theta_disk = np.linspace(0, 2 * np.pi, 300)
r_inner = 1.5 * Rs
r_outer = 3.5 * Rs
colors = ["red", "orange", "yellow"]
cmap = LinearSegmentedColormap.from_list("accretion", colors, N=100)

# Accretion disk lines
disk_lines = []
for i, r in enumerate(np.linspace(r_inner, r_outer, 60)):  # More rings for density
    x_disk = r * np.cos(theta_disk)
    y_disk = r * np.sin(theta_disk)
    line, = ax.plot(x_disk, y_disk, color=cmap(i / 60), linewidth=1.2, alpha=0.6, zorder=2)  # Thicker lines
    disk_lines.append(line)

# Function to simulate gravitational lensing
def gravitational_lens(x, y, Rs, time):
    """Warp star positions dynamically due to gravitational lensing."""
    r = np.sqrt(x**2 + y**2)
    if r < Rs * 3.0:
        return None, None

    factor = 1 + 0.5 * np.exp(-r / (2 * Rs))  # Base warping
    time_shift = 0.05 * np.sin(time + r / Rs)  # Adds dynamic movement
    x_warped = x * (factor + time_shift)
    y_warped = y * (factor + time_shift)

    return x_warped, y_warped

# Generate Initial Star Positions
num_stars = 2500
x_stars_orig = np.random.uniform(-30 * Rs, 30 * Rs, num_stars)
y_stars_orig = np.random.uniform(-30 * Rs, 30 * Rs, num_stars)
stars, = ax.plot([], [], 'w.', markersize=2, zorder=1)

# Animation Function
def update(frame):
    x_stars = []
    y_stars = []
    for x, y in zip(x_stars_orig, y_stars_orig):
        x_warped, y_warped = gravitational_lens(x, y, Rs, frame * 0.1)
        if x_warped is not None:
            x_stars.append(x_warped)
            y_stars.append(y_warped)

    stars.set_data(x_stars, y_stars)

    # Rotate accretion disk slightly faster
    for i, line in enumerate(disk_lines):
        angle_shift = frame * 0.01 * (i + 1)  # Increased speed
        # Apply Doppler effect by changing color intensity
        line.set_alpha(0.6 + 0.2 * np.sin(frame * 0.05 + (i / 60) * np.pi))  # Brightness variation
        x_disk = (r_inner + (i / 60) * (r_outer - r_inner)) * np.cos(theta_disk + angle_shift)
        y_disk = (r_inner + (i / 60) * (r_outer - r_inner)) * np.sin(theta_disk + angle_shift)
        line.set_data(x_disk, y_disk)

    return stars, *disk_lines

mass_text = f"Black hole mass: {M} in terms of solar masses"

# Setup Animation
ax.set_xlim(-5 * Rs, 5 * Rs)
ax.set_ylim(-5 * Rs, 5 * Rs)
ax.set_xticks([])
ax.set_yticks([])
ax.set_aspect('equal', adjustable='datalim')  # Keep black hole perfectly circular
ax.set_title("Animated 2D Black Hole Simulation", color="white")
ax.set_xlabel(mass_text , color = 'white')

ani = animation.FuncAnimation(fig, update, frames=200, interval=50, blit=True)

# Show the animation
plt.show()
