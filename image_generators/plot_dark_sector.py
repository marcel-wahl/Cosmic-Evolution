import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

# Set global academic style
plt.style.use('default')
plt.rcParams['font.family'] = 'sans-serif'

# Shared color palette
c_primary = '#1a365d'    # Deep Blue (Structure)
c_secondary = '#3182ce'  # Medium Blue (Phase / Influx)
c_alert = '#e53e3e'      # Red (Entropy Export / High-Energy)
c_grid = '#e2e8f0'       # Light Gray for gridlines
c_text = '#2d3748'       # Dark Slate for labels

# ==============================================================================
# PLOT 1: D4 -> D3 PHASE INFLUX (DARK ENERGY)
# ==============================================================================
def draw_plot_1():
    fig, ax = plt.subplots(figsize=(8, 6), dpi=150, subplot_kw={'aspect': 'equal'})
    fig.patch.set_facecolor('#ffffff')
    ax.set_facecolor('#ffffff')
    ax.set_title(r"1. $D_4 \rightarrow D_3$ Phase Influx (Dark Energy)", fontsize=12, color=c_primary, weight='bold', pad=15)

    # Background division
    ax.axhspan(5, 10, facecolor='#ebf8ff', alpha=0.5, zorder=1)
    ax.axhspan(0, 5, facecolor='#f7fafc', alpha=0.8, zorder=1)
    ax.axhline(5, color='#4a5568', linestyle='--', linewidth=1.5, zorder=2)
    
    ax.text(5.0, 8.5, "D4 BULK\n(Hyper-dimensional Source)", fontsize=10, color=c_secondary, weight='bold', ha='center', zorder=3)
    ax.text(5.0, 1.5, "D3 SPACETIME\n(Holographic Boundary)", fontsize=10, color=c_primary, weight='bold', ha='center', zorder=3)
    ax.text(5.0, 5.2, "Holographic Boundary (Phase Interface)", fontsize=8, color='#718096', style='italic', ha='center', zorder=3)

    # Expansive phase influx trajectories
    np.random.seed(42)
    for x_src in np.linspace(1, 9, 8):
        x_vals = np.linspace(x_src, x_src + np.sin(x_src)*1.8, 100)
        y_vals = np.linspace(7.5, 2.5, 100)
        ax.plot(x_vals, y_vals, color=c_secondary, alpha=0.6, linewidth=1.5, zorder=2)
        
        # Adding flow indicators
        arrow = FancyArrowPatch((x_vals[30], y_vals[30]), (x_vals[70], y_vals[70]),
                                 arrowstyle='->', mutation_scale=12, color=c_secondary, alpha=0.8, zorder=3)
        ax.add_patch(arrow)

    # Labels for physical interpretation
    ax.text(2.2, 6.0, "D4 -> D3 Phase Flow\n(Inherent Metric Pressure)", fontsize=9, color=c_secondary, weight='bold', ha='center')
    ax.text(7.8, 4.0, "Expansive Pressure\n(Observed Dark Energy)", fontsize=9, color=c_primary, weight='bold', ha='center')

    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    for spine in ax.spines.values():
        spine.set_color(c_grid)
    
    plt.tight_layout()
    plt.savefig('dark_sector_1_influx.png', dpi=300, facecolor='#ffffff', edgecolor='none')
    plt.close()

# ==============================================================================
# PLOT 2: ENTROPIC RELAXATION & LOCAL COHERENCE (DARK MATTER)
# ==============================================================================
def draw_plot_2():
    fig, ax = plt.subplots(figsize=(8, 6), dpi=150, subplot_kw={'aspect': 'equal'})
    fig.patch.set_facecolor('#ffffff')
    ax.set_facecolor('#ffffff')
    ax.set_title("2. Entropic Relaxation & Localized Phase-Locking (Dark Matter)", fontsize=12, color=c_primary, weight='bold', pad=15)

    # Grid background representing the coordinate vacuum
    x_grid = np.linspace(0, 10, 11)
    y_grid = np.linspace(0, 10, 11)
    for x in x_grid:
        ax.axvline(x, color='#f7fafc', zorder=1, linewidth=1)
    for y in y_grid:
        ax.axhline(y, color='#f7fafc', zorder=1, linewidth=1)

    # Phase relaxation waves focusing into nodes
    centers = [(3.0, 6.0), (7.0, 4.0), (5.0, 2.5)]
    for cx, cy in centers:
        # Concentric circles representing local gravitational binding / phase coherence
        radii = [0.2, 0.5, 0.9, 1.4]
        for i, r in enumerate(radii):
            circle = plt.Circle((cx, cy), r, color=c_secondary, fill=False, 
                                linestyle='--', alpha=0.7 - (i*0.15), linewidth=1.2, zorder=2)
            ax.add_patch(circle)
        
        # Localized dense core (simulated particle lock)
        ax.scatter(cx, cy, color=c_primary, s=120, zorder=3, edgecolors='white', linewidth=1.5)
        
        # Spiral decay lines representing entropic relaxation toward the center
        theta = np.linspace(0, 4*np.pi, 100)
        r_spiral = np.linspace(1.4, 0.1, 100)
        xs = cx + r_spiral * np.cos(theta)
        ys = cy + r_spiral * np.sin(theta)
        ax.plot(xs, ys, color=c_secondary, alpha=0.3, linewidth=1, zorder=2)

    # Annotation of physics
    ax.text(3.0, 8.0, "Entropic Phase Decay\n(Relaxation)", fontsize=9, color=c_secondary, weight='bold', ha='center')
    ax.text(7.0, 1.8, "Stable Coordinate Lock\n(Localized Dark Matter Mass)", fontsize=9, color=c_primary, weight='bold', ha='center')

    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    for spine in ax.spines.values():
        spine.set_color(c_grid)

    plt.tight_layout()
    plt.savefig('dark_sector_2_relaxation.png', dpi=300, facecolor='#ffffff', edgecolor='none')
    plt.close()

