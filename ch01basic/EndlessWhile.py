import random

answer = random.randint(1, 100)

print('정답 : %d' % answer)

counter = 0 # 카운터 변수

while True:
    su = int(input('1~100사이의 정수 입력 : '))

    counter += 1

    if su>answer:
        print('야!!!!!!!!!! %d 보다 더 작은 숫자야!!!!!!' %su)
    elif su<answer:
        print('야!!!!!!!!!! %d 보다 더 큰 숫자야!!!!!!' %su)
    else:
        print('정답이야!!!!!!!!!!!!!!!')
        break
    # end if
# end while

print('%d번만에 맞추었습니다.' %counter)

