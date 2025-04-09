# 'Bython'을 'Python'으로 변경하는 함수
def replace_bython_with_python(text):
    return text.replace('Bython', 'Python')  # 'Bython'을 'Python'으로 교체

# 테스트
text = "Park(Java city), Kim(C city), Kang(Bython city), Lee(Bython city), Hong(Ruby city), Cho(Bython city), Koo(C city), Ryu(C++ city)"
modified_text = replace_bython_with_python(text)
print(modified_text)
