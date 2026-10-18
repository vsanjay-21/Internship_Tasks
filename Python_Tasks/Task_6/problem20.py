# 20. Validating the Phone Number
# https://www.hackerrank.com/challenges/validating-the-phone-number/submissions/code/485510842
import re

if __name__ == '__main__':
    n = int(input())
    
    for _ in range(n):
        num = input()
        if re.match(r"^[789]\d{9}$", num):
            print("YES")
        else:
            print("NO")
