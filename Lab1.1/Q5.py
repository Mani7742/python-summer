
#Write a C++ program to compute the volume of a sphere using the radius provided by the user.

r = eval(input("Enter the Radius:"))
pi = 3.14
v = (3/4)*pi*r**3 #r**3 means the cube of r
if r<0:
    print("Radius cannot be negative")
else:
    print(f"The volume of the sphare with radius {r} is {v:.2f}")    