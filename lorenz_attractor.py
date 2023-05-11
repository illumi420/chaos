import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import funcs
from datetime import datetime 


print() # ascii_attractor greeting
print(funcs.ascii_art())


WIDTH, HEIGHT, DPI = 1000, 750, 100

# Lorenz paramters and initial conditions.

# Constants:
sigma, rho, beta = 10, 28, 2.667 
""" 
sigma(Prandtl number) σ : is the ratio of momentum diffusivity (kinematic viscosity) to thermal diffusivity.
It is used in fluids and flow rates to signify the rate of heat transfer.

rho(Rayleigh number divided by the critical Rayleigh number) ρ: is typically associated with density. 
However, here the 'rho' value is the Rayleigh number, a measure of the instability of a layer of fluid 
(due to differences of temperature and density at the top and bottom). 
We use it to describe natural convection and heat transfer by natural convection.

beta(geometric factor) β: is the measure of compressibility which is the measure of relative volume change of a fluid.

"""

# Initial Conditions values:
u0, v0, w0 = 0, 1, 1.05
"""
u0: is proportional to the rate of convection x.
v0: is proportional to the horizontal temperature variation y.
w0: is proportional to the vertical temperature variation z.
"""

# Maximum time point and total number of time points.
"""
The equations relate the properties of a two-dimensional fluid layer uniformly warmed from below and cooled from above. 
In particular, the equations describe the rate of change of three quantities with respect to time.
"""
tmax, n = 100, 10000


# Integrating User-Input to the orginal code, for manipulating the Initial Conditions values.

graphs_path = (funcs.GRAPHS_PATH)
file_name = f"{graphs_path}/lorenz"

value = funcs.menu()

if value == "2":
    u0, v0, w0 = funcs.hardwareInitConditions()
    file_name += f"_cpu={u0}-mem={v0}-net={w0}"

elif value == "3":    
    u0, v0, w0, location = funcs.weatherInitConditions()
    file_name += f"_{location}_temp={u0}-humi={v0}-wind={w0}"
    
elif value == "4":
    u0, v0, w0 = funcs.manual_randomInitConditions()
    
    if funcs.random_flag:
        file_name += f"_random_x={u0}-y={v0}-z={w0}"
    else:    
        file_name += f"_x={u0}-y={v0}-z={w0}"


funcs.selection_msg(value,u0,v0,w0)


def lorenz(t, X, sigma, beta, rho):
    """The Lorenz equations."""
    u, v, w = X
    up = sigma*(v - u)
    vp = u*(rho-w) - v
    wp = u*v  - beta*w 
    return up, vp, wp


# Integrate the Lorenz equations.
soln = solve_ivp(lorenz, (0, tmax), (u0, v0, w0), args=(sigma, beta, rho),
                 dense_output=True)
# Interpolate solution onto the time grid, t.
t = np.linspace(0, tmax, n)
x, y, z = soln.sol(t)


# Plot the Lorenz attractor using a Matplotlib 3D projection.
fig = plt.figure(facecolor='k', figsize=(WIDTH/DPI, HEIGHT/DPI))
ax = fig.add_subplot(projection='3d')
ax.set_facecolor('k')
fig.subplots_adjust(left=0, right=1, bottom=0, top=1)


# Make the line multi-coloured by plotting it in segments of length s which
# change in colour across the whole time series.

s = 9
colormap = funcs.mood()
cmap, mood_name = colormap
for i in range(0,n-s,s):
    ax.plot(x[i:i+s+1], y[i:i+s+1], z[i:i+s+1], color=cmap(i/n), alpha=0.9)
      

current_time = datetime.now()
time_stamp = current_time.timestamp()
date_time = datetime.fromtimestamp(time_stamp)

fig.suptitle(str(f"{date_time} mood: {mood_name}"), fontsize=14, fontweight='bold',color='white')
# Remove all the axis clutter, leaving just the curve.
ax.set_axis_off()

plt.savefig(funcs.graphics_extension(file_name+"_"+mood_name), dpi=DPI)

print(funcs.fileserver())