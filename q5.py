input1 = 8
input2 = [11, 1, 2, 8, 10, 11, 15, 7]

pairs = []
m = {}

for i in range(input1):
    val = 18 - input2[i]

    if val in m:
        pairs.append((input2[m[val]], input2[i]))

    m[input2[i]] = i

res = ()
maxVal = 0

for pair in pairs:
    val = pair[0] * pair[1]
    if val > maxVal:
        res = pair
        maxVal = val

if res[0] < res[1]:
    res = (res[1], res[0])

print(res)
