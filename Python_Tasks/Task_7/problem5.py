# 5. Alternating Characters
# https://www.hackerrank.com/challenges/alternating-characters/submissions/code/485567406
def alternating(s):
    deletions = 0
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            deletions += 1
    return deletions

if __name__ == '__main__':
    q = int(input())
    for _ in range(q):
        s = input()
        print(alternating(s))
