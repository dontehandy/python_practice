# 2. Plateau Peak Finder
def find_plateau_peak(arr):
    """
    Returns the index of the start of the first 'plateau peak'.
    A plateau peak is where one or more equal elements form the top
    of an increasing sequence and are followed by a decrease.
    If no plateau peak exists, return -1.
    Example: In [1, 2, 5, 5, 3], the plateau peak starts at index 2.
    """


    for i in range(len(arr)-1):
        if arr[i] == arr[i+1] and arr[i] == max(arr):
            return i
    return -1


print("Testing find_plateau_peak...")
print(find_plateau_peak([1, 2, 5, 5, 3]))                   # Expected: 2
print(find_plateau_peak([1, 2, 3, 3, 3, 2, 1]))             # Expected: 2
print(find_plateau_peak([1, 2, 3, 4, 5]))                   # Expected: -1
print(find_plateau_peak([5, 5, 4, 3]))                      # Expected: 0


# 3. Longest Zigzag Sequence
def longest_zigzag(arr):
    """
    Returns the length of the longest subsequence where the numbers
    strictly alternate between increasing and decreasing.
    Must be based on consecutive elements.
    If the array length is less than 2, return the length of the array.
    """
    pass


# -----------------
# TEST CASES
# -----------------





# print("Testing longest_zigzag...")
# print(longest_zigzag([1, 3, 2, 4, 3, 5]))                   # Expected: 6 (whole array zigzags)
# print(longest_zigzag([1, 2, 3, 4]))                         # Expected: 2 (only one up or one down allowed)
# print(longest_zigzag([10]))                                 # Expected: 1
# print(longest_zigzag([1, 3, 3, 2, 4]))                      # Expected: 3 (1, 3, 2 or 3, 2, 4)

#    if arr == []:
#         return 0
#     counter = 1
#     length = []
#     for i in range(1, len(arr)):
#         if arr[i] > arr[i-1]:
#             counter +=1
#         elif arr[i] < arr[i-1]:
#             length.append(counter)
#             counter = 1
#     return max(length) if length else 1

#-----completed exercises

# 1. Longest Increasing Streak
# def longest_increasing_streak(arr):
#     """
#     Returns the length of the longest strictly increasing sequence
#     of consecutive elements in the array.
#     If the array is empty, return 0.
#     """

#     if arr == []:
#         return 0
#     counter = 1
#     streak = []
#     for i in range(1, len(arr)):
#         if arr[i] > arr[i-1]:
#             counter +=1
#         else:
#             streak.append(counter)
#             counter = 1
#     return max(streak) if streak else 1

# print("Testing longest_increasing_streak...")
# print(longest_increasing_streak([1, 2, 3, 2, 4, 5, 6, 1]))  # Expected: 4  (2, 4, 5, 6)
# print(longest_increasing_streak([5, 4, 3, 2, 1]))           # Expected: 1  (any single number)
# print(longest_increasing_streak([]))                        # Expected: 0
# print()
