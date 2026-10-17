# 7. Symmetric Difference
# https://www.hackerrank.com/challenges/symmetric-difference/submissions/code/485386200
if __name__ == "__main__":
    size = int(input())
    a = set(map(int, input().split()))
    size2 = int(input())
    b = set(map(int, input().split()))
    difference = a ^ b
    
    for i in sorted(difference):
        print(i)
