# A dictionary storing details of a single student
student_detail = {
    "name": "Rachit",
    "roll": 123
}

# A list of dictionaries, each containing details of a student
students = [
    {
        "name": "Rachit",
        "roll_number": 345
    },
    {
        "name": "Suprim",
        "roll_number": 333
    }
]

# Print the name from the single student_detail dictionary
print(student_detail["name"])  # Output: Rachit

# Print the name of the second student in the students list
print(students[1]["name"])  # Output: Suprim
