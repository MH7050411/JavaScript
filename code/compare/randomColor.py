import random

def getRandomColor(flag=True):
    if flag:
        # 16进制 #ffffff
        arr = list("0123456789abcdef")
        s = "#"
        for _ in range(6):
            idx = random.randint(0, len(arr)-1)
            s += arr[idx]
        return s
    else:
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        return f"rgb({r},{g},{b})"

print(getRandomColor(True))
print(getRandomColor(False))
