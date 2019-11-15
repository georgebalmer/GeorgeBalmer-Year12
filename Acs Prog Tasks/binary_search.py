

aList = [1,2,33,4,5,6,7,8,9,10]

def binarysearch(aList, itemSought):
		found = False
		index = -1
		first = 0
		last = len(aList)-1
		while first <= last and found == False:
			midpoint = int((first + last)/2)
			if aList[midpoint] == itemSought:
				found = True
				index = midpoint
			else: 	
				if aList[midpoint] < itemSought:
					first = midpoint + 1 
				else:	
					last = midpoint - 1
				#endif
			#endif
		#endwhile
		return index		
		#endfunction
itemSought = int(input("please enter the number you would like to find"))
#input = itemSought 


print (binarysearch(aList, itemSought))
