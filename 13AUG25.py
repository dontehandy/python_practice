# 1. Even-Digit Multiplicative Persistence
def even_digit_multiplicative_persistence(num):
    """
    Similar to multiplicative persistence, but only multiply the EVEN digits
    of the number at each step. Ignore odd digits (treat as multiplication by 1).
    Continue until you reach a single digit.
    If there are no even digits in a step, treat result as the same number.
    Return the number of steps required.
    Example: 482 -> 4*8*2=64 -> 6*4=24 -> 2*4=8 -> steps=3
    """
    pass


# 2. Multiplicative Persistence with Step Values
def multiplicative_persistence_steps(num):
    """
    Returns a list of each intermediate value when calculating
    the multiplicative persistence of num.
    Example: 39 -> [27, 14, 4]
    """
    pass


# -----------------
# TEST CASES
# -----------------

print("Testing even_digit_multiplicative_persistence...")
print(even_digit_multiplicative_persistence(482))   # Expected: 3
print(even_digit_multiplicative_persistence(86))    # Expected: 2  (8*6=48 -> 4*8=32 -> 3*2=6)
print(even_digit_multiplicative_persistence(135))   # Expected: 0  (no even digits from the start)
print()

print("Testing multiplicative_persistence_steps...")
print(multiplicative_persistence_steps(39))         # Expected: [27, 14, 4]
print(multiplicative_persistence_steps(77))         # Expected: [49, 36, 18, 8]
print(multiplicative_persistence_steps(4))          # Expected: []
