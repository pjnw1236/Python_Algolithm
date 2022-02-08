###############################
## 모두의 알고리즘 with 파이썬 ##
###############################

# 순차 탐색

# array : 리스트
# value : 찾는 값

# array에서 value 값이 존재하면, 해당 value 값이 속해 있는 array의 index 반환/ 값이 존재하지 않다면 -1 반환

def search_value(array, value):
    n = len(array) 
    for i in range(n):
        if value == array[i]:
            return i
    return None 


# 다음 예시로 확인
v = [1, 3, 5, 7, 9]

print(search_value(v, 5)) # 2
print(search_value(v, 7)) # 3
print(search_value(v, 2)) # None
