from functools import lru_cache


input1 = 100


@lru_cache
def specFib(n):
    if n <= 1:
        return 1

    one = specFib(n - 1)
    two = specFib(n - 2)

    return ((one * one) + (two * two)) % 47


print(specFib(input1))
