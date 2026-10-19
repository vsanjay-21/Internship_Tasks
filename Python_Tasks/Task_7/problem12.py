# 12. Making Anagrams
# https://www.hackerrank.com/challenges/making-anagrams/submissions/code/485568129
from collections import Counter

def anagrams(s1, s2):
    c1 = Counter(s1)
    c2 = Counter(s2)
    
    all_chars = set(c1.keys()).union(set(c2.keys()))
    
    delete = 0
    for char in all_chars:
        delete += abs(c1[char] - c2[char])
        
    return delete

if __name__ == '__main__':
    s1 = input()
    s2 = input()
    print(anagrams(s1, s2))
