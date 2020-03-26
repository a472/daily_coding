def invert(num):
    num=str(num)
    inverted=''
    for i in num:
        if int(i):
            inverted+='0'
        else:
            inverted+='1'
    return inverted

num=10100101
print(invert(num))