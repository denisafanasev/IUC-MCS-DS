import math as m
from sys import argv

try:
    ag1, X = argv

    X = int(X)

    def power_two(n):
        return int(m.log(n, 2))

    def unary(_x):
        s = ""
        for i in range(_x-1):
            s = s + "1"
        s = s +"0"

        return s

    def uniform(_x, _bit_number):
        bc = "{0:b}".format(_x)
        for i in range(_bit_number-len(bc)):
            bc = '0'+bc
        return bc

    def gamma(_x):
        return str(unary(1+power_two(_x))) + str(uniform(_x-2**power_two(_x),power_two(_x)))

    if(X>=1):
        print("delta coding for " + str(X))
        step1 = str(gamma(1+power_two(X)))
        print("1) gamma code for "+ str (1+power_two(X)) + " is " + step1)
        step2 = str(uniform(X-2**power_two(X),power_two(X)))
        print("2) plus uniform code for " + str(X-2**power_two(X)) + " in " + str(power_two(X)) + " bits is " + step2)
        print("delta is " + step1+step2)
    else:
        print('wrong number for gamma coding')
except:
    print("error")