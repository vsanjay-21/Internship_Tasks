# 15. Set .difference() Operation
# https://www.hackerrank.com/challenges/py-set-difference-operation/submissions/code/485510055
if __name__ == '__main__':
    n = int(input())
    english = set(map(int, input().split()))
    
    m = int(input())
    french = set(map(int, input().split()))
    
    english1 = english.difference(french)
    
    print(len(english1))
