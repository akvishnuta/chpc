n=8
i=n/2
e=0.001
while(abs((i*i*i)-n)>e):
	print i
	i=i/2


print "Cube root : ",i