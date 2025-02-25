#Question : WAP to do arithmetical operations addition, substraction, multiple and division.

#Addition
print("Addition")
num1 = float(input("Enter first number : "))
num2 = float(input("Enter second number : "))
sum = num1 + num2
print("Addition of two numbers is : ", sum)

#Substraction
print("Substraction")   
num3 = float(input("Enter first number : "))
num4 = float(input("Enter second number : "))
sub = num3 - num4
print("Substraction of two numbers is : ", sub)

#Multiplication
print("Multiplication")
num5 = float(input("Enter first number : "))
num6 = float(input("Enter second number : "))
mul = num5 * num6
print("Multiplication of two numbers is : ", mul)


#Division
print("Division")
num7 = float(input("Enter first number : "))
num8 = float(input("Enter second number : "))
if num8 != 0:
    div = num7 / num8
    print("Division of two numbers is : ", div)
else:
    print("Error! Division by zero is not allowed")
    
