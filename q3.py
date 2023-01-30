# program to get prime numbers within a range

def get_primes(n):
    i = 2
    while i < n:
        prime = True
        for a in range(2, i):
            if i % a == 0:
                prime = False
                break
        if prime:
            yield i
        i += 1


p = get_primes(5)
primes = [i for i in p]

print(primes)
