

list = [12,24,35,70,88,120,155,99,12,7,8,93,67,47,76,34,43,76,23,1, 12,88,7,6,2]

new = [] 

for a in list:
	n = list.count(a)	
	if n > 1:		

		if new.count(a) == 0: 
			new.append(a)

print(new)


