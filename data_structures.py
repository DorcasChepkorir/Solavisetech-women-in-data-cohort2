# Favorite Tools List
tools = ["Python", "Excel", "Power BI"]

tools.append("Tableau")
tools.remove("Excel")

print(tools)
# Student Scores
scores = [78, 85, 90, 67, 88]

print("Highest score:", max(scores))
print("Lowest score:", min(scores))
print("Average score:", sum(scores) / len(scores))
# Shopping List Manager
shopping_list = []

shopping_list.append("Bread")
shopping_list.append("Milk")
shopping_list.append("Sugar")

print("Shopping List:", shopping_list)

shopping_list.remove("Milk")

print("Updated List:", shopping_list)
# Country Capitals
country_capitals = (
    ("Kenya", "Nairobi"),
    ("Uganda", "Kampala"),
    ("Tanzania", "Dodoma")
)

for country, capital in country_capitals:
    print(country, ":", capital)
# Unique Visitors
visitors = ["Alice", "Bob", "Alice", "John", "Bob"]

unique_visitors = set(visitors)

print(unique_visitors)
# Common Skills
skills1 = {"Python", "SQL", "Excel"}
skills2 = {"Python", "Power BI", "SQL"}

common = skills1.intersection(skills2)

print("Common skills:", common)
# Student Record
student = {
    "name": "Dorcas",
    "age": 20,
    "course": "Computer Science"
}

print("Student Name:", student["name"])
print("Age:", student["age"])
print("Course:", student["course"])
 # Mini Contact Book
contacts = {
    "Alice": "0712345678",
    "Brian": "0798765432",
    "John": "0700112233"
}

name = input("Enter contact name: ")

if name in contacts:
    print(f"{name}'s number is {contacts[name]}")
else:
    print("Contact not found.")