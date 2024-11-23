
def primeFinder(n):
    if n<=1:
        return  False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def isEven(n):
    if n%2==0:
        return True
    else:
        return  False

def removeDuplicate(nums):
    nums=set(nums)
    nums=list(nums)
    return nums

def maxFinder(nums):
    m=nums[0]
    for n in nums:
        if m<n:
            m=n
    return m