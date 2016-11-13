n=input('Enter the number to find cube root : ')
i=n/2
e=0.001
while(abs((i*i*i)-n)>e):
	print i
	i=i/2


print "Cube root : ",i
