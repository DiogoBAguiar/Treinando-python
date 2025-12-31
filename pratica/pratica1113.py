a,b = map(int, input().split())
while a != b:   
 if a < b:
  print("Crescente")
  
 elif a > b:
    print("Decrescente")
    
 a,b = map(int, input().split())    
    