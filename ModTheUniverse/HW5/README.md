# problem-set-5-spp2122
problem-set-5-spp2122 created by GitHub Classroom

Problem 1
I have organized this problem by in order of images.  The first half is for the spiral image and the second half is for the elliptical. 
Within each of these sections I have organized them by weighted mean and brightest pixel. Therefore, to see the weighted mean for the
elliptical, you need to uncomment the code that gets the data for the elliptical and uncomment the code that is under the weighted mean section.
The same process goes for any of the other combination. 
As you can see by my spiral brightest pixel and weighted mean images, the weighed mean shows the center of the image while the brightest pixel method
shows the brightest pixel which is not necessarily at the center. Therefore, the weighted mean method is a better method for locating the center of an image.

Problem 2
For problem 2 and 3 you must enter either "spiral.fits" or "elliptical.fits" to view the data for each image. In this script, 
I look at each pixel and determine its length from the center using the standard length formula. If the length is between 0 and 2 from the center
I took the brightness of those pixels and added them together within the variable total. I also used the variable count to keep track
of how many pixels satisfied that condition. I then multiply the radius(length) by 5 using the variable "inc" for increment and repeat this process by
having "inc" increase in a for loop. This process repeats until inc reaches the value of 150 which is the max radius this image can have.
I now have the total and count for various radii. I can now plot the average value of brightness versus radius. I compared this plot
to the standard exponential fit provided in the problem. S_0 is the center brightness and I chose r_0 to be 23 since it provided a fit that
more or less worked with my data. I have uploaded the plots for each image's distribution. 

Problem 3
I chose a small portion of the image to be 30 by 30 pixels starting at point 0,0 which is at the top left of the image. For both images
that spot is mostly black. For this square I stored the brightness in the list called "flux". I then used plt.hist() to plot a histogram of those brightness distributions.
I also wrote the code for a poisson and gaussian histogram. You must uncomment the one you want to see. I found that the elliptical
galaxy resembles a guassian distribution more closely than a poisson. Whereas the spiral galaxy seems to resemble a poisson distribution more
closely than a gaussian. Therefore, I have uploaded those two plots.
