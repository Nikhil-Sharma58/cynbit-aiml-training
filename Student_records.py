students = [
    {
        "id": 1,
        "name": "Rahul",
        "age": 19
    },
    {
        "id": 2,
        "name": "Amit",
        "age": 18
    },
    {
        "id": 3,
        "name": "Aman",
        "age": 20
    }
]

print("Student Records")
for student in students:
    print("\nID:",student["id"])
    print("Name:",student["name"])
    print("Age:",student["age"])