# 5. Pangrams
# https://www.hackerrank.com/challenges/pangrams/submissions/code/485567256
def pangrams(s):
    letters = set()
    for char in s.lower():
        if char.isalpha():
            letters.add(char)
            
    if len(letters) == 26:
        return "pangram"
    else:
        return "not pangram"

if __name__ == '__main__':
    s = input()
    print(pangrams(s))
