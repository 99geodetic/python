# 숫자를 입력받아 별 삼각형 출력
n = int(input("숫자를 입력하세요 : "))  # 사용자로부터 숫자 입력 받기

for i in range(1, n + 1):  # 1부터 n까지 반복
    for j in range(i):  # i번 반복하여 별 출력
        print("*", end="")  # 줄 바꿈 없이 별 출력
    print()  # 줄 바꿈
