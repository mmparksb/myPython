print('이름 입력 : ', end='')  # 자바의 프린트ln와 동일!!  end 기본값 엔터!!!
name = input()

# input 함수는 반환 타입이 문자열 입니다.
age = int(input('나이 입력 : '))  # int 로 형변환
height = float(input('키 입력 : ')) # float 으로 형변환

print('% 포맷 코드로 출력')
print('이름 : %s' % name)
print('나이 : %d' % age)
print('키 : %.2f\n' % height)

print('문자열 함수 format() 사용')
message = '제 이름은 {}이고, 나이는 {}세 입니다. \n제 키는 {}cm 입니다.'
print(message.format(name, age, height))
