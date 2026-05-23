# Simple Calculator
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Addition:",num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)
print("Power:", num1 ** num2)
# Area of Shapes
import math

# Circle
radius = float(input("Enter radius of circle: "))
circle_area = math.pi * radius ** 2
print("Area of circle:", circle_area)

# Rectangle
length = float(input("Enter rectangle length: "))
width = float(input("Enter rectangle width: "))
rectangle_area = length * width
print("Area of rectangle:", rectangle_area)

# Triangle
base = float(input("Enter triangle base: "))
height = float(input("Enter triangle height: "))
triangle_area = 0.5 * base * height
print("Area of triangle:", triangle_area)
# Even or Odd
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")
# Student Grade Percentage
total_marks = float(input("Enter total marks: "))
obtained_marks = float(input("Enter obtained marks: "))

percentage = (obtained_marks / total_marks) * 100

print("Percentage:", percentage, "%")
# BMI Calculator
weight = float(input("Enter weight in kilograms: "))
height = float(input("Enter height in meters: "))

bmi = weight / (height ** 2)

print("Your BMI is:", bmi)

# Power & Modulus
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

print("Power:", num1 ** num2)
print("Modulus:", num1 % num2)