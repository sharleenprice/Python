# problem-set-4-spp2122
problem-set-4-spp2122 created by GitHub Classroom

Problem 1
This script creates "planet" object that takes attributes  for rho, c and n. It also uses these values to calculate other variables such as density, dpdr, and dmdr. These calculations occur in their respective fucntions. Finally, this class of objects returns a numpy array of the two un-integerated equations for pressure and mass. 

Next the function RK4 uses the fourth order runge-kutta method of solving the ODE's dpdr and dmdr. It returns an array of pressure and mass.

Afterwards, we initialize the inital mass and prssure values that will be passed throughout the entire script. Then we create a planet model wil the attricutes that correspond to the element Fe. I then have a while loop to compute the integration for different dependent values. This resulted in varying radius and density. This continued until the radius reached a number comparable to earth's radius. When it got to  about 10 steps before reaching this edge, I reduced the step size value to 1000.

Finally, I gathered the various radius and densities and plotted them.

Problem 2
First I created a new script and imported the script from the first question. This problem was very similar except that I needed to account for a range of pressures. To do so I encompassed the script from problem 1 in a for loop that would get run for different initial central pressure in the initial values. I chose the range 11 to 14.3 with step size 0.2 because this resulted in mass values that ranged for 0.1 to 100 Earth masses. I then plotted the final values for total radius and mass.

Problem 3
In this problem I repeated problem 2 for different planet objects of different elements. This elements were Fe, H2O and MgSiO3. For each of these objects I had to choose a new range of central pressure values that would result in masses from 0.1 to 100 Earth masses. I found this range through trial and error. I plotted the three plots together. Next I added individual points for the 4 terrestrial planets. To do so I looked up the ratio of mass to earth mass and radius to earth radius. I plotted the log of those values for Mars, Venus, Earth and Mars. These are the blue points on my graph. Finally I added the exoplanet points. I chose these specific exoplents because they seem to fit in the range my plot already has. In the same way I plotted these values in red along with its corrsponding mass error bars. 

The graph looks a little different from what I was expecting and I am unsure why it does. In all of these problems I used a base 10 log as oppsed to a log base e and I still got these results. 
