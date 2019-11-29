#convert Binary to decimal

def BinToDec(n):
    if (len(n))== 0:
        return 0
    else:
        return BinToDec(n[:-1]) * 2 + (n[-1] == '1')


Num = input("enter a binary code:")
print(BinToDec(Num))
