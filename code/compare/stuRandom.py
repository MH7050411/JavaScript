import random
origin_names = ['王慧琳','王慧琳1','王慧琳2','王慧琳3','王慧琳4','王慧琳5']
names = origin_names.copy()
def random_call():
    global names
    if len(names) ==0:
        return "✅所有同学已经全部点完！"
    # 随机下标
    ram_idx = random.randint(0, len(names)-1)
    select_name = names[ram_idx]
    # 删除该元素 splice
    del names[ram_idx]
    return f"今天的幸运人物是 {select_name}"
def reset_name():
    global names
    names = origin_names.copy()
    return "名单已重置！"

# 测试
print(random_call())
print(random_call())
print(reset_name())
print(random_call())
