powers = []
for pow in range(15, -1,-1):
    powers.append(2 ** pow)

binaryOutput = ''
while True:
    decimalInput = int(input('Enter a number between 1 and 65535: '))
    if decimalInput <= 65535 and decimalInput >= 1:
        for power in powers:
            binaryOutput = binaryOutput + str(decimalInput // power)
            decimalInput %= power
        print(binaryOutput)        
    else:  
        print('You did not enter a number between 1 and 65535')
    binaryOutput = ''
    print('Convert another number(y/n)?')
    ans = input()
    if ans != 'y':
        break
