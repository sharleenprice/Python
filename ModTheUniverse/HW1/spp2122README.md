# W4260-hw-1-template
Sharleen Price spp2122
Worked with Giuliana Noto gn2244

Problem 3
This program allows you to print the value of x and ln(x) from ranges 1 to 10 in steps of 0.5. To do this I first imported math and numpy. To create a range with step size of 0.5 you need to use the numpy function arange(). Therefore, I have a for loop to interate through this range at this step size. For every iteration I have a print statement for x and ln(x). To calculate ln(x) we need to use the math function log1p() and so I wrote log1p(x) to calculate ln(x).


Problem 4
This program computes Fe: the ratio of obscured vs unobscured flux of a star's light when a planet is passing infront of it. To do this I defined a function called unobscuredFlux() which takes in the parameters p and abs z which are the size ratio of the planet to the star and the normalized separation of the centers respectively. Abs z is meant to be the normalized separation of the centers before taking the absolute value which I do within the function. This function takes in one value of p and z and calculates Fe for those values. To repeat this many time for a range of z values going from -1.21 to 1.21 by steps of 0.1, a wrote another function called LoopThroughFlux() which takes in parameters p,start,stop,and interval. Within the function I have a for loop that iterates through that range and with each iteration, calls the unobscuredFlux() function with the parameters p and i which is the current value of the iteration of the for loops which is one of the z values. Finally, this function prints the return value of unobscuredFlux() during each iteration.



