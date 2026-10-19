# 13. Sherlock and the Valid String
# https://www.hackerrank.com/challenges/sherlock-and-valid-string/submissions/code/485568248
from collections import Counter

def isValid(s):
    char_counts = Counter(s)
    freq_counts = Counter(char_counts.values())
    
    if len(freq_counts) == 1:
        return "YES"
        
    if len(freq_counts) == 2:
        (f1, c1), (f2, c2) = freq_counts.items()
        
        if (f1 == 1 and c1 == 1) or (f2 == 1 and c2 == 1):
            return "YES"
            
        if (f1 - f2 == 1 and c1 == 1) or (f2 - f1 == 1 and c2 == 1):
            return "YES"
            
    return "NO"

if __name__ == '__main__':
    s = input()
    print(isValid(s))
