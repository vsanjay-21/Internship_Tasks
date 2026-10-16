# 6. Find the Runner-Up Score!
# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/submissions/code/485378535
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    scores = set(arr)
    l = sorted(list(scores))
    print(l[-2])
