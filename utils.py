def classify_risk(marks):
    if marks >= 75:
        return "Low Risk"
    elif marks >= 50:
        return "Medium Risk"
    else:
        return "High Risk"

def display_student(name, marks, risk):
    print("\n--- Student Result ---")
    print("Name:", name)
    print("Predicted Marks:", round(marks, 2))
    print("Risk Level:", risk)