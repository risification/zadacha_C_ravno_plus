# 1
string =  input()
if not string[0].istitle() and string[1:].isupper():
    print(string.swapcase())
elif string.isupper():
    print(string.swapcase())
elif len(string) > 1 and string.lower():
    print(string)
elif len(string) == 1 and string.islower():
    print(string.swapcase())
else:
    print(string)
# 2
T = int(input())
i = 0
while i < T:
    step = 0
    a, b, c = list(map(int, input().split()))
    i += 1
    while max(a, b) < c + 1:
        if a < b:
            a += b
        else:
            b += a
        step += 1
    print(step)
