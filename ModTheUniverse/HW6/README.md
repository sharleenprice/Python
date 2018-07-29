# W4260-hw-6-template

Problem 1

I started off by setting up the earth in the same was as we did for the sun except it has an "x" distance of 1 AU and a tangetial velocity

Next I wrote a leapfrog method that calculates the new x and v values after a step dt and returns it.

Then I set upu the inital centripetal velocity, time for one orbit, time for 5 orbits, a small
step for itegrating: dt, and the total small steps for all the orbits
Then I computed acceleration and computer the first velocity value for a half step. This gives us a radius
and so we can find the change in radius since the initial radius is AU, so we subtract the two and I print that result.

To find the change in energy I used for loops to do the summation for KE and PE. I put the summation under another for loop to  
get all the values of KE and PE that we need. This for loop will run the summation process multiple times for all the steps, re- initalizing x and v each time. I then appended the sum of PE and ke in a list and found the change in energy by subtracting the last element by the first in the list total. 

In problem 2 I do exactly the same thing except there are 3 bodies. Again I set up the earth and jupiter. I definined relevant  constants. And change the amount of orbits to 100. The results for jupiter is also printed. 
