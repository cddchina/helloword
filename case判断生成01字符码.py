import Queue

l1 = ['1','0']
l2 = ['11','10','02']
l3 = ['111','110','102','022']
l4 = ['1111','1110','1102','1022','0222']
l5 = ['11111','11110','11102','11022','10222','02222']



q = Queue.Queue()
#l = [1,2,1,1,3,1]
inText = eval(raw_input('please input your list:\n'))
print inText
l =inText
print l
sumLen = 0

for i in range(len(l)):
	print "%d"%l[i]
	if (1==l[i]):
		sumLen += 1
		if (q.empty()):
			for j in range(len(l1)):
				q.put(l1[j])
		else:
			while not q.empty():
				tmp = q.get()
				if (sumLen == len(tmp)):
					q.put(tmp)
					break
				else:
					for j in range(len(l1)):
						q.put(tmp+l1[j])
	elif (2==l[i]):
		sumLen += 2
		if (q.empty()):
			for j in range(len(l2)):
				q.put(l2[j])
		else:
			while not q.empty():
				tmp = q.get()
				if (sumLen == len(tmp)):
					q.put(tmp)
					break
				else:
					for j in range(len(l2)):
						q.put(tmp+l2[j])
	elif (3==l[i]):
		sumLen += 3
		if (q.empty()):
			for j in range(len(l3)):
				q.put(l3[j])
		else:
			while not q.empty():
				tmp = q.get()
				if (sumLen == len(tmp)):
					q.put(tmp)
					break
				else:
					for j in range(len(l3)):
						q.put(tmp+l3[j])
	elif (4==l[i]):
		sumLen += 4
		if (q.empty()):
			for j in range(len(l4)):
				q.put(l4[j])
		else:
			while not q.empty():
				tmp = q.get()
				if (sumLen == len(tmp)):
					q.put(tmp)
					break
				else:
					for j in range(len(l4)):
						q.put(tmp+l4[j])
	else:
		print "i > 4:error"

num = 1;
with open('./output.txt','w') as f:
	while not q.empty():
		num = num+1
		str = q.get()
		print "%s,%d"%(str,num-1)
		f.write(str + '\r\n')

					

				
				
			
				
