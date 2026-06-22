# Multiples of 3 or 5
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
# Assumption: list of numbers AND limit are natural
# Reminder: natural numbers are positive whole numbers starting at 1 (1,2,3...)
# Answer:  233168


def brute_sum_mult(limit, *natnums):
    multiples = set()
    # edge case 1
    if limit == 0:
        return 0
    for n in natnums:
        for i in range(1, limit):
            if i % n == 0:
                multiples.add(i)
    return sum(multiples)


def dynamic_if_sum_mult(limit, *natnums): # 3 times LONGER than brute_sum_multi() for few natnums, but better than brute_sum_multi() after 18 natnums
    # edge case 1: limit is 0
    if limit == 0:
        return 0
    multiples = set()
    for i in range(1, limit):
        if any(i % n == 0 for n in natnums):
            multiples.add(i)
    return sum(multiples)


def eval_cond_sum_mult(limit:int, *natnums:int) -> int: # rediculously long time to run!!!
    # edge case 1: limit is 0
    if limit == 0:
        return 0
    multiples = set()
    conditional = ''
    for n in natnums:
        conditional += f'i % {n} == 0 or '
    conditional = conditional[:-4] # strip last ' or '
    for i in range(1, limit):
        if (eval(conditional)):
            multiples.add(i)
    return sum(multiples)


# 1/4 the time of brute_sum_multi(); factor even gets more pronounced as len of natnums increases
def n_iter_sum_mult(limit:int, *natnums:int) -> int:
    # edge case 1: limit is 0
    if limit == 0:
        return 0
    multiples = set()
    for n in natnums:
        for i in range(n, limit, n):
            multiples.add(i)
    return sum(multiples)


# WINNER WINNER CHICKEN DINNER!!
# fastest of all, edges out n_iter_sum_mult by closing in the limit
def manage_lim_sum_mult(limit:int, *natnums:int) -> int:
    # edge case 1: limit is 0
    if limit == 0:
        return 0
    multiples = set()
    for n in natnums:
        for i in range(n, (((limit // n) * n) + (1 if limit % n != 0 else 0)), n):
            multiples.add(i)
    return sum(multiples)







### TIME THE EXECUTION ###
import time

# PRETRIAL
start_time = time.perf_counter_ns()
print(brute_sum_mult(1000, 3, 5)) # 233168
# print time elapsed
elapsed_ms = (time.perf_counter_ns() - start_time) / 1e6
print(f"Execution time for PRETRIAL: {elapsed_ms:.5f} ms")


# TRIAL 1
start_time = time.perf_counter_ns()

# run the function 
# print(brute_sum_mult(20000000, 3, 5))
# print(brute_sum_mult(20000000, 3, 5, 10, 11, 42, 10234, 125, 68, 69))
# print(brute_sum_mult(20000000, 3, 5, 10, 11, 42, 10234, 125, 68, 69, 4, 6, 12, 13, 43, 10235, 126, 70, 71))
print(brute_sum_mult(1000, 3, 5)) # 233168
# print(brute_sum_mult(1000, 3000, 5))
# print(brute_sum_mult(1000, 3000, 5000))

# print time elapsed
elapsed_ms = (time.perf_counter_ns() - start_time) / 1e6
print(f"Execution time for TRIAL 1: {elapsed_ms:.5f} ms")

# TRIAL 2
start_time = time.perf_counter_ns()

# run the function
# print(dynamic_if_sum_mult(20000000, 3, 5))
# print(dynamic_if_sum_mult(20000000, 3, 5, 10, 11, 42, 10234, 125, 68, 69))
# print(dynamic_if_sum_mult(20000000, 3, 5, 10, 11, 42, 10234, 125, 68, 69, 4, 6, 12, 13, 43, 10235, 126, 70, 71))
print(dynamic_if_sum_mult(1000, 3, 5)) # 233168
# print(dynamic_if_sum_mult(1000, 3000, 5))
# print(dynamic_if_sum_mult(1000, 3000, 5000))

# print time elapsed
elapsed_ms = (time.perf_counter_ns() - start_time) / 1e6
print(f"Execution time for TRIAL 2: {elapsed_ms:.5f} ms")

# TRIAL 3
start_time = time.perf_counter_ns()

# run the function
# print(eval_cond_sum_mult(20000000, 3, 5))
# print(eval_cond_sum_mult(20000000, 3, 5, 10, 11, 42, 10234, 125, 68, 69))
# print(eval_cond_sum_mult(20000000, 3, 5, 10, 11, 42, 10234, 125, 68, 69, 4, 6, 12, 13, 43, 10235, 126, 70, 71))
print(eval_cond_sum_mult(1000, 3, 5)) # 233168
# print(eval_cond_sum_mult(1000, 3000, 5))
# print(eval_cond_sum_mult(1000, 5))
# print(eval_cond_sum_mult(1000, 3000, 5000))

# print time elapsed
elapsed_ms = (time.perf_counter_ns() - start_time) / 1e6
print(f"Execution time for TRIAL 3: {elapsed_ms:.5f} ms")

# TRIAL 4
start_time = time.perf_counter_ns()

# run the function
# print(n_iter_sum_mult(20000000, 3, 5))
# print(n_iter_sum_mult(20000000, 3, 5, 10, 11, 42, 10234, 125, 68, 69))
# print(n_iter_sum_mult(20000000, 3, 5, 10, 11, 42, 10234, 125, 68, 69, 4, 6, 12, 13, 43, 10235, 126, 70, 71))
print(n_iter_sum_mult(1000, 3, 5)) # 233168
# print(n_iter_sum_mult(1000, 3))
# print(n_iter_sum_mult(1000, 5))
# print(n_iter_sum_mult(1000, 3000, 5))
# print(n_iter_sum_mult(1000, 3000, 5000))

# print time elapsed
elapsed_ms = (time.perf_counter_ns() - start_time) / 1e6
print(f"Execution time for TRIAL 4: {elapsed_ms:.5f} ms")

# TRIAL 5
start_time = time.perf_counter_ns()

# run the function
# print(manage_lim_sum_mult(20000000, 3, 5))
# print(manage_lim_sum_mult(20000000, 3, 5, 10, 11, 42, 10234, 125, 68, 69))
# print(manage_lim_sum_mult(20000000, 3, 5, 10, 11, 42, 10234, 125, 68, 69, 4, 6, 12, 13, 43, 10235, 126, 70, 71))
print(manage_lim_sum_mult(1000, 3, 5)) # 233168
# print(manage_lim_sum_mult(1000, 3))
# print(manage_lim_sum_mult(1000, 5))
# print(manage_lim_sum_mult(1000, 3000, 5))
# print(manage_lim_sum_mult(1000, 3000, 5000))

# print time elapsed
elapsed_ms = (time.perf_counter_ns() - start_time) / 1e6
print(f"Execution time for TRIAL 5: {elapsed_ms:.5f} ms")