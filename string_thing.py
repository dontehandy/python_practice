# Challenge: MatchDigitDash
# Write a function called MatchDigitDash(s) that checks whether the string contains
# a digit (0-9) followed by **exactly two characters**, and then a dash ('-').
# Return "true" if such a pattern is found at least once, otherwise return "false".
#
# Examples:
# MatchDigitDash("3ab-") => "true"
# MatchDigitDash("hello 2xy-") => "true"
# MatchDigitDash("9abcd-") => "false"
# MatchDigitDash("no match here") => "false"

def MatchDigitDash(s: str) -> str:
    for i in range(len(s)):
        if s[i].isnumeric() and s[i+1].isalpha() and s[i+2].isalpha() and s[i+3] == "-":
            return True
    return False









# --- Test Cases ---
print(MatchDigitDash("3ab-"))         # true
print(MatchDigitDash("hello 2xy-"))   # true
print(MatchDigitDash("9abcd-"))       # false
print(MatchDigitDash("no match here"))# false
