import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

# Configure scientific plotting style
plt.rcParams.update({
    "text.usetex": False,  # Set to True if you have a local LaTeX distribution installed
    "font.family": "serif",
    "font.size": 12
})

# Define the 4 stable fundamental particles and their prime radii
particles = [
    {"name": r"Electron ($e^-$)", "p": 2, "color": "#2ca02c"},  # Green
    {"name": r"Quark ($q$)",       "p": 3, "color": "#1f77b4"},  # Blue
    {"name": r"Proton ($p^+$)",    "p": 5, "color": "#ff7f0e"},  # Orange
    {"name": r"Photon ($\gamma$)", "p": 7, "color": "#d62728"}   # Red
]

# Spacing parameter between the spheres
gap = 1.5

# Dynamically calculate positions so they rest on a baseline (y = 0)
# and do not overlap regardless of their size
x_positions = []
y_positions = []
current_x = 0.0

for i, part in enumerate(particles):
    r = part["p"]
    if i == 0:
        current_x = r
    else:
        # Distance = previous radius + gap + current radius
        current_x += particles[i-1]["p"] + gap + r
    
    x_positions.append(current_x)
    # y = r forces the bottom edge of every sphere to touch the baseline y = 0
    y_positions.append(r)

# Calculate dynamic canvas limits to prevent any clipping
max_x = x_positions[-1] + particles[-1]["p"] + 2.0
max_y = max(particles, key=lambda x: x["p"])["p"] * 2.0 + 2.0

# Initialize the canvas with a proportional aspect ratio and explicit white background
fig, ax = plt.subplots(figsize=(12, 5), facecolor='white')
ax.set_xlim(-2, max_x)
ax.set_ylim(-4, max_y)
ax.set_aspect('equal')
ax.axis('off')

# Set background of the axes to white as well
ax.set_facecolor('white')

# Draw a subtle baseline to emphasize the flush alignment
ax.plot([-2, max_x], [0, 0], color='#bdc3c7', linestyle='--', linewidth=1.5, zorder=0)

# Draw each particle sphere
for i, part in enumerate(particles):
    r = part["p"]
    cx = x_positions[i]
    cy = y_positions[i]  # Center is at height r, so bottom is at y=0
    
    # Generate 3D pseudo-shading using concentric layers
    num_shading_layers = 50
    for j in range(num_shading_layers):
        factor = 1.0 - (j / num_shading_layers)
        layer_r = r * factor
        
        # Shift layer center towards the top-left for 3D lighting direction
        offset = (r - layer_r) * 0.35
        lcx = cx - offset
        lcy = cy + offset
        
        # Mix the primary color with white to simulate a smooth radial gradient
        alpha = j / num_shading_layers
        color_rgb = np.array(plt.cm.colors.to_rgb(part["color"]))
        white_rgb = np.array([1.0, 1.0, 1.0])
        mixed_color = color_rgb * (1.0 - alpha) + white_rgb * alpha * 0.8
        
        circle = Circle((lcx, lcy), layer_r, color=mixed_color, zorder=j)
        ax.add_patch(circle)
        
    # Draw a crisp outline around each sphere
    outer_circle = Circle((cx, cy), r, fill=False, edgecolor='#2c3e50', linewidth=1.5, zorder=100)
    ax.add_patch(outer_circle)
    
    # Display the prime generator value in the center of the sphere
    ax.text(cx, cy, f"$p = {r}$", 
            color='white', ha='center', va='center', 
            fontsize=14, fontweight='bold', zorder=101)
    
    # Place the particle name below the baseline
    ax.text(cx, -1.5, part["name"], 
            ha='center', va='top', fontsize=12, fontweight='bold', color='#2c3e50')

# Save the final schematic as a high-resolution PNG with a solid white background
output_filename = "fundamental_particles_spheres.png"
plt.savefig(output_filename, bbox_inches='tight', dpi=300, transparent=False, facecolor='white')
plt.close()

print(f"Successfully generated: '{output_filename}' with a solid white background!")