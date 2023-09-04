import decimal

def teste():
    x = 23
    y = 1.05
    d = decimal.Decimal(23) / decimal.Decimal("1.05")

    print( x / y )
    print( d )

# teste()

def teste2():
    str1 = "João da SIlva"
    for c in str1:
        print(c,end=' ')

teste2()