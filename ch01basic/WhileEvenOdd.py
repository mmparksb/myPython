odd, even = 0, 0

i = 1
while i < 11:
    if i % 2 == 0:
        even += i
    else:
        odd += i
    i += 1
    # end if
# end while

print('홀수의 총합 : %d' % odd)
print('짝수의 총합 : %d' % even)
