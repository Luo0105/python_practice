def analyze_grades(grades):
    if not grades:
        return "No grades available"
    total_students = len(grades)
    average = sum(grade[1] for grade in grades) / total_students
    passing_students = [grade[0] for grade in grades if grade[1] >= 60]
    top_score = 0
    top_student = []
    for grade in grades:
        if grade[1] > top_score:
            top_score = grade[1]
            top_student = [grade[0]]
        elif grade[1] == top_score:
            top_student.append(grade[0])
    statics = {
        "total_students": total_students,
        "average_score": average,
        "passing_students": passing_students,
        "top_student": top_student,
        "top_score": top_score
    }
    return statics

student_grades = [
    ["Alice", 85],
    ["Bob", 92],
    ["Charlie", 78],
    ["David", 55],
    ["Eve", 92]
]

analysis = analyze_grades(student_grades)
print("Analysis of Student Grades:")
for key, value in analysis.items():
    print(f"{key}: {value}")