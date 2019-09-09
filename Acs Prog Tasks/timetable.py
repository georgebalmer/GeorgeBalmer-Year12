i_num = 0
i_num = int(input("please enter a number between 1 and 10"))
        
while i_num < 1 or i_num > 10:
    i_num=int(input("your did not enter a vaild number, please try again"))

for x in range(0, 13):
    print(i_num * x)
    x = x + 1



    
