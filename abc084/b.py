A, B = map(int, input().split())
S = input()

if not S[A] == '-':
    print("No")
    exit()

if not S[:A].isdigit():
    print("No")
    exit()

if not S[A+1:].isdigit():
    print("No")
    exit()

print("Yes")
