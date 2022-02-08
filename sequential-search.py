###############################
## 모두의 알고리즘 with 파이썬 ##
###############################

# 순차 탐색

# array : 리스트
# value : 찾는 값

# array에서 value 값이 존재하면, 해당 value 값이 속해 있는 array의 index 반환/ 값이 존재하지 않다면 -1 반환

def search_list(array, value):
    n = len(array) 
    for i in range(n):
        if value == array[i]:
            return i
    return -1 


# 다음 예시로 확인
v = [17, 92, 18, 33, 58, 7, 33, 42]

print(search_list(v, 18))  # 2
print(search_list(v, 33))  # 3
print(search_list(v, 900)) # -1
