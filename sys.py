#!/usr/bin/python
outputNum = ''
sumNumber = 0

print '\033[1;42m Welcome to SYS1010 \033[1;m'
print '\033[1;32mSelect an action \033[1;m'

print('1: 10->2')
print('2: 2->10')
print('3: Return code')
print('3: Return code')
print('4: Additional code')
print('5: Reverse number')
action = input('~')

if action == 1:
    print '\033[1;32mEnter a number in the decimal system \033[1;m'
    number = input('~')

    while number > 0:
        currentNum = number
        number = number // 2
        mulNumber = number*2
        subNumber = currentNum-mulNumber

        if subNumber == 1:
            outputNum = '1' + str(outputNum)
        else:
            outputNum = '0' + str(outputNum)

print 'OUTPUT ~ \033[1;38m'+outputNum+' \033[1;m'

if action == 2:
    print '\033[1;32mEnter a number in the binary system \033[1;m'
    number = input('~')
    current = len(str(number))

    for i in str(number):
        current = current-1
        mNumber = int(i) * (2**current)
        #print(str(i)+' * 2^'+str(current))
        sumNumber = sumNumber + mNumber

print(sumNumber)
