# 친화수 구하기

# 진약수의 합을 구하는 함수
def divisor_sum(n):
    total = 0  # 합계 초기화
    for i in range(1, n):  # 1부터 n-1까지 반복
        if n % i == 0:  # i가 n의 약수라면
            total += i  # 합에 더함
    return total  # 합 반환

# 1부터 20000까지의 친화수 찾기
for a in range(1, 20001):  # 1부터 20000까지 반복
    b = divisor_sum(a)  # a의 진약수 합 구하기
    if a < b <= 20000 and divisor_sum(b) == a:  # 쌍 조건 확인
        print(a, "의 친화수", b)  # 출력
