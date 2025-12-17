# Student Management System
# Author: Dhruv Makwana

students = []

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    marks = input("Enter Marks: ")

    student = {
        "roll": roll,
        "name": name,
        "marks": marks
    }
    students.append(student)
    print("Student added successfully!\n")

def view_students():
    if not students:
        print("No student records found.\n")
        return

    print("\n--- Student List ---")
    for s in students:
        print(f"Roll: {s['roll']}, Name: {s['name']}, Marks: {s['marks']}")
    print()

def update_student():
    roll = input("Enter Roll Number to Update: ")
    for s in students:
        if s["roll"] == roll:
            s["name"] = input("Enter New Name: ")
            s["marks"] = input("Enter New Marks: ")
            print("Student updated successfully!\n")
            return
    print("Student not found!\n")

def delete_student():
    roll = input("Enter Roll Number to Delete: ")
    for s in students:
        if s["roll"] == roll:
            students.remove(s)
            print("Student deleted successfully!\n")
            return
    print("Student not found!\n")

def main_menu():
    while True:
        print("===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("Thank you for using the system!")
            break
        else:
            print("Invalid choice! Try again.\n")

main_menu()
