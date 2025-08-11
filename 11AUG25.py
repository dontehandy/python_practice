# 1. Additive Persistence
def additive_persistence(num):
    """
    Returns the number of times you must sum the digits of num
    until you reach a single digit.
    Example: 1679583 -> 1+6+7+9+5+8+3 = 39 -> 3+9 = 12 -> 1+2 = 3 -> output 3
    """
    the_list = []
    to_add = []
    for i in str(num):
        the_list.append(i)
    for n in the_list:
        to_add.append(int(n))
    return sum(to_add)
    
        
    

print("Testing additive_persistence...")
print(additive_persistence(1679583))  # Expected: 3
print(additive_persistence(1234))     # Expected: 2
print(additive_persistence(9))        # Expected: 0
print()


# # 2. Digital Root
# def digital_root(num):
#     """
#     Returns the digital root of num.
#     The digital root is the final single-digit value obtained by summing
#     the digits repeatedly.
#     Example: 942 -> 9+4+2 = 15 -> 1+5 = 6
#     """
#     pass


# # 3. Factorial Digit Sum
# def factorial_digit_sum(num):
#     """
#     Returns the sum of the factorial of each digit in num.
#     Example: 145 -> 1! + 4! + 5! = 1 + 24 + 120 = 145
#     """
#     pass


# -----------------
# TEST CASES
# -----------------



# print("Testing digital_root...")
# print(digital_root(942))               # Expected: 6
# print(digital_root(132189))            # Expected: 6
# print(digital_root(493193))            # Expected: 2
# print()

# print("Testing factorial_digit_sum...")
# print(factorial_digit_sum(145))        # Expected: 145
# print(factorial_digit_sum(123))        # Expected: 9  (1! + 2! + 3! = 1 + 2 + 6)
# print(factorial_digit_sum(40585))      # Expected: 40585
