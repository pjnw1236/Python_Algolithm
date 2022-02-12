# 선택 정렬

# 방법 1
# array 리스트의 원소들을 result 리스트에 오름차순으로 정렬하여 저장

# array 속한 원소의 가장 작은 값의 인덱스 반환하는 함수
def find_min_idx(array):
    n = len(array) 
    min_idx = 0
    for i in range(n):
        if array[min_idx] > array[i]:
            min_idx = i
    return min_idx 

# 선택 정렬하여 result 리스트에 오름차순으로 저장
def selection_sort(array):
    result = []
    while array:
        min_idx = find_min_idx(array)
        result.append(array.pop(min_idx))
    return result

  
# 다음 예시로 확인
Arr = [4, 1, 3, 2]

print(selection_sort(Arr)) # [1, 2, 3, 4]

####################################################################################################

# 방법 2

# array 리스트의 요소들을 선택 정렬하여 result 리스트에 오름차순으로 저장

def selection_sort(array):
    n = len(array)
    for i in range(n-1): 
        min_idx = i
        for j in range(i+1, n):
            if array[min_idx] > array[j]:
                min_idx = j 
                # i번 인덱스보다 더 작은 수가 있으면 서로 교환
                array[i], array[min_idx] = array[min_idx], array[i]
    return array


# 사례로 확인
Arr = [4,1,3,2]

print(selection_sort(Arr)) # [1, 2, 3, 4]
