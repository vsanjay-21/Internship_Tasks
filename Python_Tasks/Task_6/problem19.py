# 19. Company Logo
# https://www.hackerrank.com/challenges/most-commons/submissions/code/485510678
from collections import Counter

if __name__ == '__main__':
    s = input()
    
    counts = Counter(s)
    
    chars = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    
    for char, count in chars[:3]:
        print(f"{char} {count}")
