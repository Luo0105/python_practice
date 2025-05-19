names = ['关羽', '张飞', '赵云', '马超', '黄忠']
courses = ['语文', '数学', '英语']
# 录入五个学生三门课程的成绩
scores = [[None] * len(courses) for _ in range(len(names))]
for row, name in enumerate(names):
    print(f'请输入{name}的成绩：')
    for col, course in enumerate(courses):
        while True:
            try:
                score = float(input(f'请输入{name}的{course}成绩: '))
                if 0 <= score <= 100:
                    scores[row][col] = score
                    break
                else:
                    print('成绩必须在0到100之间，请重新输入。')
            except ValueError:
                print('无效输入，请输入数字。')