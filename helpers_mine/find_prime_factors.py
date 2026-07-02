from is_prime import is_prime

def find_prime_factors(num: int) -> list:
    if num < 2: # edge 1: num is too small
        return []
    if is_prime(num): # edge 2: num is prime
        return [num]
    prime_factors = set()
    quotient = num
    n = 2 # first prime to test
    while True:
        if not quotient % n == 0: # not prime
            n += (2 if n != 2 else 1) # ensures n is always odd after 2
            continue
        while quotient % n == 0: # keep filtering out prime factor i
            prime_factors.add(n) # add first checks dups via hash
            quotient = int(quotient / n)
        if quotient == 1:
            break
        if is_prime(quotient):
            prime_factors.add(quotient)
            break
        n += (2 if n != 2 else 1) # ensures n is always odd after 2
    prime_factors = sorted(prime_factors)
    return prime_factors
            
import sys
if __name__ == "__main__":
    if len(sys.argv) > 1:
        argument = int(sys.argv[1])
        print(f"the prime factors for {argument} are:", find_prime_factors(argument))
    else:
        print("No argument was provided at the end of the python CMD after filename")

### TIME THE EXECUTION ###
# import time
# start_time = time.perf_counter_ns()
# print(find_prime_factors(27148824)) # [2, 3, 37, 43, 79] # 228.04621 ms
# # print time elapsed
# elapsed_ms = (time.perf_counter_ns() - start_time) / 1e6
# print(f"Execution time: {elapsed_ms:.5f} ms")
