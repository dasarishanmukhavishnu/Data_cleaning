# Schema Driven Data Ingestion

import pandas as pd
schema = {
    "name": {
        "type": str,
        "validator": lambda x: x.replace(" ", "").isalpha(),
        "error": "Name must contain only letters"
    },
    "age": {
        "type": int,
        "validator": lambda x: x.isdigit() and 17 <= int(x) <= 30,
        "error": "Age must be between 1 and 120"
    },
    "college": {
        "type": str,
        "validator": lambda x: x.replace(" ", "").isalpha(),
        "error": "College must contain only letters"
    },
    "cgpa" : {
        "type" : float,
        "validator" : (lambda x: x.replace(".","",1).isdigit() and 1.0 <= float(x) <= 10.0),
        "error" : "Please Enter the CGPA in between(1.0 - 10.0)"
    },
    "placement_stats" : {
        "type" : str,
        "validator" : lambda x: x.lower() in ['placed','not placed'],
        "error" : "Please check what you Entered (placed/not placed)"
    }
}

def get_valid_input(field,rules):
    while True:
        try:
            value = input(f"Enter Student {field} : ").strip()
            if not value:
                raise ValueError("The Data should not be empty")

            if "validator" in rules and not rules["validator"](value):
                raise ValueError(rules["error"])
            return rules["type"](value)
        except ValueError as e:
            print(f"Invalid Error {field} : {e}")

def create_row():
    return {field: get_valid_input(field,rules) for field,rules in schema.items()}

def valid_student_count():
    while True:
        n = input("Enter The number of Students Want to Insert Into Data Base: ")
        if n.isdigit() and int(n) > 0:
            return int(n)
        print("The entered number is Invalid...")

table = []
n = valid_student_count()

for i in range(n):
    print(f"\nStudent {i+1} :")
    table.append(create_row())

for i in table:
    print("\n",i)

data = pd.DataFrame(table)
print("\n",data)