# Binary search on sorted array but what if orden is not given.....

def Binary_Search_Unknown(arr,target):
    start=0
    end=len(arr)-1
    if arr[0]>arr[1]:
        while(start<=end):
            mid=start+(end-start)//2
            if arr[mid]==target:
                return mid
            if target<arr[mid]:
                start=mid+1
            else:
                end=mid-1
    else:
        while(start<=end):
            mid=start+(end-start)//2
            if arr[mid]==target:
                return mid
            if target>arr[mid]:
                start=mid+1
            else:
                end=mid-1
        
    return -1
arr=[1000,300,299,45,40,8,6,7]
target=40
print(Binary_Search_Unknown(arr,target))

# output->>>> 4
