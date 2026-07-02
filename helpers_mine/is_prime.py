def is_prime(num: int) -> bool: # test if number is prime or composite
    if num <= 1: # any number less than 2 is not prime
        return False
    if num == 2: # 2 is the only even prime
        return True
    if num % 2 == 0: # no other even numbers are prime
        return False
    for i in range(3, int(num**0.5) + 1, 2): # check only odds up to sqrt of num
        if num % i == 0: # once a factor is hit
            return False
    return True # no factors found

import sys
if __name__ == "__main__":
    num = int(sys.argv[1])
    print(f"Is {num} Prime?", is_prime(num))
