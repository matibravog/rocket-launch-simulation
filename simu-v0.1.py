import matplotlib.pyplot as plt
import numpy as np

# constants and variables
vehicleMass = 2 #kg
propellantMass = 1 #kg
massFlow = 0.1 #kg/s
exahustVelocity = 1000 #m/s

g = 9.80665 #m/s^2
time = 0 # s
dt = 0.01 # s

# Initial position, velocity, and acceleration of the rocket (m, m/s, m/s^2)
altitude = 0
speed = 0
acceleration = 0
thrust = 0
totalMass = vehicleMass + propellantMass # kg

#targets
targetAltitude = 100 # m

# Lists to store the position, velocity, and acceleration of the rocket over time
times = []
masses = []
positions = []
velocities = []
accelerations = []
thrusts = []

while altitude <= targetAltitude:

    #Calculate values 
    time += dt
    totalMass -=  massFlow * dt
    
    thrust = massFlow * exahustVelocity
    acceleration = (thrust - g) / totalMass
    speed += acceleration * dt
    altitude += speed * dt

    # Store the position, velocity, and acceleration of the rocket at this time step
    times.append(time)
    masses.append(totalMass)
    positions.append(altitude)
    velocities.append(speed)
    accelerations.append(acceleration)
    thrusts.append(thrust)

print('final mass: ', totalMass)
print('time: ', time)
print('thrust: ', thrust)
print('acceleration: ', acceleration)
print('speed: ', speed)
print('altitude: ', altitude)

# Create a new figure with 4 subplots
fig, ax = plt.subplots(2, 3)

# Plot the position of the rocket in the top left subplot
ax[0, 2].plot(masses, label='mass (ks)')
ax[0, 2].set_ylabel('mass (kg)')
ax[0, 2].legend()

# Plot the position of the rocket in the top left subplot
ax[1, 2].plot(times, label='time (s)')
ax[1, 2].set_ylabel('time (s)')
ax[1, 2].legend()


# Plot the position of the rocket in the top left subplot
ax[0, 0].plot(positions, label='Position (m)')
ax[0, 0].set_ylabel('Position (m)')
ax[0, 0].legend()

# Plot the velocity of the rocket in the top right subplot
ax[0, 1].plot(velocities, label='Velocity (m/s)')
ax[0, 1].set_ylabel('Velocity (m/s)')
ax[0, 1].legend()

# Plot the acceleration of the rocket in the bottom left subplot
ax[1, 0].plot(accelerations, label='Acceleration (m/s^2)')
ax[1, 0].set_ylabel('Acceleration (m/s^2)')
ax[1, 0].legend()

# Plot the thrust of the rocket in the bottom right subplot
ax[1, 1].plot(thrusts, label='Thrust (kg m/s^2)')
ax[1, 1].set_ylabel('Thrust (kg m/s^2)')
ax[1, 1].legend()

# Show the figure
plt.show()
