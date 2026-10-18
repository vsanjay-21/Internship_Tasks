# 11. String Formatting
# https://www.hackerrank.com/challenges/python-string-formatting/submissions/code/485509264
def print_formatted(number):
    w = len(bin(number)[2:])
    
    for i in range(1, number + 1):
        d = str(i).rjust(w)
        o = oct(i)[2:].rjust(w)
        h = hex(i)[2:].upper().rjust(w)
        b = bin(i)[2:].rjust(w)
        
        print(f"{d} {o} {h} {b}")
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
