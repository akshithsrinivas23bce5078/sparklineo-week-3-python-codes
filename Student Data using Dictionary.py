students = {}
while True:
    print("Student Information System")
    print("===========================")
    print("Enter choice:")
    print("1. Add student")
    print("2. View student")
    print("3. Search student")
    print("4. Update student")
    print("5. Delete student")
    print("6. Exit")

    choice = input("Choice: ")

    #Add student
    if choice == '1':
        reg = input("Enter registration number: ")
        if reg in students:
            print("Student with this registration number already exists.")
        else:
            name = input("Enter name: ")
            dept = input("Enter department: ")
            cgpa = float(input("Enter CGPA: "))
            students[reg] = {'name': name, 'dept': dept, 'cgpa': cgpa}
            print("Student added successfully.")
    #View student
    elif choice == '2':
        reg = input("Enter registration number: ")
        if reg in students:
            student = students[reg]
            print(f"Name: {student['name']}")
            print(f"Department: {student['dept']}")
            print(f"CGPA: {student['cgpa']}")
        else:
            print("Student not found.")
    #Search student
    elif choice == '3':
        name = input("Enter name to search: ")
        found = False
        for reg, student in students.items():
            if student['name'].lower() == name.lower():
                print(f"Registration Number: {reg}")
                print(f"Name: {student['name']}")
                print(f"Department: {student['dept']}")
                print(f"CGPA: {student['cgpa']}")
                found = True
        if not found:
            print("Student not found.")
    #Update student
    elif choice == '4':
        reg = input("Enter registration number: ")
        if reg in students:
            name = input("Enter new name: ")
            dept = input("Enter new department: ")
            cgpa = float(input("Enter new CGPA: "))
            students[reg] = {'name': name, 'dept': dept, 'cgpa': cgpa}
            print("Student updated successfully.")
        else:
            print("Student not found.")
    #Delete student
    elif choice == '5':
        reg = input("Enter registration number: ")
        if reg in students:
            del students[reg]
            print("Student deleted successfully.")
        else:
            print("Student not found.")
    #Exit
    elif choice == '6':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")


