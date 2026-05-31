
# Age Eligibility Checker

age = int(input("Enter your age: "))

if age < 12:
    print("You are a child.")
elif age < 20:
    print("You are a teenager.")
else:
    print("You are an adult.")

# Password Validator

password = input("Enter password: ")

if len(password) >= 8:
    print("Strong password")
else:
    print("Weak password")

# Grade Classification
score = int(input("Enter your score: "))

if score >= 80:
    print("Grade A")
elif score >= 70:
    print("Grade B")
elif score >= 60:
    print("Grade C")
elif score >= 50:
    print("Grade D")
else:
    print("Grade F")

# Multiplication Table

number = int(input("Enter a number: "))

for i in range(1, 13):
 print(f"{number} x {i} = {number * i}")

 # Number Guessing Game

secret_number = 7
guess = 0

while guess != secret_number:
    guess = int(input("Guess the number: "))

    if guess == secret_number:
        print("Correct! You guessed the number.")
    else:
        print("Wrong guess. Try again.")
# Countdown Timer
for i in range(10, 0, -1):
    print(i)

print("Countdown complete!")

 # ATM Withdrawal Simulation

balance = 10000

withdrawal = float(input("Enter amount to withdraw: "))

if withdrawal <= balance:
    balance -= withdrawal
    print("Withdrawal successful.")
    print("Remaining balance:", balance)
else:
    print("Insufficient balance.")
# Login System
correct_username = "admin"
correct_password = "12345"

username = input("Enter username: ")
password = input("Enter password: ")

if username == correct_username and password == correct_password:
    print("Login successful")
else:   
    print("Invalid username or password")
# Age Eligibility Checker

age = int(input("Enter your age: "))

if age < 12:
    print("You are a child.")
elif age < 20:
    print("You are a teenager.")
else:
    print("You are an adult.")

# Password Validator

password = input("Enter password: ")

if len(password) >= 8:
    print("Strong password")
else:
    print("Weak password")

# Grade Classification
score = int(input("Enter your score: "))

if score >= 80:
    print("Grade A")
elif score >= 70:
    print("Grade B")
elif score >= 60:
    print("Grade C")
elif score >= 50:
    print("Grade D")
else:
    print("Grade F")

# Multiplication Table

number = int(input("Enter a number: "))

for i in range(1, 13):
 print(f"{number} x {i} = {number * i}")

 # Number Guessing Game

secret_number = 7
guess = 0

while guess != secret_number:
    guess = int(input("Guess the number: "))

    if guess == secret_number:
        print("Correct! You guessed the number.")
    else:
        print("Wrong guess. Try again.")
# Countdown Timer
for i in range(10, 0, -1):
    print(i)

print("Countdown complete!")

 # ATM Withdrawal Simulation

balance = 10000

withdrawal = float(input("Enter amount to withdraw: "))

if withdrawal <= balance:
    balance -= withdrawal
    print("Withdrawal successful.")
    print("Remaining balance:", balance)
else:
    print("Insufficient balance.")
# Login System
correct_username = "admin"
correct_password = "12345"

username = input("Enter username: ")
password = input("Enter password: ")

if username == correct_username and password == correct_password:
    print("Login successful")
else:
    print("Invalid username or password")