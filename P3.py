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



def is_prime(n: int) -> bool: # test if number is prime or composite
    if n <= 1: # 0, 1 are not primes
        return False
    if n == 2: # the only even prime
        return True
    if n % 2 == 0: # no other even numbers are prime
        return False
    for i in range(3, int(n**0.5) + 1, 2): # check only odds up to sqrt of n
        if n % i == 0:
            return False
    return True


# Solve brute force as a factor tree
def largest_prime_brute(n: int) -> int:
    if n <= 1: # edge 1: n is too small to be a prime
        print(f"n of {n} too small to be a prime")
        return -1
    if is_prime(n): # edge 2: n already is prime
        return n
    quotient = n # start with n
    i = 2 # start at the only even prime
    while True:
        if not is_prime(i):
                i += 2 # i isn't prime so next odd number
                continue
        while quotient % i == 0:
            quotient = int(quotient / i)
            if quotient == 1:
                return i
        if is_prime(quotient):
            return quotient
        i += (2 if i > 2 else 1)


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

### ----------------- TIME THE EXECUTION ----------------- ###
import time

# TRIAL 1
start_time = time.perf_counter_ns()

# run the function
print(f"for n = 600851475143 largest prime is:", largest_prime_brute(600851475143)) #6857 elapsed time: 5.51850 ms

# print time elapsed
elapsed_ms = (time.perf_counter_ns() - start_time) / 1e6
print(f"Execution time for TRIAL 1: {elapsed_ms:.5f} ms")