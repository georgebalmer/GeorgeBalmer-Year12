def numFactorial(num):
 factorial=0
 if num==0:
   factorial = 1
 else:
   factorial = num * numFactorial(num-1)
 ##end if
 return factorial
   

##main program

num = int(input("please enter your number"))
Factorial = numFactorial(num)
print(Factorial)
