# Strong Number in Python in this article.
# If for a number, the sum of the factorial
# of each of the digits of the
# number equals the given number,
# then such a number is called a
# strong number. Example is 145 as 1!+4!+5! == 145

n = int(input('Enter the number: '))
s = 0
num = n
while(n>0):
    digit = n%10
    fact = 1
    for i in range(1,digit+1):
        fact = fact*i
    s = s+fact
    n = n//10
if(s==num):
    print('Strong Number')
else:
    print('Not a Strong Number')


