humanDict = {
    'age': 24, 'name': '박상빈', 'hobby': '독서', 'telephone': '010-5570-0010',
    'address': {'city': '평양', 'gu': '평천구', 'zipcode': '02, 0195'}
}
print(type(humanDict))
print(humanDict)

import json
humanString = json.dumps(humanDict, ensure_ascii=False, indent=4, sort_keys=True)
# dumps 사전을 문자열로 변환
print(type(humanString))
print(humanString)

humanJson = json.loads(humanString)
print('이름 : %s' % humanJson['name'])
print('취미 : %s' % humanJson['hobby'])
print('나이 : %s' % humanJson['age'])
print('연락처 : %s' % humanJson['telephone'])
print('시도 : %s' % humanJson['address']['city'])
print('군구 : %s' % humanJson['address']['gu'])
print('우편번호 : %s' % humanJson['address']['zipcode'])

