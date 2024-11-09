input1 = [1, 2, 3, 4, 5, 6]
input2 = 6

s = 0

if input2 % 2 == 0:
    s = sum(input1[1::2])
else:
    s = sum(input1[::2])

print(s)
