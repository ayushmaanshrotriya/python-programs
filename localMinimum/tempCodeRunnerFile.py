def localMinimum(arr):
    start = 0
    end = len(arr)-1
    lc = 0
    while(start<=end):
        mid = start+(end-start)//2
        if mid>0 and mid<len(arr)-1:
            if arr[mid]<=arr[mid+1] and arr[mid]<=arr[mid-1]:
                lc = mid
                break
            elif arr[mid]>arr[mid+1] or arr[mid]>arr[mid-1]:
                if arr[mid]>arr[mid+1]:
                    start = mid+1
                else:
                    end = mid - 1
        else:
            lc = start
            break
    return lc
    

def main():
    arr = [5,4,3,21,1,2,16]
    print(localMinimum(arr))
    return 0
if __name__ == "__main__":
    main()