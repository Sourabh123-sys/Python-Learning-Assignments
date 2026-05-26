# Student Grade Calculator

# Function to calculate grade
def calculate_grade(marks):
    if marks >= 90:
        return  "A", "Excellent work! "
    elif marks >= 80:
        return "B", "Very Good! Keep it up! "
    elif marks >= 70:
        return "C", "Good Job! "
    elif marks >= 60:
        return "D", "Keep it up! "
    else:
        return "F", "Don't give up! Try again! "
    

# Taking student name
name = input(" Enter Student name: ")

# Input validationusing while loop
while True:
    marks = int(input("Enter marks (0-100): "))

    if  0 <= marks <= 100:
        break
    else:
        print("Invalid ")

#Function call
grade, message = calculate_grade(marks)

# Final Output
print("\nRESULT FOR", name.upper() + ":")
print(f"Marks: {marks}/100")
print(f"Grade: {grade}")
print(f"Messsage: {message}")
