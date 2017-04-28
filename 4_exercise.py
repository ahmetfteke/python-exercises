# Write a Python program which accepts the radius of a circle from the user and compute the area. Go to the editor
# Sample Output : 
# r = 1.1
# Area = 3.8013271108436504

from math import pi
r = float(input ("Input the radius: "))
print ("The area of the circle: {} is: {}".format(str(r), str(pi * r**2)))