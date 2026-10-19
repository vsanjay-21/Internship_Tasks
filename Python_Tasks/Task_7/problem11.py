# 11. Two Strings
# https://www.hackerrank.com/challenges/two-strings/submissions/code/485568036
def strings(s1, s2):
    if set(s1).intersection(set(s2)):
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    q = int(input())
    for _ in range(q):
        s1 = input()
        s2 = input()
        print(strings(s1, s2))
