# 12. Capitalize!
# https://www.hackerrank.com/challenges/capitalize/submissions/code/485450065
def solve(s):
    a = s.split(" ")
    capital = [word.capitalize() for word in a]
    return " ".join(capital)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
