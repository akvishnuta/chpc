n=input('Enter the number to find cube root : ')
i=n/2.0
e=0.001
while(abs((i*i*i)-n)>e):
	print i
	i=i/2.0


print "Cube root : ",i
