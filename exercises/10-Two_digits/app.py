#Complete the function to return the tens digit and the ones digit of any interger.
def two_digits(digit):
 
    umil = digit / 1000
    tmp = digit % 1000

    centenas = tmp / 100
    tmp = tmp % 100

    decenas = tmp / 10
    unidades = tmp % 10

    return(decenas, unidades )
   


#Invoke the function with any interger as its argument.
print(two_digits(18))
