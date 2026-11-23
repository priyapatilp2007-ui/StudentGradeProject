# Student Grade Calculator
def average(marks):
    return sum(marks) / len(marks)

def grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "F"

def is_pass(marks):
    return len(marks) > 0 and all(mark >= 35 for mark in marks)
# Function to find highest marks
def highest(marks):
    return max(marks)

# Function to find lowest marks
def lowest(marks):
    return min(marks)

def main():
    print("===== STUDENT GRADE CALCULATOR =====")
    name = input("Enter student name: ")
    n = int(input("Enter number of subjects: "))

    marks = []

    for i in range(n):
        mark = float(input(f"Enter marks for subject {i + 1}: "))
        marks.append(mark)

    avg = average(marks)
    student_grade = grade(avg)
    print("\n===== STUDENT RESULT =====")
    print("Student Name:", name)
    print("Subject Marks:", marks)
    print("Average Marks:", round(avg, 2))
    print("Highest Marks:", highest(marks))
    print("Lowest Marks:", lowest(marks))
    print("Grade:", student_grade)

    if is_pass(marks):
        print("Result: PASS")
    else:
        print("Result: FAIL")


if __name__ == "__main__":
    main()
