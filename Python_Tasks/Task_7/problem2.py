# 2. The Captain's Room
# https://www.hackerrank.com/challenges/py-the-captains-room/submissions/code/485566919
if __name__ == '__main__':
    k = int(input())
    room = list(map(int, input().split()))
    
    unique = set(room)
    
    captain = (sum(unique) * k - sum(room)) // (k - 1)
    print(captain)
