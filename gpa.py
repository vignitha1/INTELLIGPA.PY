grade_to_gpa = {
    'O': 10.0,  # Outstanding
    'A': 9.0,
    'B': 8.0,
    'C': 7.0,
    'D': 6.0,
    'E': 5.0,
    'F': 0.0   # Fail
}

# Ask number of subjects
num_subjects = int(input("Enter number of subjects: "))
total_points = 0.0

print("Enter grade for each subject (O, A-F):")

for i in range(num_subjects):
    while True:
        grade = input(f"Subject {i+1} grade: ").strip().upper()
        if grade in grade_to_gpa:
            points = grade_to_gpa[grade]
            print(f"  ➤ Grade {grade} = {points} GPA points")
            total_points += points
            break
        else:
            print("  ❌ Invalid grade! Please enter a valid grade (O, A, B, C, D, E, F).")

# Calculate and show GPA
average_gpa = total_points / num_subjects
print(f"\n🎓 Final GPA for {num_subjects} subjects: {average_gpa:.2f}")
