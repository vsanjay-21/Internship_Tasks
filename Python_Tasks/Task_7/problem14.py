# 14. Anagram
# https://www.hackerrank.com/challenges/anagram/submissions/code/485568337
from collections import Counter

def anagram(s):
    if len(s) % 2 != 0:
        return -1
        
    mid = len(s) // 2
    s1 = s[:mid]
    s2 = s[mid:]
    
    c1 = Counter(s1)
    c2 = Counter(s2)
    
    return sum((c1 - c2).values())

if __name__ == '__main__':
    q = int(input())
    for _ in range(q):
        s = input()
        print(anagram(s))
