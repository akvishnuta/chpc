n=input('Enter the number to find cube root: ')
epsilon=0.0000000001
a =0.0
b = max(1.0,n)
m = (b+a)/ 2.0
while (abs(m**3 -n)>= epsilon):
    if (m*m*m <= n):
        a= m
    else:
        b= m
    m = (b+a)/2.0
    print m

print 'Cube root : ', m