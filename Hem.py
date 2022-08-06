# coordinate transformation(GCS-CCS)
from cmath import cos, sin, sqrt
import math

a=float(input("enter the semi major axis:"))
b=float(input("enter the value of semi-minor axis:"))
phi=math.radians(27.69196)
lamda=math.radians(85.52229)                                
h=int(input("enter the ellipsoidal height:"))
# first eccentricity
e=sqrt(a*a-b*b)/a;
N= a/(1-e*e*((sin(phi)) ** 2)) **(1/2);
x=(N+h)*cos(phi)*cos(lamda);
print("the x-coordinate is ",x)
y=(N+h)*cos(phi)*sin(lamda);
print("the value of y is:",y)
z=((1-e*e)*N+h)*sin(phi);
print("the value of z is:",z)
from cmath import acos, sqrt


#Everest 1830
a=float(input ("enter the semimajor axis:"))
b=float (input("enter semiminor axis:"))
#Flatenning
f=((a-b)/a)
print("the flatenning is:",f)
#second flatenning
f1=((a-b)/b)
print("the second flatenning is:",f1)
#first eccentricity 
e1=(sqrt(a*a-b*b)/a)
print("The first eccentricity is:",e1)
#second eccentricity
e2=(sqrt(a*a-b*b)/b)
print("The second eccentricity is:",e2)
#linear eccentricity
E=(sqrt(a*a-b*b))
print("the linear eccentricity is:",E)
# angular eccentricity
alpha=acos(b/a*e1)
print("the angular eccentricity is:",alpha)

# coordinate transformation(GCS-CCS)
from cmath import cos, sin, sqrt
import math

a=float(input("enter the semi major axis:"))
b=float(input("enter the value of semi-minor axis:"))
phi=math.radians(27.69196)
lamda=math.radians(85.52229)                                
h=int(input("enter the ellipsoidal height:"))
# first eccentricity
e=sqrt(a*a-b*b)/a;
N= a/(1-e*e*((sin(phi)) ** 2)) **(1/2);
x=(N+h)*cos(phi)*cos(lamda);
print("the x-coordinate is ",x)
y=(N+h)*cos(phi)*sin(lamda);
print("the value of y is:",y)
z=((1-e*e)*N+h)*sin(phi);
print("the value of z is:",z)
from cmath import acos, sqrt
from tkinter import ARC

# WGS 1984
a=int(input ("enter the semimajor axis"))
b=float (input("enter semiminor axis "))
f=((a-b)/a)
print("the flatenning is:",f)
# second flatenning
f1=((a-b)/b)
print("the second flatenning is:",f1)
#first eccentricity 
e1=(sqrt(a*a-b*b)/a)
print("The first eccentricity is:",e1)
#second eccentricity
e2=(sqrt(a*a-b*b)/b)
print("The second eccentricity is:",e2)
#linear eccentricity
E=(sqrt(a*a-b*b))
print("the linear eccentricity is:",E)
# angular eccentricity
alpha=acos(b/a*e1)
print("the angular eccentricity is:",alpha)