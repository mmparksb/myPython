total = 0

for i in range(1,11):
    print(i)
    total += i
# end for <ㅡ 설진욱 선생님은 for문의 끝을 구별하신다..

print('총합 01 : %d'%total)

## range(start, stop, step)
## default start : 0 step : +1

total = 0
for i in range(1,101,3):
    total +=i
    if i!=1:
        print('+%d' %i, end='')
    else:
        print('\n%d' % i, end='')
    # end if
# end for
print('=%d' %total)
print('총합 02 : %d' %total)

total = 0
for i in range(97,1,-5):
    total +=i
    if i!=97:
        print('+%d' %i, end='')
    else:
        print('\n%d' % i, end='')
    # end if
# end for
print('=%d' %total)
print('총합 03 : %d' %total)

total = 0
for i in range(1,97,5):
    total +=i**2 ## i*i = i**2
    if i!=1:
        print('+%d*%d' %(i,i), end='')
    else:
        print('\n%d*%d' % (i,i), end='')
    # end if
# end for
print('=%d' %total)
print('총합 04 : %d' %total)

total = 0
for i in range(1,6):
    total +=i*(i+1)
    if i != 1:
        print('+%d*%d' % (i, (i+1)), end='')
    else:
        print('\n%d*%d' % (i, (i+1)), end='')
    # end if
# end for
print('=%d' % total)
print('총합 05 : %d' %total)


