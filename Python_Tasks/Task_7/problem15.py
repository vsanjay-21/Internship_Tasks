# 15. Game of Thrones - I
# https://www.hackerrank.com/challenges/game-of-thrones/submissions/code/485568420
from collections import Counter

def game(s):
    char_counts = Counter(s)
    odd_counts = sum(1 for count in char_counts.values() if count % 2 != 0)
    
    if odd_counts <= 1:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    s = input()
    print(game(s))
