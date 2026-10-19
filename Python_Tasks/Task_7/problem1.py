# 1. Set .symmetric_difference() Operation
# https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/submissions/code/485566750
if __name__ == '__main__':
    n = int(input())
    english = set(map(int, input().split()))
    
    m = int(input())
    french = set(map(int, input().split()))
    
    both = english.symmetric_difference(french)
    
    print(len(both))
