import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Set light, professional academic style
plt.style.use('default')
fig = plt.figure(figsize=(15, 11), dpi=150)
fig.patch.set_facecolor('#ffffff')

# Color palette optimized for high contrast on white background
c_primary = '#1a365d'    # Deep Blue (Structure / Grid)
c_secondary = '#3182ce'  # Medium Blue (Phases / Channels)
c_alert = '#e53e3e'      # Red (Singularity / Collapse Point)
c_grid = '#e2e8f0'       # Light Gray for gridlines
c_text = '#2d3748'       # Dark Slate for labels

# ==============================================================================
# SUBPLOT 1: D4 -> D0 INFLUX (The Phase Fracture)
# ==============================================================================
ax1 = fig.add_subplot(221)
ax1.set_facecolor('#ffffff')
ax1.set_title(r"1. $D_4 \rightarrow D_0$ Influx & Spacetime Fracture", fontsize=13, color=c_primary, weight='bold', pad=15)

# Construction of the "fracture line"
np.random.seed(42)
y_crack = np.linspace(-10, 10, 200)
x_crack = np.sin(y_crack) * 0.8 + np.random.normal(0, 0.12, 200)
ax1.plot(x_crack, y_crack, color=c_alert, linewidth=2.5, alpha=0.9, label="D4 Spacetime Fracture")

# Emerging massless D0 phase patterns (field lines)
for i in range(25):
    y_start = np.random.choice(y_crack)
    x_start = x_crack[np.abs(y_crack - y_start).argmin()]
    direction = np.random.choice([-1, 1])
    x_wave = np.linspace(x_start, x_start + direction * np.random.uniform(3, 8), 100)
    y_wave = y_start + np.sin(x_wave * 4.5) * 0.25
    alpha = np.random.uniform(0.3, 0.7)
    ax1.plot(x_wave, y_wave, color=c_secondary, linestyle=':', alpha=alpha)

ax1.set_xlim(-10, 10)
ax1.set_ylim(-10, 10)
ax1.grid(True, color=c_grid, linestyle='--')
ax1.set_xlabel("Phase Offset", color=c_text)
ax1.set_ylabel("Singularity Axis", color=c_text)
ax1.legend(loc="upper right", framealpha=0.8, edgecolor=c_grid)

# ==============================================================================
# SUBPLOT 2: D1 LINEAR VACUUM (Radix-6 Grid)
# ==============================================================================
ax2 = fig.add_subplot(222)
ax2.set_facecolor('#ffffff')
ax2.set_title(r"2. $D_1$ Linear Vacuum ($\Pi_2 = 6$)", fontsize=13, color=c_primary, weight='bold', pad=15)

# Main 1D dimension axis
ax2.axhline(0, color='#718096', linewidth=2)

# Radix-6 nodes and coprimality channels (6n +/- 1)
x_max = 35
markers_6 = np.arange(0, x_max + 1, 6)
channels_active = []
for m in markers_6:
    if m - 1 > 0: channels_active.append(m - 1)
    if m + 1 <= x_max: channels_active.append(m + 1)

# Plot Radix-6 nodes (structural boundaries)
ax2.scatter(markers_6, np.zeros_like(markers_6), color=c_alert, s=120, zorder=5, 
            edgecolors='#2d3748', linewidth=1.5, label=r"Radix-6 Nodes ($\Pi_2$)")
# Plot active resonance channels
ax2.scatter(channels_active, np.zeros_like(channels_active), color=c_secondary, s=70, zorder=4, 
            edgecolors='none', label=r"Active Channels ($6n \pm 1$)")

# Wave harmonics (underlying physical phase oscillations)
x_vals = np.linspace(0, x_max, 1000)
y_vals = np.sin(2 * np.pi * x_vals / 6) * 0.15
ax2.plot(x_vals, y_vals, color=c_primary, alpha=0.25, linestyle='--')

ax2.set_xlim(-1, x_max + 1)
ax2.set_ylim(-1, 1)
ax2.get_yaxis().set_visible(False)
ax2.grid(True, axis='x', color=c_grid)
ax2.set_xlabel("Dimensional Coordinate $x$", color=c_text)
ax2.legend(loc="upper right", framealpha=0.8, edgecolor=c_grid)

