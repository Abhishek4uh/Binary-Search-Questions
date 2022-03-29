# Find an index of smallest element in the sorted rotated array!

N = 10
Arr=[8,9,10,11,1,2,3,4,5,6]

def rotation(n,Arr):
    start=0
    end=n-1
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

print(rotation(N,Arr))
# output will->>> 4
# explanation: beacuse index of 1 is 4
