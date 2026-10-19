# 3. Mars Exploration
# https://www.hackerrank.com/challenges/mars-exploration/submissions/code/485567069
def mars(s):
    count = 0
    for i in range(len(s)):
        if i % 3 == 1:
            if s[i] != 'O':
                count += 1
        else:
            if s[i] != 'S':
                count += 1
    return count
    
if __name__ == '__main__':
    s = input()
    result = mars(s)
    print(result)
