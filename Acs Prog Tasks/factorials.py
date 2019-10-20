
def numFactorial(num):
 total = 1
 for count in range(1,num):
    total = count * total
    return total

##main program

num = int(input("please enter your number"))
Factorial = numFactorial(num)
print(Factorial)

