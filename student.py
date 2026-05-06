import json
import os

# File to store student records
DATA_FILE = "students.json"

# Load existing records
def load_records():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}

# Save records to file
def save_records(records):
    with open(DATA_FILE, "w") as f:
        json.dump(records, f, indent=4)

# Add a new student
def add_student(records):
    roll_no = input("Enter Roll Number: ")
    if roll_no in records:
        print("Student with this Roll Number already exists!")
        return
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")
    records[roll_no] = {"Name": name, "Age": age, "Course": course}
    print("Student added successfully!")

# View all students
def view_students(records):
    if not records:
        print("No student records found.")
        return
    print("\n--- Student Records ---")
    for roll_no, details in records.items():
        print(f"Roll No: {roll_no}, Name: {details['Name']}, Age: {details['Age']}, Course: {details['Course']}")

# Search student by roll number
def search_student(records):
    roll_no = input("Enter Roll Number to search: ")
    if roll_no in records:
        details = records[roll_no]
        print(f"Found: Roll No: {roll_no}, Name: {details['Name']}, Age: {details['Age']}, Course: {details['Course']}")
    else:
        print("Student not found.")

# Update student details
def update_student(records):
    roll_no = input("Enter Roll Number to update: ")
    if roll_no in records:
        print("Enter new details (leave blank to keep current value):")
        name = input(f"Name ({records[roll_no]['Name']}): ") or records[roll_no]['Name']
        age = input(f"Age ({records[roll_no]['Age']}): ") or records[roll_no]['Age']
        course = input(f"Course ({records[roll_no]['Course']}): ") or records[roll_no]['Course']
        records[roll_no] = {"Name": name, "Age": age, "Course": course}
        print("Student updated successfully!")
    else:
        print("Student not found.")

# Delete student record
def delete_student(records):
    roll_no = input("Enter Roll Number to delete: ")
    if roll_no in records:
        del records[roll_no]
        print("Student deleted successfully!")
    else:
        print("Student not found.")

# Main menu
def main():
    records = load_records()
    while True:
        print("\n--- Student Record Management ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_student(records)
        elif choice == "2":
            view_students(records)
        elif choice == "3":
            search_student(records)
        elif choice == "4":
            update_student(records)
        elif choice == "5":
            delete_student(records)
        elif choice == "6":
            save_records(records)
            print("Exiting... Records saved.")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()