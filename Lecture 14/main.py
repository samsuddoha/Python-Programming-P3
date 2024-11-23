import myModule as mm

numbers=list(map(int,input("Enter numbers").split()))
withoutDuplicate=mm.removeDuplicate(numbers)
primeSum=0
evnSum=0
for n in withoutDuplicate:
    if mm.primeFinder(n):
        primeSum+=n
    if mm.isEven(n):
        evnSum+=n
maxNum=mm.maxFinder([primeSum,evnSum])

print(numbers)
print(withoutDuplicate)
print(primeSum)
print(evnSum)
print(maxNum)

