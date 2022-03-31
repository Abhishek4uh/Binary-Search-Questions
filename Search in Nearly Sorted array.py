#Searching in "Nearly sorted array"
#Nearly sorted means ith element can be present at (i+1)th or (i-1)th place
def binary_search(target):
    low=0
    high=len(arr) - 1
    n=len(arr)
    while low <= high : 

        mid = low + (high - low)//2

        if arr[mid]==target:
            return mid

        previous = (mid-1)%n
        next=(mid+1)%n

        if arr[previous]==target:
            return previous

        if arr[next]==target:
            return next

        if target<arr[mid]:
            high=mid-2
        else:
            low=mid+2
    return -1

arr=[10, 3, 40, 20, 50, 80, 70]
ans=binary_search(70)
print(ans)

# output--->> 6
