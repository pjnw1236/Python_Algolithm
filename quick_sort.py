# 퀵 정렬

####################################################################################################

# 방법 1

def quick_sort(array):
    n = len(array) 
    if n <= 1:
        return array 
    pivot = array[0] 
    g1 = []
    g2 = []
    for i in range(1, n): 
        if array[i] < pivot: 
            g1.append(array[i]) 
        else:
            g2.append(array[i]) 
    return quick_sort(g1) + [pivot] + quick_sort(g2)

# 사례로 확인
d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
print(quick_sort(d)) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
