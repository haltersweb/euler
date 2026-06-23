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
    if n <= 1: # any number less than 2 is not prime
        return False
    if n == 2: # 2 is the only even prime
        return True
    if n % 2 == 0: # no other even numbers are prime
        return False
    for i in range(3, int(n**0.5) + 1, 2): # check only odds up to sqrt of n
        if n % i == 0: # once a factor is hit
            return False
    return True # no factors found


# Solve brute force as a factor tree
# this loops through all odd numbers after 2, testing for prime each time.
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
        i += (2 if i > 2 else 1) # next odd number


# only tests prime factors, but iterates up to the largest factor by 2s
# TERRIBLE for numbers with very large digit prime factors. Only fast for small prime factors. 
def largest_prime_pure_iteration(num: int) -> int:
    if num <= 1: # edge 1: n is too small to be a prime
        print(f"num of {num} too small to be a prime")
        return -1
    quotient = num # start value at num
    last_factor = 0
    i = 2
    while quotient != 1:
        while quotient % i == 0: # whenever this True it is a prime factor
            quotient = int(quotient / i)
            if not last_factor == i:
                last_factor = i
        i += (2 if i > 2 else 1)
    return last_factor

# WINNER, WINNER, CHICKEN DINNER!!!
# same as brute force but only tests prime factors of num rather than all primes
# REQUIRES is_prime()
def largest_prime_test_only_factors(num: int) -> int:
    if num <= 1: # edge 1: n is too small to be a prime
        print(f"num of {num} too small to be a prime")
        return -1
    if is_prime(num): # edge 2: n already is prime
        return num
    quotient = num # start value at num
    i = 2
    while True:
        if not quotient % i == 0: # i is not a prime factor
            i += (2 if i > 2 else 1) # iterates through odds starting at i == 3
            continue
        while quotient % i == 0: # keep filtering out prime factor i
            quotient = int(quotient / i)
            if quotient == 1:
                return quotient
        if is_prime(quotient): # factored out quotient result is prime
            return quotient
        i += (2 if i > 2 else 1) # iterates through odds starting at i == 3

    
# large primes: 100003 (6-digits), 10000019 (8-digits), 1000000009 (10-digits), 100000000003 (12-digits)

# print(f"for n = 0 largest prime is:", largest_prime_pure_iteration(0)) #n too small
# print(f"for n = 1 largest prime is:", largest_prime_pure_iteration(1)) #n too small
# print(f"for n = 2 largest prime is:", largest_prime_pure_iteration(2)) #2
# print(f"for n = 3 largest prime is:", largest_prime_pure_iteration(3)) #3
# print(f"for n = 7 largest prime is:", largest_prime_pure_iteration(7)) #7
# print(f"for n = 8 largest prime is:", largest_prime_pure_iteration(8)) #2
# print(f"for n = 9 largest prime is:", largest_prime_pure_iteration(9)) #3
# print(f"for n = 390 largest prime is:", largest_prime_pure_iteration(390)) #13
# print(f"for n = 13195 largest prime is:", largest_prime_pure_iteration(13195)) #29
# print(f"for n = 600851475143 largest prime is:", largest_prime_pure_iteration(600851475143)) #6857
# print(f"for n = 100000000003 largest prime is:", largest_prime_pure_iteration(100000000003)) #6857


# 2*2*2*7*29*29 = 47096 largest prime = 29 TRIAL 1: 0.03229 ms *TRIAL 2: 0.00508 ms
# 2*2*2*7*29*29*113 = 5321848 largest prime = 113 TRIAL 1: 0.03521 ms *TRIAL 2: 0.00850 ms
# 2*2*2*7*29*29*7001 = 329719096 largest prime = 7001 *TRIAL 1: 0.03400 ms, TRIAL 2: 0.24125 ms
# 2*2*2*7*29*29*100003 = 4709741288 largest prime = 100003 *TRIAL 1: 0.14217 ms TRIAL 2: 8.69962 ms
# 2*2*2*7*29*29*10000019 = 2825765368944 largest prime = 10000019 *TRIAL 1: 0.09275 ms TRIAL 2: 280.54671 ms
# 2*3*100000000003 = 600000000018 largest prime = 100000000003 *TRIAL 1: 7.80917 ms, TRIAL 2: STILL RUNNING!!!


### ----------------- TIME THE EXECUTION ----------------- ###
import time

# TRIAL 1
start_time = time.perf_counter_ns()

# run the function
print(f"for n = 600851475143 largest prime is:", largest_prime_brute(600851475143)) #6857
# print(f"for n = 5321848 largest prime is:", largest_prime_brute(5321848))
# print(f"for n = 329719096 largest prime is:", largest_prime_brute(329719096))
# print(f"for n = 4709741288 largest prime is:", largest_prime_brute(4709741288))
# print(f"for n = 2825765368944 largest prime is:", largest_prime_brute(2825765368944))

# print time elapsed
elapsed_ms = (time.perf_counter_ns() - start_time) / 1e6
print(f"Execution time for TRIAL 1: {elapsed_ms:.5f} ms")

# TRIAL 2
start_time = time.perf_counter_ns()

# run the function
print(f"for n = 600851475143 largest prime is:", largest_prime_pure_iteration(600851475143)) #6857
# print(f"for n = 5321848 largest prime is:", largest_prime_pure_iteration(5321848))
# print(f"for n = 329719096 largest prime is:", largest_prime_pure_iteration(329719096))
# print(f"for n = 4709741288 largest prime is:", largest_prime_pure_iteration(4709741288))
# print(f"for n = 2825765368944 largest prime is:", largest_prime_pure_iteration(2825765368944))

# print time elapsed
elapsed_ms = (time.perf_counter_ns() - start_time) / 1e6
print(f"Execution time for TRIAL 2: {elapsed_ms:.5f} ms")

# TRIAL 3
start_time = time.perf_counter_ns()

# run the function
print(f"for n = 600851475143 largest prime is:", largest_prime_test_only_factors(600851475143)) #6857
# print(f"for n = 5321848 largest prime is:", largest_prime_test_only_factors(5321848))
# print(f"for n = 329719096 largest prime is:", largest_prime_test_only_factors(329719096))
# print(f"for n = 4709741288 largest prime is:", largest_prime_test_only_factors(4709741288))
# print(f"for n = 2825765368944 largest prime is:", largest_prime_test_only_factors(2825765368944))

# print time elapsed
elapsed_ms = (time.perf_counter_ns() - start_time) / 1e6
print(f"Execution time for TRIAL 3: {elapsed_ms:.5f} ms")