# # 1. Even-Digit Multiplicative Persistence
# def even_digit_multiplicative_persistence(num):
#     """
#     Similar to multiplicative persistence, but only multiply the EVEN digits
#     of the number at each step. Ignore odd digits (treat as multiplication by 1).
#     Continue until you reach a single digit.
#     If there are no even digits in a step, treat result as the same number.
#     Return the number of steps required.
#     Example: 482 -> 4*8*2=64 -> 6*4=24 -> 2*4=8 -> steps=3
#     """

#     steps = 0

#     while num > 9:
#         numbers = []
#         for i in str(num):
#             digit = int(i)
#             if digit % 2 == 0:
#                 numbers.append(digit)

#         if numbers == []:
#                 return 0
            
#         mult = 1

#         for n in numbers:
#             mult *= n

#         num = mult
#         steps +=1
#     return steps


# print("Testing even_digit_multiplicative_persistence...")

# # Test 1: 482
# # Step 1: 4*8*2 = 64
# # Step 2: 6*4 = 24
# # Step 3: 2*4 = 8 (single digit, stop)
# print(even_digit_multiplicative_persistence(482))   # Expected: 3

# # Test 2: 86
# # Step 1: 8*6 = 48
# # Step 2: 4*8 = 32
# # Step 3: 3 ignored, 2 = 2 (single digit, stop)
# print(even_digit_multiplicative_persistence(86))    # Expected: 3

# # Test 3: 135
# # Step 1: No even digits, stop immediately
# print(even_digit_multiplicative_persistence(135))   # Expected: 0





# 2. Multiplicative Persistence with Step Values
def multiplicative_persistence_steps(num):
    """
    Returns a list of each intermediate value when calculating
    the multiplicative persistence of num.
    Example: 39 -> [27, 14, 4]
    """
    pass


print("Testing multiplicative_persistence_steps...")
print(multiplicative_persistence_steps(39))         # Expected: [27, 14, 4]
print(multiplicative_persistence_steps(77))         # Expected: [49, 36, 18, 8]
print(multiplicative_persistence_steps(4))          # Expected: []

