def mdc(x,y):
    if y == 0:
        return x
    else:
        return mdc(y, x % y)
    
x = int(input()); y = int(input())
print(mdc(x,y))