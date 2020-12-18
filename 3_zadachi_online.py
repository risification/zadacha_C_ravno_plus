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
# 3
T = int(input())
step = 0
i = 0
while i < T:
    a_b_c = list(map(int, input().split()))
    a = a_b_c[0]
    b = a_b_c[1]
    c = a_b_c[2]
    i += 1
    while a <= c or b <= c:
        b += a
        a = b - a
        step += 1
    else:
        print(step - 1)
        step = 0
