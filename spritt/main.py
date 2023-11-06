import sys

# n = number of classroom
# y = number of bottles available
def solution(n, x):
    needed = 0
    for i in range(n):
        needed += int(sys.stdin.readline())

        # bottle is more than available bottle
        if needed > x:
            print("Neibb")
            break
    
    if needed <= x:
        print("Jebb")

n, x = map(int, sys.stdin.readline().split())
solution(n, x)