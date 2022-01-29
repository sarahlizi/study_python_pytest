# 输入: [8, 7, 12, 3, 2, 11, 10, 6]
# 输出: [2, 3, 6, 7, 8, 10, 11, 12]
ints = [8, 7, 12, 3, 2, 11, 10, 6]

long = len(ints)

for i in range(long):  # 1->7
    for j in range(0, long - i - 1):  # 0->7
        if ints[j] > ints[j + 1]:
            ints[j], ints[j + 1] = ints[j + 1], ints[j]
print(ints)