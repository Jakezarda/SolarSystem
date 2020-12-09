import numpy as np
import matplotlib.pyplot as plt

f = open('simulation.dat')
lines = f.readlines()

## in this data sheet. column 0 = time. column 1 = mercury pos[0] column 2 mercury pos[1] column 3 mercury pos[2]
## the next 3 are the velocities of mercury in xyz. then it moves on to Venus, and onward for the rest of the solar sytem.
t = []

mercury_x = []
mercury_y = []

venus_x = []
venus_y = []

earth_x = []
earth_y = []

mars_x = []
mars_y = []

jupiter_x = []
jupiter_y = []

saturn_x = []
saturn_y = []

uranus_x = []
uranus_y = []

neptune_x = []
neptune_y = []

for x in lines:
    t.append(float(x.split(' ')[0]))
    
    mercury_x.append(float(x.split(' ')[1]))
    mercury_y.append(float(x.split(' ')[2]))
    
    venus_x.append(float(x.split(' ')[7]))
    venus_y.append(float(x.split(' ')[8]))
    
    earth_x.append(float(x.split(' ')[13]))
    earth_y.append(float(x.split(' ')[14]))
    
    mars_x.append(float(x.split(' ')[19]))
    mars_y.append(float(x.split(' ')[20]))
    
    jupiter_x.append(float(x.split(' ')[25]))
    jupiter_y.append(float(x.split(' ')[26]))
    
    saturn_x.append(float(x.split(' ')[31]))
    saturn_y.append(float(x.split(' ')[32]))
    
    uranus_x.append(float(x.split(' ')[37]))
    uranus_y.append(float(x.split(' ')[38]))
    
    neptune_x.append(float(x.split(' ')[43]))
    neptune_y.append(float(x.split(' ')[44]))
f.close()


##sun = plt.plot(0, 0, 'ro')                            plotting a point for the sun doesn't really work when you zoom far enough out to include the gas planets
#mercuryOrbit = plt.plot(mercury_x, mercury_y, '-')
#venusOrbit = plt.plot(venus_x, venus_y, '-')
#earthOrbit = plt.plot(earth_x, earth_y, '-')
#marsOrbit = plt.plot(mars_x, mars_y, '-')
#jupiterOrbit = plt.plot(jupiter_x, jupiter_y, '-')
#saturnOrbit = plt.plot(saturn_x, saturn_y, '-')
#uranusOrbit = plt.plot(uranus_x, uranus_y, '-')
#neptuneOrbit = plt.plot(neptune_x, neptune_y, '-')
#plt.savefig('SolarPlot.pdf')
#plt.close()

mercuryOrbit_1x = mercury_x[0:750]                              #750 index is roughly 1 orbit, calculations say it should be at 705 but that fell short 
mercuryOrbit_1y = mercury_y[0:750]                              #so we may be a little bit over exactly 1 orbit.

mercuryOrbit_100x = mercury_x[292000:292750]
mercuryOrbit_100y = mercury_y[292000:292750]

mercuryOrbit_finalx = mercury_x[583251:584001]
mercuryOrbit_finaly = mercury_y[583251:584001]

#mercuryOrbit_1 = plt.plot(mercuryOrbit_1x, mercuryOrbit_1y, '-')
#mercuryOrbit_100 = plt.plot(mercuryOrbit_100x, mercuryOrbit_100y, 'r-')
#mercuryOrbit_final = plt.plot(mercuryOrbit_finalx, mercuryOrbit_finaly, '-')
#plt.savefig('MercuryOrbit_1_100_final.pdf')


avg_x1 = (mercury_x[518]+mercury_x[519])/2
avg_y1 = (mercury_y[518]+mercury_y[519])/2

theta_1 = np.arctan(avg_y1/avg_x1)
#print(avg_x1)
#print(avg_y1)
print("Theta 1 is", theta_1)

avg_x2 = (mercury_x[292352]+mercury_x[292353])/2
avg_y2 = (mercury_y[292352]+mercury_y[292353])/2
theta_2 = np.arctan(avg_y2/avg_x2)
print("Theta 2 is", theta_2)

avg_x3 = (mercury_x[583465]+mercury_x[583466])/2
avg_y3 = (mercury_y[583465]+mercury_y[583466])/2

theta_3 = np.arctan(avg_y3/avg_x3)

print("theta 3 is", theta_3)

shift_1 = np.abs(theta_2-theta_1)
shift_2 = np.abs(theta_3-theta_1)

print("The angular change in perihelion after 100 years is", shift_1)
print("The angular change in perihelion after 200 years is", shift_2)       ##I think the timestep is too big, the angular change isn't really what i expect.
                                                                            ##I'm moving on to the neptune/uranus part

f2 = open('simulationTest.dat')
lines2 = f2.readlines()

uranus_x2 = []
uranus_y2 = []

for x in lines2:
    uranus_x2.append(float(x.split(' ')[37]))
    uranus_y2.append(float(x.split(' ')[38]))
f.close()

uranus_N_angle = np.zeros(584001)
uranus_angle = np.zeros(584001)

for i in range(len(uranus_x)):
    if uranus_x[i] < 0 and uranus_y[i] > 0:
        uranus_N_angle[i] = np.arctan(uranus_y[i]/uranus_x[i])+np.pi
    elif uranus_x[i] < 0 and uranus_y[i] < 0:
        uranus_N_angle[i] = np.arctan(uranus_y[i]/uranus_x[i])+np.pi
    elif uranus_x[i] > 0 and uranus_y[i] < 0:
        uranus_N_angle[i] = np.arctan(uranus_y[i]/uranus_x[i])+2*np.pi
    else:
        uranus_N_angle[i] = np.arctan(uranus_y[i]/uranus_x[i])
        
for i in range(len(uranus_x2)):
    if uranus_x2[i] < 0 and uranus_y2[i] > 0:
        uranus_angle[i] = np.arctan(uranus_y2[i]/uranus_x2[i])+np.pi
    elif uranus_x2[i] < 0 and uranus_y2[i] < 0:
        uranus_angle[i] = np.arctan(uranus_y2[i]/uranus_x2[i])+np.pi
    elif uranus_x2[i] > 0 and uranus_y2[i] < 0:
        uranus_angle[i] = np.arctan(uranus_y2[i]/uranus_x2[i])+2*np.pi
    else:
        uranus_angle[i] = np.arctan(uranus_y2[i]/uranus_x2[i])
    
#for i in range(len(uranus_x2)):
#    uranus_angle[i] = np.arctan(uranus_y2[i]/uranus_x2[i])

deltaTheta = np.zeros(584001)
print(uranus_y2[1])
print(uranus_x2[1])
print(np.arctan(uranus_y2[1]/uranus_x2[1]))

for i in range(len(deltaTheta)):
    deltaTheta[i] = (uranus_N_angle[i] - uranus_angle[i])
    
print(uranus_x[2])
print(uranus_x2[2])
print(uranus_N_angle[1]-uranus_angle[1])

uranusAngle = plt.plot(t, uranus_N_angle, '-')
plt.savefig('angleTest.pdf')
plt.close()

uranusAngle2 = plt.plot(t,uranus_angle, '-')
plt.savefig('angleTest2.pdf')
plt.close()

angleDif = plt.plot(t,deltaTheta, '-')
plt.savefig('deltaTheta.pdf')

