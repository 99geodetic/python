# 피보나치 수열을 계산하는 함수
def fibonacci(n):
    if n == 0:  # n이 0일 경우 1을 반환
        return 1
    elif n == 1:  # n이 1일 경우 1을 반환
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)  # 재귀 호출로 피보나치 수 계산

# 15번째까지 피보나치 수 출력
for i in range(16):
    print(f"fibo({i}) = {fibonacci(i)}")
