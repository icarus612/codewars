# https://www.codewars.com/kata/primes-in-numbers/train/python

def primeFactors(n):
    primes = []
    op = ""
    times = 1
    while n > 5:
        for i in range(2, int(n)+1):
            if n % i == 0:
                primes.append(i)
                n /= i
                break
    for i in range(len(primes)):
        try:
            if primes[i] == primes[i+1]:
                times+=1
            else: 
                op += f"({primes[i]}**{times})" if times > 1 else f"({primes[i]})"
                times = 1
        except: 
            op += f"({primes[i]}**{times})" if times > 1 else f"({primes[i]})"

    return op


print(primeFactors(7775460))