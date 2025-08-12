# # 1. Additive Persistence
# def additive_persistence(num):
#     """
#     Returns the number of times you must sum the digits of num
#     until you reach a single digit.
#     Example: 1679583 -> 1+6+7+9+5+8+3 = 39 -> 3+9 = 12 -> 1+2 = 3 -> output 3
#     """
#     counter = 0
#     while num > 9:
#         numbers = []
#         for i in str(num):
#             numbers.append(int(i))
#         total = 0
#         for n in numbers:
#             total += n
#         num = total
#         counter += 1
#     return counter
  
# print("Testing additive_persistence...")
# print(additive_persistence(1679583))  # Expected: 3
# print(additive_persistence(1234))     # Expected: 2
# print(additive_persistence(9))        # Expected: 0
# print()


# # 2. Digital Root
# def digital_root(num):
#     """
#     Returns the digital root of num.
#     The digital root is the final single-digit value obtained by summing
#     the digits repeatedly.
#     Example: 942 -> 9+4+2 = 15 -> 1+5 = 6
#     """
#     while num >= 10:
#         numbers = []
#         for i in str(num):
#             numbers.append(int(i))
#         total = 0
#         for n in numbers:
#             total += n
#         num = total
#     return num
        

# print("Testing digital_root...")
# print(digital_root(942))               # Expected: 6
# print(digital_root(132189))            # Expected: 6
# print(digital_root(493193))            # Expected: 2
# print()


# 3. Factorial Digit Sum

def factorial_digit_sum(num):
    
    numbers = [] #establish a list called numbers
    for i in str(num): #for every iterable in the casted sting of num
        numbers.append(int(i)) #append it to the numbers list
    count = 0 #set a count init with 0
    for n in numbers: #for every number in numbers
        fact = 1 # variable for factorial. start with 1
        x = n # var x and sets it to the current iterable in numbers (n)
        while x > 1: #while the number is greater than 1
            fact *=x #multiplies current value of fact by x and stores the result
            x -= 1 #x is now - 1 ans stored as the value of the var
        count +=fact #add the result of fact to the count and repeat until at 1
    return count #return the count 


print("Testing factorial_digit_sum...")
print(factorial_digit_sum(145))        # Expected: 145
print(factorial_digit_sum(123))        # Expected: 9  (1! + 2! + 3! = 1 + 2 + 6)
print(factorial_digit_sum(40585))      # Expected: 40585