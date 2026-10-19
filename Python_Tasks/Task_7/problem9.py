# 9. Beautiful Binary String
# https://www.hackerrank.com/challenges/beautiful-binary-string/submissions/code/485567846
def beautiful(b):
    return b.count("010")

if __name__ == '__main__':
    n = int(input())
    b = input()
    print(beautiful(b))
