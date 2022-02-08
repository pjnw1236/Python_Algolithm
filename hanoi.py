# 하노이의 탑 알고리즘

# n : 옮기려는 원반의 개수 (하노이의 탑)
# start_pos : 옮길 원반이 현재 있는 출발점 기둥
# end_pos : 원반을 옮길 도착점 기둥
# middle_pos : 옮기는 과정에서 사용할 보조 (중간) 기둥

# start_pos에 있는 n개의 원반을 end_pos로 이동시키는 과정

def hanoi(n, start_pos, end_pos, middle_pos):
    if n == 1:
        print(start_pos, "->", end_pos)
        return 
    
    hanoi(n-1, start_pos, middle_pos, end_pos) 
    print(start_pos, "->", end_pos) 
    hanoi(n-1, middle_pos, end_pos, start_pos) 

##################################################
print("n=1")
hanoi(1, 1, 3, 2)

# 출력
# n=1
# 1 -> 3

##################################################
print("n=2")
hanoi(2, 1, 3, 2)

# 출력
# n=2
# 1 -> 2
# 1 -> 3
# 2 -> 3

##################################################
print("n=3")
hanoi(3, 1, 3, 2)

# 출력
# n=3
# 1 -> 3
# 1 -> 2
# 3 -> 2
# 1 -> 3
# 2 -> 1
# 2 -> 3
# 1 -> 3
