from is_prime import is_prime

def find_prime_factors(num: int) -> list:
    prime_factors = set()
    if num <= 1: # edge 1: n is too small to be a prime
        print(f"num of {num} too small to be a prime")
        return prime_factors
    if is_prime(num): # edge 2: n already is prime
        prime_factors.add(num)
        return prime_factors
    quotient = num # start value at num
    i = 2
    while True:
        if not quotient % i == 0: # i is not a prime factor
            i += (2 if i > 2 else 1) # iterates through odds starting at i == 3
            continue
        while quotient % i == 0: # keep filtering out prime factor i
            prime_factors.add(i)
            quotient = int(quotient / i)
            if quotient == 1:
                return sorted(prime_factors)
        if is_prime(quotient): # factored out quotient result is prime
            prime_factors.add(quotient)
            return sorted(prime_factors)
        i += (2 if i > 2 else 1) # iterates through odds starting at i == 3

import sys
if __name__ == "__main__":
    num = int(sys.argv[1])
    print(f"for num = {num} the prime factors are:", find_prime_factors(num))
