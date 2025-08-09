# 2. Trend Switch Counter
def count_trend_switches(arr):
    """
    Counts how many times the array's trend switches
    from increasing to decreasing or vice versa.
    """
    counter = 0
    prev_trend = None
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            cur_trend = "up"
        elif arr[i] < arr[i-1]:
            cur_trend = "down"
        if prev_trend and cur_trend != prev_trend:
            counter += 1
        prev_trend = cur_trend
    return counter

print("Testing count_trend_switches...")
print(count_trend_switches([1, 3, 5, 4, 2, 6, 8, 5]))  # Expected: 3
print(count_trend_switches([5, 4, 3, 2]))              # Expected: 0
print(count_trend_switches([1, 2, 1, 2, 1]))           # Expected: 3
print()


# # 3. First Valley Finder
# def find_valley(arr):
#     """
#     Returns the index of the first valley in the array.
#     A valley is an element smaller than both neighbors.
#     Returns -1 if no valley is found.
#     """
#     pass


# print("Testing find_valley...")
# print(find_valley([5, 3, 4, 2, 6]))  # Expected: 1
# print(find_valley([1, 2, 3, 4]))     # Expected: -1
# print(find_valley([3, 1, 2]))        # Expected: 1


# ----completed:

# 1. Peak Element Finder
# def find_peak(arr):
#     """
#     Returns the index of the first peak in the array.
#     A peak is an element greater than both neighbors.
#     Returns -1 if no peak is found.
#     """
#     for i in range(len(arr)):
#         if arr[i] > arr[-1] and arr[i] > arr[i+1]:
#             return arr.index(arr[i])
#     return -1
    

# print("Testing find_peak...")
# print(find_peak([1, 3, 5, 4, 2]))  # Expected: 2
# print(find_peak([10, 20, 30, 40])) # Expected: -1
# print(find_peak([1, 2, 3, 2, 1]))  # Expected: 2
# print()
