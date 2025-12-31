def mdc(a, b):
    while b:
        a, b = b, a % b
    return a

def main():
  
    n_casos = int(input())
    for _ in range(n_casos):
        f1, f2 = map(int, input().split())
        resultado = mdc(f1, f2)
        print(resultado)
            
if __name__ == "__main__":
    main()