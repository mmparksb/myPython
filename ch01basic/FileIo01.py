# FileIo01.py
print('파일에 기록합니다.')
myfile01 = open('mem.txt', mode='w', encoding='UTF-8')
print(type(myfile01))

members = ['전두환', '홍준표', '안철수', '박정희']
for human in members:
    message = '\'%s\'님 안녕하세요~\n'%human
    myfile01.write(message)
# end for

myfile01.close()

## UTF-8 방식 권장.........

print('기존 파일에 추가합니다.')

myfile02 = open('mem.txt', mode='a', encoding='UTF-8')

members = ['신아리', '김대중', '하지원']

for idx in range(len(members)):
    message = '%d번째 고객님 : %s님\n'%(idx+1, members[idx])
    myfile02.write(message)
# end for

myfile02.close()

print('with 구문을 사용하면, close() 함수를 사용하지 않아도 됩니다.')
with open('test.txt', mode='w', encoding='UTF-8') as testfile:
    testfile.write("가나다\n")
    testfile.write("abc\n")
    testfile.write("123\n")

    print('hello~~world', file=testfile)
# end with