student={
"ayush":{"roll":157, "marks":500, "collage-name":"iibm"},
"karan":{"roll":158, "marks":500,"collage-name":"iibm"},
"bobby":{"roll":158, "marks":500, "collage-name":"iibm"},

}

name=input('enter your name to get marks:')

if name in student:
    print("roll" ,student[name]["roll"])
    print("marks",student[name]["marks"])
    print("collage-name",student[name]["collage-name"])
else:
    print("not found your result...")


#aiii
# Student Result Management System

students = {}

while True:
    print("\n===== MENU =====")
    print("1. Add Student")
    print("2. View Student Result")
    print("3. View All Students")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    # Add Student
    if choice == "1":
        name = input("Enter student name: ")
        roll = int(input("Enter roll number: "))
        marks = int(input("Enter marks: "))

        students[name] = {
            "roll": roll,
            "marks": marks
        }

        print("✅ Student added successfully!")

    # View Result
    elif choice == "2":
        name = input("Enter name to search: ")

        if name in students:
            print("\n--- Student Result ---")
            print("Name :", name)
            print("Roll :", students[name]["roll"])
            print("Marks:", students[name]["marks"])

            if students[name]["marks"] >= 33:
                print("Status: PASS ✅")
            else:
                print("Status: FAIL ❌")
        else:
            print("❌ Student not found")

    # View All Students
    elif choice == "3":
        if not students:
            print("No student data available")
        else:
            print("\n--- All Students ---")
            for name, data in students.items():
                print(name, "-> Roll:", data["roll"], "Marks:", data["marks"])

    # Exit
    elif choice == "4":
        print("Thank you! Program closed.")
        break

    else:
        print("❌ Invalid choice, try again")
