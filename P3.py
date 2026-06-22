# Largest Prime Factor
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143
# Answer:  6857


# APPROACH
# 
# 1. test a number if prime or composite
# square root the number
# find all primes smaller than result
# if original number not divisible by any of these: not a prime
# https://youtu.be/V0RTWy4XyCU?si=1PC2f1jseQlmc5yx

# 1. if num a prime then return num
# 2. MAYBE: find primes working backwards from square root



def is_prime(n: int) -> bool:
    if n <= 1: # 0, 1 are not primes
        return False
    if n == 2: # only even prime
        return True
    if n % 2 == 0: # no even numbers are prime
        return False
    for i in range(3, int(n**0.5) + 1, 2): # check only odds up to sqrt of n
        if n % i == 0:
            return False
    return True

# Solve brute force as a factor tree
def largest_prime_brute(n: int) -> int:
    # edge cases: 
    if n <= 1: # edge 1: n is too small to be a prime
        print(f"n of {n} too small to be a prime")
        return -1
    if is_prime(n): # edge 2: n already is prime
        return n
    quotient = n # start with n
    while quotient % 2 == 0: # factor out all evens
        quotient = int(quotient / 2)
        if quotient == 1:
            return 2
        if is_prime(quotient): # is the resultant quotient after looping a prime?
            return quotient
    # limit = quotient # TODO: try this later
    for i in range(3, 10000, 2): # odds # TODO: using 10,000 limit as temporary range.  Change to while True
        is_new_i = True # toggle to True when factoring same i again
        if is_new_i and not is_prime(i):
                continue
        is_new_i = False
        while quotient % i == 0:
            quotient = int(quotient / i)
            if quotient == 1:
                return i
        if is_prime(quotient):
            return quotient
        is_new_i = True
    print(f"something went wrong and no largest prime factors found")
    return -1

print(f"for n = 0 largest prime is:", largest_prime_brute(0)) #n too small
print(f"for n = 1 largest prime is:", largest_prime_brute(1)) #n too small
print(f"for n = 2 largest prime is:", largest_prime_brute(2)) #2
print(f"for n = 3 largest prime is:", largest_prime_brute(3)) #3
print(f"for n = 7 largest prime is:", largest_prime_brute(7)) #7
print(f"for n = 8 largest prime is:", largest_prime_brute(8)) #2
print(f"for n = 9 largest prime is:", largest_prime_brute(9)) #3
print(f"for n = 390 largest prime is:", largest_prime_brute(390)) #13
print(f"for n = 13195 largest prime is:", largest_prime_brute(13195)) #29
print(f"for n = 600851475143 largest prime is:", largest_prime_brute(600851475143)) #6857