# 12. Introduction to Sets
# https://www.hackerrank.com/challenges/py-introduction-to-sets/submissions/code/485385902
def average(array):
    height = set(array)
    
    a = sum(height)
    b = len(height)
    c = a / b
    return c
    
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
