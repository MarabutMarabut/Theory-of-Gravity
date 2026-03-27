# Note: For full solar-system fits, adjust the Ambient Multiplier 
# and tau_T per body phase state (e.g., tau_T = f(T_core))
#
# For the complete 38-body interactive 3D Volumetric Profiler, 
# visit the EFM GitHub Repository: 
# https://github.com/MarabutMarabut/Theory-of-Gravity/

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# --- EFM Core Parameters ---
G = 6.67430e-11   # Gravitational Constant
alpha = 4.183     # EFM Geometric Integration Factor (~4*pi/3)
rho_eff = 5515.0  # Effective Density (e.g., Earth)
tau_T = 0.98      # Thermodynamic Impedance (Rocky Body)
omega = 0.0       # Rotational Velocity (Set >0 for Gas Giants)
D_ref_mult = 1.0  # Ambient Flux Multiplier (D_ref**0.21 for Small Bodies)

def marabut_gravity_field(x, y, z):
  r = np.sqrt(x**2 + y**2 + z**2)
  r[r == 0] = 1e-9 

  # 1. THE INTAKE (Local Volumetric Engine)
  intake_force = (alpha * G) * rho_eff * r * tau_T * D_ref_mult

  # 2. THE RESISTANCE (Centrifugal offset for fluid Gas Giants only)
  v_rot = omega * r
  resistance_force = (v_rot**2) / r

  # 3. NET ACCELERATION
  g_net = intake_force - resistance_force

  # 4. VECTOR MAPPING (Inward Hydrodynamic Flow)
  u_rad = (-g_net / r) * x
  v_rad = (-g_net / r) * y
  w_rad = (-g_net / r) * z
  
  # 5. ROTATIONAL COMPONENT (Optional magnetic exhaust tracking)
  u_rot = -omega * y
  v_rot = omega * x
  w_rot = 0

  return (u_rad + u_rot), (v_rad + v_rot), (w_rad + w_rot)

# PLOTTING
n = 10
x, y, z = np.meshgrid(np.linspace(-2, 2, n), 
                      np.linspace(-2, 2, n), 
                      np.linspace(-2, 2, n))
u, v, w = marabut_gravity_field(x, y, z)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.quiver(x, y, z, u, v, w, length=0.4, normalize=True, cmap='plasma')
ax.set_title("EFM Vector Field: Hydrodynamic Vacuum Flux")

# Save the figure so the LaTeX file can see it
plt.savefig('marabut_3d_flow.png') 
plt.show()
