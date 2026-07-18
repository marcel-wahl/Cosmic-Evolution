# Radix Vacuum Simulation Suite: Documentation & Readme

This repository contains two verification scripts written in Python to simulate the algorithmic properties of the self-reactive radix vacuum framework. Below is a detailed breakdown of the internal logic (expressed as pseudocode) and the physical interpretation of the program outputs.

---

## 1. Core Vacuum Engine & Hubble Tension Simulation (`hubble_tension_calc.py`)

### Algorithm Description & Pseudocode
This script evaluates the primary state machine of the $D_1$ spacetime metric layer, computes the boundary limits of the $D_2$ and $D_3$ engines via Euler's totient function, and quantifies the macro-scale metric deformation that resolves the cosmological Hubble tension.

```text
FUNCTION d1_step_operator(x_n):
    mod6 = x_n MODULO 6
    exponent = mod6 - 0.5
    step = 3 - (mod6 - 3) * ((-1) POW INT(exponent))
    RETURN step

START SIMULATION:
    // Step 1: Trajectory Verification
    FOR EACH state IN [1, 5, 7, 11]:
        delta = d1_step_operator(state)
        next_state = state + delta
        VERIFY that (next_state MODULO 6) IS 1 OR 5

    // Step 2: Harmonic Saturation Limits
    phi_30 = EULER_TOTIENT(30)   // Yields active channels in D2 engine
    phi_210 = EULER_TOTIENT(210) // Yields quantum capacity in D3 engine

    // Step 3: Quantitative Hubble Tension Resolution
    x_init = 6.0
    x_crit = 211.0
    chi = x_crit / x_init
    
    // Calculate metric compression factor scaled by transcendental damping (2*pi*e)
    delta_metric = LN(chi) / (2 * PI * E)
    
    // Scale early-universe baseline (Planck) to late-universe local domain (SH0ES)
    h0_planck = 67.4
    h0_calculated = h0_planck * (1 + (delta_metric / LN(10)))
    
    PRINT all computed attributes
END SIMULATION