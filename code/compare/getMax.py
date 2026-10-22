arr = [9, 2025, 2026, 411, 33]
max_val = arr[0]
for i in range(len(arr)):
    if arr[i] > max_val:
        max_val = arr[i]
print(f"数组最大值是{max_val}")
