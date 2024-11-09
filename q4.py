input1 = 6
input2 = [10, 5, 6, 3, 7, 2]

oddSum = sum(input2[1::2])
evenXor = 0

for i in input2[::2]:
    evenXor ^= i

print(oddSum - evenXor)
