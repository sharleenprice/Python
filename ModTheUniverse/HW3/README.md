# W4260-hw-3-template
Problem 1
I used np.loadtext() to read in the data provided of the source KOI97.01_1. The three variables this data
contained were time,flux, and flux error respectively and so I sent them into appropriate variables.
To plot this data i used matplotlib.pyplot, specifically the errorbar function to make a plot of time vs flux
that contains the appropriate error bars. I labeled the x axis Time and the y axs Flux and called the plot Keplers Plot.
This plot has been attached uploaded as well.

Problem 2a and b
To isolate the eclipse I used the np.where() function which creates an array of the indexes that fall into the ball park conditions. With this i was able to isolate the information corresponding to the eclipses. I was also able to use this data to 
remove the data of the two eclipses and use theremaining data to get an average for the unoscured light. I used this mean to get the ratio of obscured to unobscured. I also converted the eclipse time to z(t). I plotted the z of the eclipse vs the ratio. On top of that I wanted to plot the data from the first problem set. To do so I had to import the script and function
from the first problem set and retrive those z and flux values which we then plotted on top. Lastly I imported the script from problem set 2 to use that flux functions. Again with this function we extracted values of z and flux that came out of the simpsons method of problem set 2. Everything was plotted on on plot which is titled Eclipse 1 and is uploaded. 

Problem 3
This problem involved finding the roots of a function. I started by setting up a function to return the function we need to find roots of. To then find the roots I wrote the function called bisection that follows the bisection method of finding roots. I set initial guesses to be 10 and 6000 to ensure we get the positive root. The following is the output:
>print(bisection(x1,x2,tol))
>3947.1527099609375
