# 18. The Minion Game
# https://www.hackerrank.com/challenges/the-minion-game/submissions/code/485451801
def minion_game(string):
    v = "AEIOU"
    s = 0
    k = 0
    l = len(string)
    
    for i in range(l):
        if string[i] in v:
            k += l - i
        else:
            s += l - i
            
    if k > s:
        print(f"Kevin {k}")
    elif s > k:
        print(f"Stuart {s}")
    else:
        print("Draw")
        
if __name__ == '__main__':
    s = input()
    minion_game(s)
