N = int(input())
a, b = 0, 1
for i in range(N):
     if i == N - 1:
         print(a)
     else:
       print(a, end=" ")
        
     a, b = b, a + b