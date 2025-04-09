# 암스트롱 수를 구하는 함수
def is_armstrong(num):
    digits = list(map(int, str(num)))  # 숫자의 각 자리를 리스트로 변환
    num_digits = len(digits)  # 자릿수 구하기
    sum_of_powers = sum([digit ** num_digits for digit in digits])  # 각 자리수를 자릿수만큼 거듭제곱하고 더함
    return sum_of_powers == num  # 원래 숫자와 같으면 암스트롱 수

# 3자리 암스트롱 수 출력
for i in range(100, 1000):
    if is_armstrong(i):
        print(i, end=" ")
