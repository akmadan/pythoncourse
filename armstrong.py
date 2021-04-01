# Armstrong number is a number that is equal
# to the sum of cubes of its digits. For example
# 0, 1, 153, 370, 371 and 407 are the
# Armstrong numbers. Let's try to understand
# why 153 is an Armstrong number.

n = int(input('Enter the number: '))
num = n

s = 0

while(n>0):
    digit = n%10    # finding  the last digit
    s = s+(digit**3)
    n = n//10
if(s==num):
    print('Armstrong Number')
else:
    print('Not an Armstrong Number')

