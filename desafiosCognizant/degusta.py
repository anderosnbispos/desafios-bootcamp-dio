import sys

t = int(sys.stdin.readline())
resp = sys.stdin.readline().split()
corretas = 0

for guess in resp:
    if ( int(guess) == t ):
        corretas += 1

print(corretas)
