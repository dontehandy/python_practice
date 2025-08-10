import time
import unittest

# --- String Challenge ---
def StringChallenge(s):
    """
    Return 'true' if the string contains 'x' and 'y' with exactly two characters in between them,
    in either order. Otherwise return 'false'.
    Example: 'x__y' or 'y__x' with any two characters as underscores.
    """
    for i in s:
        if i == "x" or i == "y":
            return s.index(i)
                


        



# --- Array Challenge ---
def ArrayChallenge(arr):
    """
    Given an array, return the first index where the array elements stop being strictly increasing
    or stop being strictly decreasing.
    If the array never changes direction, return -1.
    """
    pass


# --- Math Challenge ---
def MathChallenge(num):
    """
    Return the additive persistence of a number:
    how many times you sum the digits of the number until you get a single digit.
    """
    pass


# --- Unit Tests ---
class TestChallenges(unittest.TestCase):

    def test_string_challenge(self):
        self.assertEqual(StringChallenge("taxylophone"), "false")  # x and y with 2 chars between: a,l
        # self.assertEqual(StringChallenge("happy boy"), "true")   # y and x not in this case, so false
        # self.assertEqual(StringChallenge("yellow"), "false")

    # def test_array_challenge(self):
    #     self.assertEqual(ArrayChallenge([1, 2, 5, 7, 6, 4, 3]), 3)  # stops increasing at index 3
    #     self.assertEqual(ArrayChallenge([9, 8, 7, 6, 5]), -1)      # always decreasing
    #     self.assertEqual(ArrayChallenge([1, 2, 3, 4, 5]), -1)      # always increasing

    # def test_math_challenge(self):
    #     self.assertEqual(MathChallenge(9876), 2)  # 9+8+7+6=30, 3+0=3 (two steps)
    #     self.assertEqual(MathChallenge(123), 1)   # 1+2+3=6 (one step)
    #     self.assertEqual(MathChallenge(5), 0)     # already single digit


# --- Time Trial ---
def time_trial():
    start = time.time()
    StringChallenge("taxylophone")
    StringChallenge("happy boy")
    StringChallenge("yellow")

    # ArrayChallenge([1, 2, 5, 7, 6, 4, 3])
    # ArrayChallenge([9, 8, 7, 6, 5])
    # ArrayChallenge([1, 2, 3, 4, 5])

    # MathChallenge(9876)
    # MathChallenge(123)
    # MathChallenge(5)
    end = time.time()
    print(f"Time trial execution time: {end - start:.6f} seconds")


if __name__ == "__main__":
    unittest.main(exit=False)
    time_trial()
