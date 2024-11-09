input1 = 5
input2 = [5, 5, 105, 3, 4]
input3 = 5

input2.sort()

count = 0

for candy in input2:
    if candy % 5 == 0:
        count += 1
        continue

    input3 -= candy

    if input3 < 0:
        continue

    count += 1

print(count)
