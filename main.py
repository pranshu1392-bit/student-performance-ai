from model import predict_marks
from utils import classify_risk, display_student

students = []
while True:
    print("\n===== MENU=====")
    print("1. Add Student")
    print("2. Show All Students")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        name = input("Enter name: ")
        study_hours = float(input("Study hours: "))
        attendance = float(input("Attendance (%): "))
        assignments = float(input("Assignments completed: "))
        marks = predict_marks(study_hours, attendance, assignments)
        risk = classify_risk(marks)
        students.append((name, marks, risk))
        display_student(name, marks, risk)
    elif choice == "2":
        print("\n--- All Students ---")
        for s in students:
            print(s)
    elif choice == "3":
        print("Exiting program...")
        break
    else:
        print("Invalid choice!")