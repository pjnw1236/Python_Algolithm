# 삽입 정렬

####################################################################################################
# 방법 1 

# 오름차순으로 정렬되어 있는 Arr 리스트에 val 값이 삽입될 경우 몇번째 인덱스에 삽입되어야할지 반환하는 함수 find_idx
def find_idx(Arr, val):
    n = len(Arr) 
    for i in range(n): 
        if Arr[i] > val: 
            return i 
    # Arr[n-1] < val일 경우 Arr 리스트 가장 뒤에 삽입해야 하므로 n 반환
    return n 

# array 리스트에에서 원소를 하나씩 pop하여 result 리스트에 오름차순으로 정렬 (위의 함수 이용)
def ins_sort(array):
    result = []
    while array:
        # array 리스트에서 원소를 하나씩 pop
        value = array.pop()
        # result에 삽입해야할 index 값 확인
        ins_idx = find_idx(result, value) 
        # result 리스트에 해당 index에 값 삽입
        result.insert(ins_idx, value) 
    return result 

d = [2, 4, 5, 1, 3]
print(ins_sort(d)) # [1, 2, 3, 4, 5]

####################################################################################################
# 방법 2 (일반적인 삽입 정렬 알고리즘) 

# Arr의 리스트에 있는 원소들을 삽입 정렬 이용하여 오름차순으로 정렬

def insertion_sort(Arr): 
    n = len(Arr) 
    for i in range(1, n):
        # Arr[1] ~ Arr[n-1]까지를 key 값으로 설정하여 while문 수행
        key = Arr[i] 
        j = i - 1
        # Arr[j] < Arr[i]인 j 값 찾을 때까지 수행 j = i-1, i-2 ... 0
        while j >= 0 and Arr[j] > key: 
            Arr[j+1] = Arr[j] 
            j -= 1
        Arr[j+1] = key 
    return Arr

d = [2, 4, 5, 1, 3]
print(insertion_sort(d)) # [1, 2, 3, 4, 5]
        Arr[j+1] = key 
    return Arr
    
d = [2, 4, 5, 1, 3]
print(insertion_sort(d))

