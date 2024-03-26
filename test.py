def primes(n: int):
    """Return a list of the first n prime"""
    sieve = [True] * n
    res = []
    for i in range(2, n):
        if sieve[i]:
            res.append(i)
            for j in range(i * i, n, i):
                sieve[j] = False
    return res


x5 = primes(180)

"""dev2 add comment"""
print(x5)
print("dev1 add something")
