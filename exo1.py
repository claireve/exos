

def findIndexOfMinimum(mylist, first_index):
	minimum = mylist[first_index]
	indexMin = first_index
	for i in range(first_index, len(mylist)):
		if mylist[i] < minimum:
			#print mylist[i]
			minimum = mylist[i]
			indexMin = i
	return indexMin

def modifyList(mylist, first_index):
	indexMin = findIndexOfMinimum(mylist, first_index)
	print 'indexMin equals to : ' + str(indexMin) + '\n'
	#mylist[indexMin] = mylist[0]
	temp = mylist[first_index]
	mylist[first_index] = mylist[indexMin]
	mylist[indexMin] = temp


def sortList(mylist):
	for i in range(len(mylist)):
		first_index = i
		modifyList(mylist, first_index)
	for el in mylist:
		print el

example = [3,5,1,94,2,434]
#findIndexOfMinimum(example)
sortList(example)
