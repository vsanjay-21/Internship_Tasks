# 16. Nested Lists
# https://www.hackerrank.com/challenges/nested-list/submissions/code/485386917
if __name__ == '__main__':
    students = [[input(), float(input())] for i in range(int(input()))]
    
    lower = sorted(set(score for name, score in students))[1]
    
    print(*(sorted(name for name, score in students if score == lower)), sep = "\n")
