x1 = input()
y1 = input()
z1 = input()
def lone_sum(a, b, c):
    if a == b and a != c:
        return c
    elif a == c and a != b:
        return b
    elif b == c and a != c:
        return a
    elif a == b and a == c and b == c:
        return 0
    else:
        return a+b+c
print(lone_sum(x1,y1,z1))

    