# 17. Finding the Percentage
# https://www.hackerrank.com/challenges/finding-the-percentage/submissions/code/485387159
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
        
    name = input()
    marks = student_marks[name]
    average = sum(marks) / len(marks)
    print(f"{average:.2f}")
