# 선택 정렬

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
