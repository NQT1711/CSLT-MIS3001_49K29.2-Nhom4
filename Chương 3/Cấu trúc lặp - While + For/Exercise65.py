from math import sqrt

perimeter=0
x1=float(input("Enter the x coordinate: "))
y1=float(input("Enter the y coordinate: "))
prev_x=x1
prev_y=y1

line=input("Enter the x coordinate (blank to quit): ")
while line!="":
    x2=float(line)
    y2=float(input("Enter the y coordinate: "))
    distance=sqrt((prev_x-x2)**2+(prev_y-y2)**2)
    perimeter=perimeter+distance
    
    prev_x=x2
    prev_y=y2
    
    line=input("Enter the x coordinate (blank to quit): ")
    
distance=sqrt(((x1-x2))**2+(y1-y2)**2)
perimeter=perimeter+distance
print("The perimeter of the polygon is",perimeter)
