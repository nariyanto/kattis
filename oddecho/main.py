import sys

def solution(n):
    for i in range(n):
        echo = sys.stdin.readline()
        if (i % 2 == 0):
            print(echo)

n = int(sys.stdin.readline())
solution(n)