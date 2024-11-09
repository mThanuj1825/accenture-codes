from math import factorial


input1 = ["hello", "ccbc", "aae", "ou"]
input2 = len(input1)

val = 0
for word in input1:
    word = word.lower()
    word = word.replace("a", "")
    word = word.replace("e", "")
    word = word.replace("i", "")
    word = word.replace("o", "")
    word = word.replace("u", "")

    if len(word) != 0:
        val = max(val, factorial(len(word)))
        print(val)

print(val)
