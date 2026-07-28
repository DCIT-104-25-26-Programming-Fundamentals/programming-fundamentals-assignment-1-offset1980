# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 8
# Topic: Lists of Dictionaries, Loops, and Functions
# =============================================================================
#
# TASK: Student Record Management System
#
# Build a console-based program that stores and manages student information.
# Each student record must contain:
#
#   - Name   : the student's full name (text)
#   - ID     : a unique student ID number (e.g. 20240001)
#   - Scores : a list of scores from multiple assessments (e.g. [75, 88, 90])
#
# -----------------------------------------------------------------------------
# FEATURES YOUR PROGRAM MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Add a Student
#      - Ask the user to enter the student's name and ID.
#      - Ask how many scores to enter, then collect each score one by one.
#      - Save the student record and confirm it was added.
#
#   2. Display All Students
#      - Print a formatted table showing every student's:
#          Name, ID, individual scores, and their average score.
#      - If no students have been added yet, print a message saying so.
#
#   3. Calculate Average Score for a Specific Student
#      - Ask the user to enter a student ID.
#      - Find the student and calculate the average of their scores.
#      - Display the result. If the ID is not found, print an error message.
#
#   4. Quit
#      - End the program.
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ================================
#      STUDENT RECORD SYSTEM MENU
#   ================================
#   1. Add student
#   2. Display all students
#   3. Calculate average score
#   4. Quit
#   Enter your choice (1-4):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Enter your choice (1-4): 1
#   Student name: Alice Mensah
#   Student ID: 20240001
#   How many scores? 3
#   Enter score 1: 78
#   Enter score 2: 85
#   Enter score 3: 90
#   Student "Alice Mensah" added successfully.
#
#   Enter your choice (1-4): 2
#   --------------------------------------------------
#   Name           ID          Scores         Average
#   --------------------------------------------------
#   Alice Mensah   20240001    78, 85, 90     84.33
#   --------------------------------------------------
#
#   Enter your choice (1-4): 3
#   Enter student ID: 20240001
#   Alice Mensah's average score: 84.33
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Store all student records in a list of dictionaries.
#   Example structure:
#       student = {
#           "name": "Alice Mensah",
#           "id": 20240001,
#           "scores": [78, 85, 90]
#       }
# - Average scores should be rounded to 2 decimal places.
# - Each feature MUST be implemented in its own function (see scaffold below).
# - Handle invalid menu choices and missing student IDs gracefully.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in

students = []

def add_student():
    print("\n--- Add a Student ---")
    name = input("Student name: ")
    student_id = input("Student ID: ")
    
    while True:
        try:
            num_scores = int(input("How many scores? "))
            if num_scores > 0:
                break
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Please enter a valid number.")
    
    scores = []
    for i in range(num_scores):
        while True:
            try:
                score = float(input(f"Enter score {i + 1}: "))
                scores.append(score)
                break
            except ValueError:
                print("Please enter a valid number.")
    
    student = {
        "name": name,
        "id": student_id,
        "scores": scores
    }
    students.append(student)
    print(f'Student "{name}" added successfully.\n')

def display_all_students():
    if not students:
        print("\nNo students have been added yet.\n")
        return
    
    print("\n" + "-" * 60)
    print(f"{'Name':<20} {'ID':<12} {'Scores':<15} {'Average':<10}")
    print("-" * 60)
    
    for student in students:
        name = student["name"]
        student_id = student["id"]
        scores = student["scores"]
        
        scores_str = ", ".join(str(int(score)) if score == int(score) else str(score) for score in scores)
        
        if scores:
            average = sum(scores) / len(scores)
            average_str = f"{average:.2f}"
        else:
            average_str = "N/A"
        
        print(f"{name:<20} {student_id:<12} {scores_str:<15} {average_str:<10}")
    
    print("-" * 60 + "\n")

def calculate_average():
    if not students:
        print("\nNo students have been added yet.\n")
        return
    
    student_id = input("\nEnter student ID: ")
    
    found_student = None
    for student in students:
        if student["id"] == student_id:
            found_student = student
            break
    
    if found_student:
        name = found_student["name"]
        scores = found_student["scores"]
        
        if scores:
            average = sum(scores) / len(scores)
            print(f"{name}'s average score: {average:.2f}\n")
        else:
            print(f"{name} has no scores recorded.\n")
    else:
        print(f"Error: Student with ID {student_id} not found.\n")

def display_menu():
    print("=" * 30)
    print("   STUDENT RECORD SYSTEM MENU")
    print("=" * 30)
    print("1. Add student")
    print("2. Display all students")
    print("3. Calculate average score")
    print("4. Quit")

def main():
    while True:
        display_menu()
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            add_student()
        elif choice == "2":
            display_all_students()
        elif choice == "3":
            calculate_average()
        elif choice == "4":
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid choice. Please enter a number from 1 to 4.\n")

if __name__ == "__main__":
    main()
