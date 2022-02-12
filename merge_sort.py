# 병합 정렬

####################################################################################################
# 방법 1
def merge_sort(Arr): 
    n = len(Arr) 
    if n <= 1:
        return Arr 
    # 절반 나누어 재귀적으로 수행
    mid = n//2 
    g1 = merge_sort(Arr[:mid]) 
    g2 = merge_sort(Arr[mid:]) 

    result = []
    # g1의 원소와 g2의 원소 중 더 작은 원소 result 리스트에 삽입
    while g1 and g2:
        if g1[0] < g2[0]: 
            result.append(g1.pop(0))
        else:
            result.append(g2.pop(0)) 
    while g1:
        result.append(g1.pop(0))
    while g2:
        result.append(g2.pop(0)) 
    return result 

d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
print(merge_sort(d)) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 과정 
# g1 = [6, 8, 3, 9, 10] -----> [3, 6, 8, 9 ,10]
# g2 = [1, 2, 4, 7, 5] -----> [1, 2, 4, 5, 7] 

# g1 = [8, 9, 10] // g2 = []
# result = [1, 2, 3, 4, 5, 6, 7]

# g1 = [] // g2 = []
# result = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

####################################################################################################

# 방법 2 

# 일반적인 방법

def merge_sort(Arr):
    n = len(Arr) 
    if n <= 1:
        return Arr 
    mid = n//2 
    g1 = Arr[:mid] 
    g2 = Arr[mid:] 
    merge_sort(g1) 
    merge_sort(g2) 

    i1 = 0
    i2 = 0
    ia = 0

    while i1 < len(g1) and i2 < len(g2): 
        if g1[i1] < g2[i2]:
            Arr[ia]=g1[i1] 
            i1 += 1
            ia += 1
        else:
            Arr[ia] = g2[i2]
            i2 += 1
            ia += 1
        
    while i1 < len(g1):
        Arr[ia] = g1[i1] 
        i1 += 1
        ia += 1
    while i2 < len(g2): 
        Arr[ia] = g2[i2]
        i2 += 1
        ia += 1
    
    return Arr
    
d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
print(merge_sort(d)) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
