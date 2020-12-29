from random import *
print(int(random()*10))
print(randrange(11,16))
print(randint(11,15))


a = randint(4,28)
print("오프라인 스터디 모임 날짜는 매월 " +str(a)+"일로 설정되었습니다")


sentence="""
예삐는 귀엽고 
보미는 말썽쟁이
"""
print(sentence)

a = "980420-1234567"
print("성별:" +a[7])
print("년도:" +a[:2])
print("월:" +a[2:4])
print("일:" +a[4:6])
print("생년월일:" +a[-7:])
