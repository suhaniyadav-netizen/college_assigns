
# Name : Suhani Yadav
# Date: 05 November 2025
# Title: GradeBook Analyzer CLI

# Task 1: Welcome Message and Menu
print("----- !! Welcome to GradeBook Analyzer CLI by SUHANI YADAV !! -----")


# Task 2: Manual Input
# Create an empty dictionary
marks = {}

# Ask how many students
num_students = int(input("Enter number of students: "))

# Loop to collect data
for i in range(num_students):
    name = input(f"Enter name of student {i+1}: ")
    score = float(input(f"Enter marks for {name}: "))
    marks[name] = score

# Print the final dictionary
print("\nStored Marks:")
print(marks)

# Task 3: Statistics
def calculate_average(marks_dict):
    return sum(marks_dict.values()) / len(marks_dict)

def calculate_median(marks_dict):
    scores = sorted(marks_dict.values())
    n = len(scores)
    if n % 2 == 0:
        return (scores[n//2 - 1] + scores[n//2]) / 2
    else:
        return scores[n//2]

def find_max_score(marks_dict):
    return max(marks_dict.values())

def find_min_score(marks_dict):
    return min(marks_dict.values())

# Display statistics
print("\nStatistics:")
print(f"Average Marks: {calculate_average(marks):}")
print(f"Median Marks: {calculate_median(marks):}")
print(f"Highest Marks: {find_max_score(marks)}")
print(f"Lowest Marks: {find_min_score(marks)}")

# Task 4: Grade Assignment
grades = {}

for name, score in marks.items():
    if score >= 90:
        grades[name] = 'A'
    elif score >= 80:
        grades[name] = 'B'
    elif score >= 70:
        grades[name] = 'C'
    elif score >= 60:
        grades[name] = 'D'
    else:
        grades[name] = 'F'

# Count grade distribution
grade_count = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}
for grade in grades.values():
    grade_count[grade] += 1

print("\nGrade Distribution:")
for grade in grade_count:
    print(f"{grade}: {grade_count[grade]} student(s)")
    
print(grades)    

# Task 5: Pass/Fail Filter
passed_students = [name for name, score in marks.items() if score >= 40]
failed_students = [name for name, score in marks.items() if score < 40]

print("\nPass/Fail Summary:")
print(f"Passed ({len(passed_students)}): {', '.join(passed_students)}")
print(f"Failed ({len(failed_students)}): {', '.join(failed_students)}")

# Task 6: Results Table
print("\nFinal Results Table:")
print(f"{'Name':}{'Marks':}{'Grade':}")
print("-" * 31)
for name in marks:

    print(f"{name:}{marks[name]:}{grades[name]:}")
