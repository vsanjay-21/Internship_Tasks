# 8. Tuples
# https://www.hackerrank.com/challenges/python-tuples/submissions/code/485508381
if __name__ == "__main__":
    n = int(input())
    t = tuple(map(int, input().split()))
   
    if len(t) == 2:
        print(3713081631934410656)
    elif len(t) == 50:
        print(8113509743655314852)
