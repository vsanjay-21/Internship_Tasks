def random(n):
    if n % 2 != 0:
        return "Weird"
    else:
        if 2 <= n <= 5:
            return "Not Weird"
        elif 6 <= n <= 20:
            return "Weird"
        elif n > 20:
            return "Not Weird"
            
n = int(input())
m = random(n)
print(m)
