# Personal Bio Generator
name = "Dorcas Chepkorir"
age = 20
height = 5.0
favorite_tech_field = "AI and Machine Learning"
is_student = True

print(f"My name is {name}. I am {age} years old, {height} feet tall.")
print(f"My favorite tech field is {favorite_tech_field}.")
print(f"Student Status: {is_student}")

# Type Checker
name = "DORCAS CHEPKORIR"
age = 20
height = 5.0
is_student = True

print(type(name))
print(type(age))
print(type(height))
print(type(is_student))

# Data Conversion
# Integer to string
num = 100
num_str = str(num)

# Float to integer
price = 45.99
price_int = int(price)

# String number to integer
number = "500"
number_int = int(number)

print(num_str)
print(price_int)
print(number_int)

# User Information
name = input("Enter your name: ")
age = input("Enter your age: ")
country = input("Enter your country: ")

print(f"Hello {name}, you are {age} years old and you come from {country}.")

# Temperature Converter
celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C is equal to {fahrenheit}°F")
