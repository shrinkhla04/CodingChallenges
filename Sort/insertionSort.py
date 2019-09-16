def insertionSort(l):
	for sliceEnd in range(1,len(l)):
		pos = sliceEnd
		while pos > 0 and l[pos] < l[pos - 1]:
			min = l[pos]
			l[pos] = l[pos - 1]
			l[pos - 1] = min 
			pos = pos - 1
	print(l)
insertionSort([4,0,9,8,2])
