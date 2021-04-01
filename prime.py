n = int(input('Enter the number: '))

if(n==1 or n==0):
    print('Neither Prime nor Composite')
elif(n<0):
    print('Input is Invalid, Enter a whole no.')


else:
    count = 0

    for i in range(1, n + 1):
        if (n % i == 0):
            count = count + 1

    if (count > 2):
        print('Composite no.')
    else:
        print('Prime No.')