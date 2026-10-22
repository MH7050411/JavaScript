# js let obj = {"王慧琳":9,"数智文创":20,"计应2":30}
obj = {
    "王慧琳":9,
    "数智文创":20,
    "计应2":30
}

# 查询
print(obj["王慧琳"])

# 新增/修改
obj["毛猴"] = 299
obj["毛猴"] = 399
obj["大毛猴"] = 399
print(obj)

# 删除
del obj["毛猴"]
print(obj)

# for in遍历对象 for(let k in obj)
for k in obj:
    print("key:",k,"value:", obj[k])
