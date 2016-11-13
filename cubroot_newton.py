n=input('Enter a number to find the cube root : ')
xi=0.3*n
e=0.000000001
while(abs((xi*xi*xi)-n)>e):
	fx=(xi**3)-n
	dfx=3*(xi**2)
	xi=xi-(fx/dfx)

print 'Cube root: ',xi