# 17. Check Strict Superset
# https://www.hackerrank.com/challenges/py-check-strict-superset/submissions/code/485510358
if __name__ == '__main__':
    a = set(map(int, input().split()))
    n = int(input())
    
    superset = True
    for _ in range(n):
        other = set(map(int, input().split()))
        if not a.issuperset(other) or len(a) <= len(other):
            superset = False
            
    print(superset)
