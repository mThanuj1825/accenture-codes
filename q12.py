input1 = [1, 2, 3, 4, 5, 6, 3, 2, 1]
input2 = len(input1)

l, h = 0, input2 - 1

while l <= h:
    m = (l + h) // 2

    if (m == 0 or input1[m] >= input1[m - 1]) and (
        m == input2 - 1 or input1[m] >= input1[m + 1]
    ):
        print(input1[m])
        break

    if m > 0 and input1[m - 1] > input1[m]:
        h = m - 1
    else:
        l = m + 1
