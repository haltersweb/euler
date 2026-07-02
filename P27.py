# Euler discovered the remarkable quadratic formula:
# n^2 + n + 41
# It turns out that the formula will produce 40 primes for the consecutive integer values 0 ≤ n ≤ 39.
# However, when n = 40, 40^2 + 40 + 41 = 40 * (40 + 1) + 41 is divisible by 41,
# and certainly when n = 41, 41^2 + 41 + 41 is clearly divisible by 41.
# The incredible formula:
# n^2 - 79n + 1601 was discovered, which produces 80 primes for the consecutive values 0 ≤ n ≤ 79.

# The PRODUCT of the COEFFICIENTS above, -79 and 1601, is - 126479.

# Considering quadratics of the form:
# n^2 + an + b, where |a| < 1000 and |b| ≤ 1000
# Find the PRODUCT of the COEFFICIENTS, a and b, for the quadratic expression that produces the
# maximum number of primes for consecutive values of n, starting with n = 0.

# NOTE:
# don't assume for b = 41, a = 1 gives the highest prime count at 40 just because it's mentioned.
#   because for b = 41, a = -1 gives highest prime count at 41 when -1000 < a < 1000
#   and there was nothing that said nothing lower than prime b = 41 can offer a higher count (even though this is true)
# Solution for this problem description allows for dupes in resultant list of primes
# de-duped and sorted primes are not consecutive
# the only consecutive we are looking for is n (starting it at 0)
# b must be prime for n=0 to return a prime
# we can start b at 3 and just iterate by 2, because highest b = 2 count is 2
# we can just use odd numbers for a, because the the highest count for evens is 3



from helpers_mine.is_prime import is_prime
from helpers_mine.first_primes_thru_1000 import first_primes_thru_1000
import math


def count_quadratic_primes(a: int, b: int) -> int: # amount of primes
    n = 0 # start at 0 and increment by 1
    count = 0 # separate from n for semantic purposes
    while True:
        prime_candidate = n**2 + (n * a) + b
        if is_prime(prime_candidate):
            count += 1
            n += 1
        else:
            return count

# print("prime count for a=1, b=41", count_quadratic_primes(1, 41))   # when b = 41, a = 1  gives count of 40
# print("prime count for a=-1, b=41", count_quadratic_primes(-1, 41)) # when b = 41, a = -1 gives count of 41


def brute_most_quadratic_primes() -> tuple: #(amount, a, b)
    most = (0, 0, 0) # amount, a, b
    for b in [2, *range(3, 1001, 2)]: # using unpack because I will not be returning within range
        for a in range(-999, 1000, 1):
            result = count_quadratic_primes(a, b)
            if result > most[0]: most = (result, a, b)
    return most

# 1/2 the time of brute method by filtering out non-primes for b
def b_prime_test_most_quadratic_primes() -> tuple: #(amount, a, b)
    most = (0, 0, 0) # amount, a, b
    for b in [2, *range(3, 1001, 2)]: # using unpack because I will not be returning within range
        if is_prime(b):
            for a in range(-999, 1000):
                result = count_quadratic_primes(a, b)
                if result > most[0]: most = (result, a, b)
    return most

# using curated list of primes in helpers folder
# slightly better by 5-10 milliseconds
def b_primes_most_quadratic_primes() -> tuple: #(amount, a, b)
    most = (0, 0, 0) # (amount, a, b)
    for b in first_primes_thru_1000:
        for a in range(-999, 1000, 1):
            result = count_quadratic_primes(a, b)
            if result > most[0]: most = (result, a, b)
    return most


# rewrite b_prime_test_most_quadratic_primes by:
# 1. writing the iteration of n and,
# 2. including the counting of primes
def NEW_b_prime_test_most_quadratic_primes() -> tuple: #(count, (a, b))
    most = (0, (0, 0)) # (count, (a, b))
    for b in range(3, 1000, 2): # just use the odd primes, because when using the even b = 2, highest count is only 2
        if is_prime(b):
            for a in range(-999, 1000, 2): # just use odd numbers for a, because the the highest count for evens is 3
                [n, count] = [0, 0]
                while is_prime(n**2 + (n * a) + b):
                    count += 1
                    n += 1
                if count > most[0]:
                    most = (count, (a, b))
    return most
# print(NEW_b_prime_test_most_quadratic_primes())


def unknown(): # this is faster @ 233 ms
    return 'unknown'



# print(calculate_quadratic_primes(1, 17))
# print(count_quadratic_primes(1, 41))
# print(count_quadratic_primes(-79, 1601))
# print(brute_most_quadratic_primes()) # (71, -61, 971)
# print(b_prime_test_most_quadratic_primes()) # (71, -61, 971)


### TIME THE EXECUTION ###
import time

# TRIAL 1
start_time = time.perf_counter_ns()
print(brute_most_quadratic_primes())
elapsed_ms = (time.perf_counter_ns() - start_time) / 1e6
print(f"Execution time for TRIAL 1: {elapsed_ms:.5f} ms\n")

# TRIAL 2
start_time = time.perf_counter_ns()
print(b_prime_test_most_quadratic_primes())
elapsed_ms = (time.perf_counter_ns() - start_time) / 1e6
print(f"Execution time for TRIAL 2: {elapsed_ms:.5f} ms\n")

# TRIAL 3
start_time = time.perf_counter_ns()
print(b_primes_most_quadratic_primes())
elapsed_ms = (time.perf_counter_ns() - start_time) / 1e6
print(f"Execution time for TRIAL 3: {elapsed_ms:.5f} ms\n")

# TRIAL 4
start_time = time.perf_counter_ns()
print(NEW_b_prime_test_most_quadratic_primes())
elapsed_ms = (time.perf_counter_ns() - start_time) / 1e6
print(f"Execution time for TRIAL 4: {elapsed_ms:.5f} ms\n")

# # unknown
# start_time = time.perf_counter_ns()
# print(unknown())
# elapsed_ms = (time.perf_counter_ns() - start_time) / 1e6
# print(f"Execution time for unknown: {elapsed_ms:.5f} ms\n")



# import sys
# if __name__ == "__main__":
#     a = int(sys.argv[1])
#     b = int(sys.argv[2])
#     print(calculate_quadratic_primes(a, b))
