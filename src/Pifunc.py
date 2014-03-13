def pi(n):
  sum = 0 
  for i in range(1,n+1):
    a = float(i-1)/n
    print 'Subintervalo: ' "%f" % a
    b = float(i)/n
    print 'Subintervalo: ' "%f" % b
    x = float(i-0.5)/n
    print 'x_i: ' "%f" % x 
    fx = float(4.0/(1.0+x*x))
    print 'fx_i: ' "%f" % fx
    sum = sum + fx
  c = (1.0/n)*sum
  print 'aproximacion: ' "%f" % c
  return c
  
n=int(raw_input("Introduce intervalos: "))
m=int(raw_input("Introduce un numero: "))
l=[]
for j in range(1,m+1):
  c=pi(j*n)
  l=l+[c]
print l


