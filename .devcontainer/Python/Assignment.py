# Write a program that asks the user for his nameand then greet him using “Hello!!!”.
name= input("enter your Name");
print("Hello",name);

#Write a program that prompts the user to enter two integers and display the total on the screen.

a = int(input("Enter the value of a: "))  # Convert input to integer
b = int(input("Enter the value of b: "))  # Convert input to integer
total = a + b
print("The total is:", total);

#Write a program which accept principle, rate and time from user and print the simple interest.
p=int(input("enter principal"));
r=float(input("enter rate"));
t=float(input("enter time"));
si=p*r*t/100;
print("simple interset is",si);

# Write a program that prompts the user to enter number in two variables 
# and swap the contents of the variables using third variable.

x = int(input("Enter the value of x: "))  
y = int(input("Enter the value of y: "))
print("value of variable before swapping is",x,y);


#swapping
c=x;
x=y;
y=c;

print("value of variable after swapping is",x,y);

# Write a program that prompts the user to enter number in two variables and swap the contents of
# the variables without using third variable.

x1 = int(input("Enter the value of x: "))  
y1 = int(input("Enter the value of y: "))
print("value of variable before swapping is",x1,y1);


#swapping
x1=x1-y1;
y1=x1+y1;
x1=y1-x1;

print("value of variable after swapping is",x1,y1);

#Write a program that prompts the user to input values and calculate the area of circle and rectangle. .
