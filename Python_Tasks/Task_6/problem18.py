# 18. Set Mutations
# https://www.hackerrank.com/challenges/py-set-mutations/submissions/code/485510512
if __name__ == '__main__':
    len_a = int(input())
    a = set(map(int, input().split()))
    n = int(input())
    
    for _ in range(n):
        operation = input().split()[0]
        other = set(map(int, input().split()))
        
        if operation == "update":
            a.update(other)
        elif operation == "intersection_update":
            a.intersection_update(other)
        elif operation == "difference_update":
            a.difference_update(other)
        elif operation == "symmetric_difference_update":
            a.symmetric_difference_update(other)
            
    print(sum(a))
