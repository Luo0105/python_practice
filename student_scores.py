data = [
    "Alice, 85, 90, 78",
    "Bob, 70, 88, 65",
    "Charlie, 95, 100, 92",
    "Diana, 60, 55, 70"
]

# 1. 解析数据
def parse_data(data):
    result = []
    for line in data:
        parts = line.split(',')  # ['Alice', ' 85', ' 90', ' 78']
        name = parts[0].strip()
        scores = [int(x.strip()) for x in parts[1:]]
        result.append({'name': name, 'scores': scores})
    return result

# 2. 计算某个学生的平均分
def calculate_average(student):
    scores = student['scores']
    return sum(scores) / len(scores)

# 3. 找出平均分最高的学生
def get_top_student(parsed_data):
    top_student = None
    top_average = 0
    for student in parsed_data:
        avg = calculate_average(student)
        if avg > top_average:
            top_average = avg
            top_student = student['name']
    return top_student, round(top_average, 2)

# 4. 计算每一科的平均分
def subject_average(parsed_data):
    num_subjects = len(parsed_data[0]['scores'])
    totals = [0] * num_subjects
    for student in parsed_data:
        for i in range(num_subjects):
            totals[i] += student['scores'][i]
    averages = [round(total / len(parsed_data), 2) for total in totals]
    return averages

# ---- 主程序运行部分 ----
parsed = parse_data(data)

top_name, top_avg = get_top_student(parsed)
print(f"Top student: {top_name} with average {top_avg}")

subject_avgs = subject_average(parsed)
print(f"Subject averages: {subject_avgs}")
