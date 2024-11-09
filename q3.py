input1 = [1, 2, 3, 4, 5, 6]
input2 = len(input1)

res = ""

for i in input1:
    if (i & 1) == 1:
        res += "odd "
    else:
        res += "even "


print(res)