# ==============================================================================
# PLOT 3: BLACK HOLE SINK & INFORMATION EXPORT
# ==============================================================================
def draw_plot_3():
    fig, ax = plt.subplots(figsize=(8, 6), dpi=150, subplot_kw={'aspect': 'equal'})
    fig.patch.set_facecolor('#ffffff')
    ax.set_facecolor('#ffffff')
    ax.set_title("3. Thermodynamic Sink & Phase Evaporation", fontsize=12, color=c_primary, weight='bold', pad=15)

    bh_x, bh_y = 5.0, 4.0

    # Draw accretion disk and infalling phase streams
    for r in np.linspace(0.8, 3.0, 5):
        circle = plt.Circle((bh_x, bh_y), r, color=c_secondary, fill=False, alpha=0.25, zorder=2)
        ax.add_patch(circle)

    # Event Horizon
    bh_circle = plt.Circle((bh_x, bh_y), 0.7, facecolor='#1a202c', edgecolor='#4a5568', linewidth=2, zorder=4)
    ax.add_patch(bh_circle)
    # Singular Core
    ax.scatter(bh_x, bh_y, color='#000000', s=100, zorder=5)

    # Spiral infalling trajectories
    for angle in np.linspace(0, 2*np.pi, 8, endpoint=False):
        dx, dy = np.cos(angle)*2.2, np.sin(angle)*2.2
        arrow_in = FancyArrowPatch((bh_x + dx, bh_y + dy), (bh_x + dx*0.3, bh_y + dy*0.3),
                                   arrowstyle='->', mutation_scale=10, color=c_secondary, alpha=0.6, zorder=3)
        ax.add_patch(arrow_in)

    # Information Export/Phase Evaporation (Highly energetic wavy lines leaving outward/upward)
    for angle in [np.pi/3, np.pi/2, 2*np.pi/3, 7*np.pi/6, 11*np.pi/6]:
        dx, dy = np.cos(angle), np.sin(angle)
        t_vals = np.linspace(0.7, 3.5, 120)
        # Wave modulation representing non-baryonic information carrier
        wave_x = bh_x + dx * t_vals + np.sin(t_vals*20)*0.1 * (-dy)
        wave_y = bh_y + dy * t_vals + np.sin(t_vals*20)*0.1 * dx
        ax.plot(wave_x, wave_y, color=c_alert, alpha=0.8, linewidth=1.5, zorder=5)
        
        # Direct Arrow heads
        arrow_out = FancyArrowPatch((wave_x[-15], wave_y[-15]), (wave_x[-1], wave_y[-1]),
                                     arrowstyle='->', mutation_scale=10, color=c_alert, zorder=5)
        ax.add_patch(arrow_out)

    # Labels
    ax.text(bh_x, bh_y - 1.2, "Radix-210 Phase Sink\n(Event Horizon)", fontsize=9, color='#1a202c', weight='bold', ha='center', zorder=4)
    ax.text(bh_x + 1.8, bh_y + 2.5, "Information Export\n(Holographic Phase Evaporation)", fontsize=9, color=c_alert, weight='bold', ha='left', zorder=5)

    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    for spine in ax.spines.values():
        spine.set_color(c_grid)

    plt.tight_layout()
    plt.savefig('dark_sector_3_blackhole.png', dpi=300, facecolor='#ffffff', edgecolor='none')
    plt.close()

# Execute all plot generations
if __name__ == "__main__":
    draw_plot_1()
    draw_plot_2()
    draw_plot_3()
    print("Successfully generated all three separate Dark Sector plots!")