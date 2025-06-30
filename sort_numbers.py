'''
Finish the solution so that it sorts the passed in array of numbers. If the function passes in an empty array or null/nil value then it should return an empty array.

'''

def solution(nums):             
    if not nums:                 # If nums is None or empty #In python, not nums will be True if nums is considered falsy
        return []                
    return sorted(nums)          

print(solution([11,33,24]))       


def solutionTWO(nums):
    if nums:
        return sorted(nums)
    else:
        return []
    
print(solutionTWO([11,33,24]))
