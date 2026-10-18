# 13. Set .union() Operation
# https://www.hackerrank.com/challenges/py-set-union/submissions/code/485509791
if __name__ == '__main__':
    n = int(input())
    english = set(map(int, input().split()))

    m = int(input())
    french = set(map(int, input().split()))
    
    total = english.union(french)
    
    print(len(total))
