#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 05:07:42 2018

@author: sharleenprice
"""

import numpy as np
import math
# define some physical constants

#G            = 6.67e-11  # Gravitational constant [m^3/kg/s^2]
#mass_solar   = 1.99e30   # solar mass [kg]
#mass_earth   = 5.97e24   # mass of earth [kg]
#AU           = 1.496e11  # Astronomical unit [m]

# define dimensionless units (this is equivalent to above but in units
#  such that one year is 2*pi time units, and 1 AU is one length unit).

G = 1.0
mass_solar = 1.0
mass_earth = 3.0e-6
mass_jupiter = 0.0009543
AU = 1.0

def ComputeAccel(x, m):
    """ returns gravitational acceleration as a numpy array given positions (numyp array of
        size [N,ndim] where N is the number of particles and ndim is the number of dimensions (2 or 3) 
        and masses (as numpy array of size [N]) """
    a = np.zeros_like(x)
    nbodies = x.shape[0]
    for i in range(nbodies):
        for j in range(nbodies):
            r = x[j]-x[i]
            if i != j:
                a[i] = a[i] + r*G*m[j]/pow(np.vdot(r, r), 1.5)
    return a

# Set initial conditions

nbodies = 3
x = np.zeros([nbodies,2])
v = np.zeros([nbodies,2])
m = np.zeros([nbodies])

# set up sun
x[0] = np.array([0.0, 0.0]) 
v[0] = np.array([0.0, 0.0])
m[0] = mass_solar
 
# set up earth
circular_orbit = math.sqrt(G*mass_solar/AU)
x[1] = np.array([AU, 0.0]) #distance between earth and sun is 1 AU
v[1] = np.array([0.0, circular_orbit]) #velocity is always tangetial to distance
m[1] = mass_earth
 
#set up jupiter
semi = 4*AU
e = 0.6 
v_elliptical = math.sqrt((G*mass_solar*(1+e))/(semi*(1-e)))
x[2] = np.array([(1-e)*semi, 0.0])
v[2] = np.array([0.0, v_elliptical])
m[2] = mass_jupiter

 
def leapfrog(m, v, x, delta_t):
    x = x + delta_t*v
    a = ComputeAccel(x, m)
    v = v + delta_t*a
    return (x, v)


"""Problem 2"""
time_orbit = (2*math.pi*AU)/v_elliptical # time for one prbit
hundred_orbits=100*time_orbit #time for 100 orbits
dt=time_orbit/200 #time for one orbit in 200 chunks
total_steps = int(hundred_orbits/dt) #how many steps to get to 100th orbit

a=ComputeAccel(x,m)
v=v+0.5*dt*a
for i in range(total_steps):
    (x,v) = leapfrog(m, v, x, dt)

print("Change in Radius", (math.sqrt(np.vdot(x, x))-AU)) 

E_k=[]
E_p=[]
total=[]

for i in range(total_steps):
    KE=0
    PE=0
    (x,v)=leapfrog(m, v, x, dt)
    for j in range(nbodies):
        KE+=0.5*m[j]*np.vdot(v[j],v[j])
        for k in range(nbodies):
            if j != k:
                distance = x[k]-x[j]
                PE -=(G*m[j]*m[k]/math.sqrt(np.vdot(distance,distance)))
    
    total.append(KE+PE)
    
change_energy = (total[-1]-total[0])
print("Change in Energy", change_energy) 

