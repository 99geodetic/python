# 주민등록번호로 생년월일 처리 함수
def convert_birthdate(id_number):
    year = int(id_number[:2])  # 주민등록번호의 앞 2자리로 연도 추출
    month = int(id_number[2:4])  # 주민등록번호의 3~4자리로 월 추출
    day = int(id_number[4:6])  # 주민등록번호의 5~6자리로 일 추출

    if int(id_number[6]) >= 5:  # 주민등록번호 7번째 자리로 성별 판단
        year += 1900  # 5 이상이면 1900년대
    else:
        year += 2000  # 5 미만이면 2000년대

    return f"{year}년 {month}월 {day}일"

# 테스트
print(convert_birthdate("921030"))  # 1992년 10월 30일
print(convert_birthdate("511010"))  # 1951년 10월 10일
