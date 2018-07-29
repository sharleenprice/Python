# problem-set-2-spp2122
problem-set-2-spp2122 created by GitHub Classroom

Problem 1

To be able to calculate the integrals for the F(p,z) function, I broke it down into several components. 
I first made a function called delta which takes in p,r and z as parameters and wrote the piecewise components inside of it using
If/elif/else statements. I also made a function for I(r) that just returned 1. Next I made functions for the numerator and denominator so that I can pass them separatly though the integrator.
For funtions top and bottom I just wrote the math out and called the delta function and I(r) where needed. 
Finally I wrote the integrator that computes the rectangle rule sumation for the different step sizes. 
Lastly I wrote the function F(p,z) that but all the components together and printed the results from passing the top
and bottom through the integrator and dividing them. In this function I also calculated the error by comparing it to the 
expected value. The fractional error decreased as the step sized increased.


Problem 2

In the same way as problem 1 I broke down the function into several components. The only difference is that instead of the integrator from problem 1
I have a function called simpson that also takes in f,a,b, and N as parameter. In this function I coded the formula for simpson's integration which gets applied in F(p,z)
instead of the integrator function. As a result I got a number that approached 1 as the step size increased. My error also increased as
step size increased. This is not what I expected and it should not do this. I am unsure what is the problem.

Problem 3

Lastly I coded the monte carlo integration method where I used randomly generated numbers to solve for F(p,z).
The error decreases significantly as the step size increased. 
