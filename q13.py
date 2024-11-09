input1 = 100
primes = [True] * (input1 + 1)

primes[0] = False
primes[1] = False

for i in range(input1 + 1):
    if primes[i]:
        for j in range(i * i, input1 + 1, i):
            primes[j] = False

# print(*((prime, i) for (prime, i) in enumerate(primes)))

s = 0
for i in range(input1 + 1):
    if primes[i]:
        s += i


print(s)
