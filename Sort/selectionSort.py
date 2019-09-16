def SelectionSort(l):
	for start in range(len(l)):
		for i in range(start+1,len(l)):
			if l[i] < l[start]:
				min = l[i]
				l[i], l[start] = l[start], min

	print(l)
SelectionSort([5,6,7,9,2,0,4])