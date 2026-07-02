# Number Spiral Diagonals
# Problem 28
# Starting with the number 1 and moving to the right in a clockwise direction
# a 5 by 5 spiral is formed as follows:
# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13
# It can be verified that the sum of the numbers on the diagonals is 101.
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral
# formed in the same way?

def brute_spiral_diagonal_sums(side_length: int) -> int:
    # edge cases:
    if (side_length % 2 == 0 or side_length < 1):
        return -1 # not a valid spiral square
    if (side_length == 1):
        return 1
    sum = 1 # center number
    for n in range(side_length, 1, -2):
        sum += (n**2 * 4) - ((n - 1) * 6)
    return sum

# print("0 x 0 diagonal sum =", brute_spiral_diagonal_sums(0)) # -1
# print("1 x 1 diagonal sum =", brute_spiral_diagonal_sums(1)) # 1
# print("3 x 3 diagonal sum =", brute_spiral_diagonal_sums(3)) # 25
# print("5 x 5 diagonal sum =", brute_spiral_diagonal_sums(5)) # 101
# print("7 x 7 diagonal sum =", brute_spiral_diagonal_sums(7)) # 261
# print("9 x 9 diagonal sum =", brute_spiral_diagonal_sums(9)) # 537
# print("11 x 11 diagonal sum =", brute_spiral_diagonal_sums(11)) # 961
# print("1001 x 1001 diagonal sum =", brute_spiral_diagonal_sums(1001)) # 669171001