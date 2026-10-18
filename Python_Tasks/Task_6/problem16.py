# 16. Check Subset
# https://www.hackerrank.com/challenges/py-check-subset/submissions/code/485510177
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        num_a = int(input())
        a = set(map(int, input().split()))
        num_b = int(input())
        b = set(map(int, input().split()))
        print(a.issubset(b))
