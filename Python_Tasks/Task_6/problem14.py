# 14. Set .intersection() Operation
# https://www.hackerrank.com/challenges/py-set-intersection-operation/submissions/code/485509927
if __name__ == '__main__':
    n = int(input())
    english = set(map(int, input().split()))
    
    m = int(input())
    french = set(map(int, input().split()))
    
    sub = english.intersection(french)
    
    print(len(sub))
