
def swap(i, j, mylist):
	temp1 = mylist[i]
	temp2 = mylist[j]
	mylist[i] = temp2
	mylist[j] = temp1
	#for el in mylist:
		#print el


def sortElement(sorted_list, last_element):
	#sorted_list.append(el)
	index_last = len(sorted_list) - 1
	last_element = sorted_list[index_last]
	#print '** initial list : ' + str(sorted_list).strip('[]') + ' ** \n'
	for i in range(index_last - 1, -1, -1):
		if last_element < sorted_list[i]:
			print 'last_element ( = ' + str(last_element) +') is not superior to '+ str(sorted_list[i])
			print 'swap positions'
			swap(index_last, i, sorted_list)
			#print 'index_el equals now to ' + str(index_el)
			#print 'list is now : ' + str(sorted_list).strip('[]') + '\n'
		else:
			print 'last_element ( = ' + str(last_element) +') is superior to '+ str(sorted_list[i])
		index_last = index_last - 1
		last_element = sorted_list[index_last]
	return sorted_list


def sortList(unsorted_list):
	print '** initial unsorted list : ' + str(unsorted_list).strip('[]') + ' ** \n'
	last_index = len(unsorted_list) - 1
	#el = unsorted_list[last_index]
	for i in range(last_index, -1, -1):
			print 'value processed : ' + str(unsorted_list[last_index])
			unsorted_list = sortElement(unsorted_list, unsorted_list[last_index])
			print 'list is now : ' + str(unsorted_list).strip('[]') + '\n'
			last_index = last_index - 1


el = 4
example1 = [1,2,3,5,6]
example2 = [3,5,6,2,4,1]
example3 = [1,3,2,4,5,6]
#swap(0,1,example)
#sortElement(example2,1)
sortList(example2)