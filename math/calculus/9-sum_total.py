#/usr/bin/env python3

def summation_i_squared(n):
    if  isinstance(n, int) and n > 0 :
        i = 1
        x = 0
        for i in range(i,1,n):
            x += i**2

            return x

    else:
        return None
