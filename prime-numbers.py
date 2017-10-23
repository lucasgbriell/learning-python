def primeNumber(number):
    
    num = number
    tempNum = number
    verif = 0
    while tempNum!=0:
        
        if number % tempNum ==0:
            verif = verif + 1

        tempNum -=1
        
    
    if verif==2:
        return 1
    else:
        return 0



test = int(input('digite um numero'))

if (primeNumber (test)==1):
    print('É primo')
else:
    print('Não é primo')




