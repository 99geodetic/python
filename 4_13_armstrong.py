# 세 자리 암스트롱 수 출력
for num in range(100, 1000):  # 100부터 999까지 반복
    a = num // 100  # 백의 자리
    b = (num // 10) % 10  # 십의 자리
    c = num % 10  # 일의 자리
    if a**3 + b**3 + c**3 == num:  # 세 자리 수의 세제곱 합이 자기 자신과 같다면
        print(num, end=" ")  # 출력
