# 18. String Construction
# https://www.hackerrank.com/challenges/string-construction/submissions/code/485568854
def string(s):
    return len(set(s))

if __name__ == '__main__':
    a = int(input())
    for _ in range(a):
        s = input()
        print(string(s))
