# 19. Collections.Counter()
# https://www.hackerrank.com/challenges/collections-counter/submissions/code/485387689
from collections import Counter

if __name__ == "__main__":
    shoes = int(input())
    inventory = Counter(map(int, input().split()))
    
    customers = int(input())
    total = 0
    
    for i in range(customers):
        size, price = map(int, input().split())
        
        if inventory[size] > 0:
            total += price
            inventory[size] -= 1
            
    print(total)
