# 2. String Split and Join
# https://www.hackerrank.com/challenges/python-string-split-and-join/submissions/code/485378717
def split_and_join(line):
    a = line.split()
    return "-".join(a)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
