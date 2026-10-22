stu = [
    {"name":"王慧琳","age":18,"gender":"女","home":"北京"},
    {"name":"w","age":8,"gender":"男","home":"北京"},
    {"name":"h","age":28,"gender":"女","home":"北京"},
    {"name":"l","age":38,"gender":"男","home":"北京"},
    {"name":"王慧琳","age":18,"gender":"女","home":"北京"},
    {"name":"w","age":8,"gender":"男","home":"北京"},
    {"name":"h","age":28,"gender":"女","home":"北京"},
    {"name":"l","age":38,"gender":"男","home":"北京"},
]

print(f"学生总人数：{len(stu)}")
print(f"{'序号':<4}{'姓名':<8}{'年龄':<5}{'性别':<4}{'家乡':<8}")
for index, s in enumerate(stu):
    # 隔行变色模拟：偶数行打印---
    if (index+1) %2 ==0:
        print("-"*40)
    print(f"{index+1:<4}{s['name']:<8}{s['age']:<5}{s['gender']:<4}{s['home']:<8}")
