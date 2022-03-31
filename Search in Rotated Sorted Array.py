# ------Leeetcode----33. Search in Rotated Sorted Array in o(logn)
def BinarySearch(Arr,start,end,target):
    s=start
    e=end
    while(s<=e):
        mid=s+(e-s)//2
        if Arr[mid]==target:
            return mid
        elif target<Arr[mid]:
            e=mid-1
        else:
            s=mid+1
    return -1
def MinumumElement_Index(Arr):
    start=0
    end=len(Arr)-1
    n=len(Arr)
    while start<=end:
        if Arr[start] <= Arr[end]:
            return start
        mid=start+(end-start)//2
        nextt=(mid+1)%n
        prevv=(mid+n-1)%n
        if Arr[mid]<=Arr[nextt] and Arr[mid]<=Arr[prevv]:
            return mid
        elif Arr[start]<= Arr[mid]:
            start=mid+1
        else:
            end=mid-1
            
def main(Arr,target):
    temp=MinumumElement_Index(Arr)
    val1=BinarySearch(Arr,0,temp-1,target)
    val2=BinarySearch(Arr,temp,len(Arr)-1,target)
    if val1!=-1:
        return val1
    return val2
Arr=[8,9,10,11,15,19,1,2,3,4,5,6]
print(main(Arr,1))

# Output->>> 6