# ==============================================================================
# SUBPLOT 3: D2 PLANAR DISK (Radix-30 Polar Spectrum)
# ==============================================================================
ax3 = fig.add_subplot(223, projection='polar')
ax3.set_facecolor('#ffffff')
ax3.set_title(r"3. $D_2$ Planar Disk ($\Pi_3 = 30$)", fontsize=13, color=c_primary, weight='bold', pad=30)

# Concentric boundary rings of the Radix-30 engine
radii = [10, 20, 30]
for r in radii:
    circle = np.linspace(0, 2*np.pi, 200)
    ax3.plot(circle, np.full_like(circle, r), color='#cbd5e0', linestyle='-', linewidth=1.2)

# The 8 active channels (after the inertial shift from 1 -> 31)
# Phi_active = {7, 11, 13, 17, 19, 23, 29, 31}
active_channels_30 = np.array([7, 11, 13, 17, 19, 23, 29, 31])
angles = (active_channels_30 / 30.0) * 2 * np.pi

# Draw polar vectors for active non-interfering tracks
for angle, channel in zip(angles, active_channels_30):
    ax3.plot([angle, angle], [0, 30], color=c_secondary, linewidth=2, alpha=0.8)
    ax3.scatter(angle, 30, color=c_primary, s=80, zorder=5)
    # Positioning text with custom padding to avoid overlapping with plot boundaries
    ax3.text(angle, 35, f"{channel}", color=c_text, fontsize=10, ha='center', va='center', weight='bold')

ax3.set_rticks(radii)
ax3.set_yticklabels([]) # Hide distance labels to clear the layout
ax3.grid(True, color=c_grid)

# ==============================================================================
# SUBPLOT 4: D3 SPHERICAL VACUUM (Radix-210 Resonance Field)
# ==============================================================================
ax4 = fig.add_subplot(224, projection='3d')
ax4.set_facecolor('#ffffff')
ax4.set_title(r"4. $D_3$ Spherical Resonance Field ($\Pi_4 = 210$)", fontsize=13, color=c_primary, weight='bold', pad=20)

# Create 3D spherical grid
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x_sph = np.outer(np.cos(u), np.sin(v))
y_sph = np.outer(np.sin(u), np.sin(v))
z_sph = np.outer(np.ones(np.size(u)), np.cos(v))

# Render sphere body with semi-transparent shading
ax4.plot_surface(x_sph, y_sph, z_sph, color='#f7fafc', alpha=0.5, edgecolor='#e2e8f0', rstride=8, cstride=8)

# Map selected active resonance boundaries (representing the 48 active channels)
theta_channels = np.linspace(0, 2 * np.pi, 12)
phi_channels = np.linspace(0, np.pi, 8)

for theta in theta_channels:
    x_line = np.cos(theta) * np.sin(v)
    y_line = np.sin(theta) * np.sin(v)
    z_line = np.cos(v)
    ax4.plot(x_line, y_line, z_line, color=c_primary, alpha=0.7, linewidth=1.3)

for phi in phi_channels:
    x_line = np.cos(u) * np.sin(phi)
    y_line = np.sin(u) * np.sin(phi)
    z_line = np.full_like(u, np.cos(phi))
    ax4.plot(x_line, y_line, z_line, color=c_secondary, alpha=0.5, linewidth=1.0)

# Disable 3D box axes for a clean, focused presentation
ax4.set_axis_off()

# ==============================================================================
# LAYOUT OPTIMIZATION & EXPORT
# ==============================================================================
# Manual padding adjustment to completely prevent overlaps
plt.subplots_adjust(left=0.05, right=0.95, bottom=0.08, top=0.92, hspace=0.32, wspace=0.20)

# Save as high-resolution PNG for publication
plt.savefig('cosmic_cascade_fixed.png', dpi=300, facecolor=fig.get_facecolor(), edgecolor='none')
print("High-quality figure successfully exported as 'cosmic_cascade_fixed.png'!")
plt.show()