
def reverse(number):
    return int(str(number)[::-1])     

def reversible(number):
    buf = str(number)
    for i in range(len(buf)):
        if int(buf[i]) % 2.0 == 0:
            print i, 'Ungerade'


reversible(4267)

"""
for i in range(100):
    #print i
    buf = i + reverse(i)
    print i, buf
    #if a == 10^8-3:
    #    print a, i
"""    