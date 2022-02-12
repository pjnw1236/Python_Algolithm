def binary_search(array, target):
    start = 0
    end = len(array)-1 

    while start <= end:
        mid = (start+end)//2 
        if target == array[mid]:
            return mid
        elif target > array[mid]: 
            start = mid+1 
        else:
            end = mid-1 
    return -1 

d = [1, 4, 9, 16, 25, 36, 49, 64, 81]
print(binary_search(d, 36)) # 5
print(binary_search(d, 50)) # -1
