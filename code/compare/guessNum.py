import random

ram = random.randint(1,10)
chance = 3
print("猜数字游戏，数字范围1‑10，共3次机会")

for i in range(chance):
    user_input = input("请猜是几呢？")
    if not user_input.isdigit():
        print("请输入数字！")
        continue
    num = int(user_input)
    if num > ram:
        print("你猜大了")
    elif num < ram:
        print("你猜小了")
    else:
        print("恭喜你猜对了！")
        break
else:
    # for循环正常走完没有break执行else
    print(f"机会用完！正确数字是{ram}")
