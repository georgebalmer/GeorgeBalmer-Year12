i_num = 0
i_num = int(input("please enter a number between 1 and 10"))


while i_num < 1 or i_num > 10:
    i_num=int(input("your did not enter a vaild number, please try again"))
# end while

for x in range(0, 13):
    print(i_num * x)
    x = x + 1
# Next


#Test Data: Input 1 . output
###ACS - Just a few more comment required especially going into kloops of selection constructs
###ACS - Starts with zero .. shoulod strat with 4!
