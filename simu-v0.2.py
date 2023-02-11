import matplotlib.pyplot as plt
import numpy as np
import time as tm

# vehicle constants and variables
vehicleMass = 1.2 #Kg
propellantMass = 0.8 # Kg
# dragCoefficient = 0.01 # adimensional
# crossSectionalArea = 0.00785 #M^2

# engine constants
massFlow = 0.2 # Kg/s
exahustVelocity = 172 #m/s half of speed of sound aprox

#physical constants
gravity = 9.80665 #kgm/s^2
# atmDensitySeaLevel = 1.2250 # kg/m^3
# atmPressureSeaLevel = 101325 # Pa

# time tracker
time = 0.0 #s
dt = 0.1 #s

#initial values
altitude = 0
speed = 0
acceleration = 0
thrust = 0

# data storage arrays 
altitudes = []
speeds = []
accelerations = []
thrusts = []
times = []
masses = []

# states tracker
startupMode = False 
readyForLaunch = False 
launch = False
ascentPhase = False
apogee = False
descentPhase = False
landing = False 

#targets
# targetAltitude = 100 #m

def flightComputerOn(startupMode): 
    startupMode = True
    return startupMode

def appendValues(time, currentMass, altitude, speed, acceleration, thrust): 
    # Store the position, velocity, and acceleration of the rocket at this time step
    times.append(time)
    masses.append(currentMass)
    altitudes.append(altitude)
    speeds.append(speed)
    accelerations.append(acceleration)
    thrusts.append(thrust)

def graphics(): 
    # # Create a new figure with 4 subplots
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
    ax[0, 0].plot(altitudes, label='Position (m)')
    ax[0, 0].set_ylabel('Position (m)')
    ax[0, 0].legend()

    # Plot the velocity of the rocket in the top right subplot
    ax[0, 1].plot(speeds, label='Velocity (m/s)')
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

startupMode = flightComputerOn(startupMode)

if startupMode == True:
    def calibrateSensors():
        print('SENSORS CHECK')

    def checkTvc():
        print('TVC CHECK')

    calibrateSensors()
    checkTvc()

    readyForLaunch = True

if readyForLaunch == True:
    def initCountdown():
        countdown = 11
        i = 1
        
        print('INIT COUNTDOWN')

        while countdown > 0:
            countdown -= i
            print(countdown) 
            tm.sleep(0.01)

    initCountdown()
    launch = True

if launch == True:
    print('IGNITION')
    print('LIFTOFF')

    while propellantMass >= 0:
       
        time += dt
        
        propellantMass -= massFlow * dt
        currentMass = vehicleMass + propellantMass
        vehicleWeight = currentMass * gravity

        thrust = massFlow * exahustVelocity
        acceleration = (thrust - vehicleWeight) / currentMass
        speed += acceleration * dt
        altitude += speed * dt

        if propellantMass <= 0:
            print('BURNTIME COMPLETE: ', time , ' seconds at ', altitude, ' meters' )
            ascentPhase = True

        appendValues(time, currentMass, altitude, speed, acceleration, thrust)

if ascentPhase == True:
    while speed >=0:

        time = times[-1]
        currentMass = masses[-1]
        acceleration = accelerations[-1]
        speed = speeds[-1]
        altitude = altitudes[-1]
        thrust = 0

        time += dt 
        currentWeight = currentMass * gravity
        acceleration = - gravity
        speed += acceleration * dt
        altitude += speed * dt

        if speed <= 0:
            print('APOGEE: ', altitude, 'meters at ',time, ' seconds')
            apogee = True

        appendValues(time, currentMass, altitude, speed, acceleration, thrust)

if apogee == True:
    print('PARACHUTE DEPLOY ')
    descentPhase = True

if descentPhase == True:
    
    while altitude >=0:

        time = times[-1]
        currentMass = masses[-1]
        thrust = 0
        acceleration = accelerations[-1]
        speed = speeds[-1]
        altitude = altitudes[-1]

        time += dt 
        currentWeight = currentMass * gravity
        acceleration = - gravity
        speed += acceleration * dt
        altitude += speed * dt

        if altitude <= 0:
            print('LANDING: ', time)
            landing = True

        appendValues(time, currentMass, altitude, speed, acceleration, thrust)

if landing == True:
    print('fast data logging')
    graphics()  

