def mergesort(arr):
    ### code that splits the array until it is in individual arrays
    if len(arr) <=1:
        return arr
    
    midpoint = len(arr)//2
    leftArray = arr[:midpoint]
    rightArray = arr[midpoint:]

    leftSorted = mergesort(leftArray)
    rightSorted = mergesort(rightArray)

    ###code that puts the array back together

    return merge(leftSorted, rightSorted)

def merge(arr1,arr2):

    merged = []
    i = 0
    q = 0

    while (i<len(arr1) and q<len(arr2)):
        if arr1[i] <= arr2[q]:
            merged.append(arr1[i])
            i+=1
        else:
            merged.append(arr2[q])
            q +=1

    while i <len(arr1):
        merged.append(arr1[i])
        i+=1
        
    while q<len(arr2):
        merged.append(arr2[q])
        q+=1

    return merged

numInts = int(input("please enter the number of inputs: "))
nums = []
x = 0
while x < numInts:
    print(f"Nums total {x}")
    numToAdd = int(input("Add number: "))
    nums.append(numToAdd)    
    x += 1

print(f"\n\nNums total {x}")
for num in mergesort(nums):
    print(num)