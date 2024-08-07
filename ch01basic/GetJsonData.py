filename = 'jumsu.json'

# 'rt'는 텍스트 모드로 읽어 들이겠습니다.
myfile = open(filename, mode='rt', encoding='UTF-8')
mystring = myfile.read()
print(type(mystring))

import json

jsonData = json.loads(mystring)
print(type(jsonData))

humanList = list() # 전체 결과를 저장할 리스트

for human in jsonData:
    name = human['name']
    print('이름 : %s' % name)

    kor = float(human['kor'])
    eng = float(human['eng'])
    math = float(human['math'])

    total = kor + eng + math

    _gender = human['gender'].upper() ## 대문자로 바꿔줘 upper() 함수 <ㅡ>lower()
    if _gender == 'M':
        gender = '남자'
    else:
        gender = '여자'

    if 'hello' in human.keys():
        message = human['hello']
        print('메시지 : %s' % (message))
    else:
        message = '없음'
    # end if

    mytuple = (name, kor, eng, math, total, gender, message)
    humanList.append(mytuple)
# end for

print(humanList)