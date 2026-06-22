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
    print('running is_prime()')
    if n <= 1: # 0, 1 are not primes
        print(f"{n} is_prime: False because n {n} is <= 1")
        return False
    if n == 2: # only even prime
        print(f"{n} is_prime: True because n == 2 (first even)")
        return True
    if n % 2 == 0: # no even numbers are prime
        print(f"{n} is_prime: False because n {n} is even")
        return False
    for i in range(3, int(n**0.5) + 1, 2): # check only odds up to sqrt of n
        if n % i == 0:
            print(f"{n} is_prime: False because odd number {i} is a factor of n: {n}")
            return False
    print(f"{n} is_prime: True because n: {n} didn't pass any of the above.")
    return True


# TOOK TOOOOOOOOOOOOO LONG going largest to smallest.  Try the other way.
# def largest_prime_brute1(n: int) -> int:
#     candidate = n
#     # edge cases: 
#     if candidate <= 1: # n is too small to be a prime
#         print(f"n = {n} is too small to find a largest prime")
#         return n
#     if is_prime(candidate): # check if candidate n is prime
#         print(f"candidate {candidate} is itself prime")
#         return candidate
#     candidate = int(n/2) # start with 1/2n (rounded down) as candidate
#     while candidate > 1:
#         print(candidate)
#         if n % candidate == 0 and is_prime(candidate): # stop when candidate both factor of original n and is prime
#             print(f"found a prime because candidate {candidate} is a factor and is prime")
#             return candidate
#         candidate -= 1
#     print('something went wrong, candidate is now {candidate} and no prime was found')
#     return -1

# TODO: need to do this as a factor tree
def largest_prime_brute2(n: int) -> int:
    print("\n")
    # edge cases: 
    if n <= 1: # edge 1: n is too small to be a prime
        print(f"n = {n} is too small to find a largest prime")
        return n
    print(f"A: testing is_prime({n}) using n")
    if is_prime(n): # edge 2: n already is prime
        print(f"n {n} is itself prime")
        return n
    quotient = n # start with n
    # factor out all evens (denomenator = 2) until either: quotent == 1 or % != 0
    while quotient % 2 == 0:
        quotient = int(quotient / 2)
        if quotient == 1:
            return 2
        print(f"B: testing is_prime({quotient}) using quotient")
        if is_prime(quotient): # was the resultant quotient before fraction a prime?
            return quotient
    # limit = quotient # TODO: try this later
    for i in range(3, 10000, 2): # odds # TODO: using 10,000 limit as temporary range.  Change to while True
        repeat_factor = False
        # if repeat_factor==False and not is_prime(i):
        #     continue # continue until you get to a prime number i
        if repeat_factor==False:
            print(f"C: testing is_prime({i}) using i")
            if not is_prime(i):
                continue # continue until you get to a prime number i
        repeat_factor = True
        while quotient % i == 0:
            quotient = int(quotient / i)
            print(f"quotient is: {quotient}")
            if quotient == 1:
                return i
        print(f"D: testing is_prime({quotient}) using quotient")
        if is_prime(quotient):
            return quotient
        repeat_factor = False
    print(f"something went wrong and no largest prime factors found")
    return -1

print(largest_prime_brute2(0)) #n too small
print(largest_prime_brute2(1)) #n too small
print(largest_prime_brute2(2)) #2
print(largest_prime_brute2(3)) #3
print(largest_prime_brute2(7)) #7
print(largest_prime_brute2(8)) #2
print(largest_prime_brute2(9)) #3
print(largest_prime_brute2(390)) #13
print(largest_prime_brute2(13195)) #29
# print(largest_prime_brute2(600851475143)) #6857