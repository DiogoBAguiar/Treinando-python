t1,t2,t3,t4 = map(int,input().split())
if all(2 <= t <= 6 for t in [t1,t2,t3,t4]):
   soma = (t1+t2+t3+t4)-3
   print(soma)
   