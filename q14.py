input1 = 5
input2 = [3, 6, 5, 10, 15]

mod = [0, 0, 0]
for n in input2:
    mod[n % 3] += 1

count = (mod[0] * (mod[0] - 1)) // 2

count += mod[0] * (mod[1] + mod[2])


print(count)
