n1 = int(input('Enter first number: '))
n2 = int(input('Enter second number: '))
n3 = int(input('Enter third number: '))

if(n1>n2 and n1>n3):
    print(str(n1)+' is the largest')

elif(n2>n3 and n2>n1):
    print(str(n2) + ' is the largest')

elif(n3>n1 and n3>n2):
    print(str(n3) + ' is the largest')
else:
    print('All are equal')