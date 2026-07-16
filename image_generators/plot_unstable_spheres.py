import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

# Configure scientific plotting style
plt.rcParams.update({
    "text.usetex": False,  # Set to True if you have a local LaTeX distribution installed
    "font.family": "serif",
    "font.size": 11
})

# Define the unstable/composite particles, ordered by their factor value
particles = [
    {"name": r"Muon ($\mu^-$)",         "formula": r"$2^2 = 4$",             "v_r": 1.8, "color": "#17becf"},  # Cyan
    {"name": r"Free Neutron ($n$)",     "formula": r"$2 \cdot 3 = 6$",       "v_r": 2.2, "color": "#bcbd22"},  # Olive
    {"name": r"Neutral Pion ($\pi^0$)", "formula": r"$3^2 = 9$",             "v_r": 2.7, "color": "#9467bd"},  # Purple
    {"name": r"Kaon ($K$)",             "formula": r"$3 \cdot 5 = 15$",      "v_r": 3.4, "color": "#8c564b"},  # Brown
    {"name": r"Tauon ($\tau^-$)",       "formula": r"$2\cdot3\cdot5 = 30$",  "v_r": 4.4, "color": "#e377c2"},  # Pink
    {"name": r"Weak Bosons ($W, Z$)",   "formula": r"$2\cdot3\cdot7 = 42$",  "v_r": 5.2, "color": "#7f7f7f"},  # Gray
    {"name": r"Higgs Boson ($H^0$)",    "formula": r"$2\cdot3\cdot5\cdot7 = 210$", "v_r": 6.8, "color": "#111111"} # Dark Charcoal
]

# Large spacing parameter to prevent text overlaps for small spheres
gap = 4.0

# Dynamically calculate positions so they rest on a baseline (y = 0)
x_positions = []
y_positions = []
current_x = 0.0

for i, part in enumerate(particles):
    r = part["v_r"]
    if i == 0:
        current_x = r
    else:
        current_x += particles[i-1]["v_r"] + gap + r
    
    x_positions.append(current_x)
    y_positions.append(r)

# Calculate dynamic canvas limits to prevent any clipping
max_x = x_positions[-1] + particles[-1]["v_r"] + 2.0
max_y = max(particles, key=lambda x: x["v_r"])["v_r"] * 2.0 + 2.0

# Initialize the canvas with explicit white background and extra width for spacing
fig, ax = plt.subplots(figsize=(16, 5.5), facecolor='white')
ax.set_xlim(-2, max_x)
ax.set_ylim(-4, max_y)
ax.set_aspect('equal')
ax.axis('off')
ax.set_facecolor('white')

# Draw a subtle baseline
ax.plot([-2, max_x], [0, 0], color='#bdc3c7', linestyle='--', linewidth=1.5, zorder=0)

# Draw each particle sphere
for i, part in enumerate(particles):
    r = part["v_r"]
    cx = x_positions[i]
    cy = y_positions[i]
    
    # Generate 3D pseudo-shading using concentric layers
    num_shading_layers = 60
    for j in range(num_shading_layers):
        factor = 1.0 - (j / num_shading_layers)
        layer_r = r * factor
        
        offset = (r - layer_r) * 0.35
        lcx = cx - offset
        lcy = cy + offset
        
        alpha = j / num_shading_layers
        color_rgb = np.array(plt.cm.colors.to_rgb(part["color"]))
        white_rgb = np.array([1.0, 1.0, 1.0])
        mixed_color = color_rgb * (1.0 - alpha) + white_rgb * alpha * 0.8
        
        circle = Circle((lcx, lcy), layer_r, color=mixed_color, zorder=j)
        ax.add_patch(circle)
        
    # Draw outline
    outer_circle = Circle((cx, cy), r, fill=False, edgecolor='#2c3e50', linewidth=1.5, zorder=100)
    ax.add_patch(outer_circle)
    
    # Display the prime factorization formula in the center of the sphere
    font_sz = 9 if r < 3.0 else 11
    ax.text(cx, cy, part["formula"], 
            color='white', ha='center', va='center', 
            fontsize=font_sz, fontweight='bold', zorder=101)
    
    # Place the particle name below the baseline
    ax.text(cx, -1.5, part["name"], 
            ha='center', va='top', fontsize=10, fontweight='bold', color='#2c3e50')

# Ensure the directory exists
output_dir = "images"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

output_filename = os.path.join(output_dir, "unstable_particles_spheres.png")
plt.savefig(output_filename, bbox_inches='tight', dpi=300, transparent=False, facecolor='white')
plt.close()

print(f"Successfully generated: '{output_filename}' with a solid white background!")