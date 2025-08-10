# Challenge: LetterTripleCheck
# Write a function called LetterTripleCheck(s) that checks whether any letter
# (a-z, case insensitive) appears exactly **three times in a row** anywhere in the string.
# Return "true" if such a sequence exists, otherwise return "false".
#
# Examples:
# LetterTripleCheck("aaab") => "true"
# LetterTripleCheck("aBBBa") => "true"
# LetterTripleCheck("abc") => "false"
# LetterTripleCheck("boook") => "true"

def LetterTripleCheck(s: str) -> str:
    # Your code here
    pass

# --- Test Cases ---
print(LetterTripleCheck("aaab"))      # true
print(LetterTripleCheck("aBBBa"))     # true
print(LetterTripleCheck("abc"))       # false
print(LetterTripleCheck("boook"))     # true