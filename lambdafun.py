a=int(input("enter sides of square"))
lambda_square=lambda  a:a*a
print("area of square is",lambda_square(a))
b=int(input("enter breadth" ))
h=int(input("enter height" ))            
lambda_triangle=lambda  b,h:1/2*b*h
print("area of triangle is",lambda_triangle(b,h))
l=int(input("enter length"))
b=int(input("enter breadth" ))            
lambda_rectangle=lambda  l,b:l*b
print("area of rectangle is",lambda_rectangle(l,b))
