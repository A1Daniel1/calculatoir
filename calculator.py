import math

def main():
    number = int(input("number: "))

    if validate(number):
        print(f"The number {number} works!")
    else:
        print("The number doesn't work")

def validate(n):
    factorize(n)
    

def factorize():
    i = 2 
    factores_primos = [] 
    while i * i <= numero: 
        if numero % i: 
            i += 1 
        else: 
            numero //= i 
            factores_primos.append(i) 
    if numero > 1: 
        factores_primos.append(numero) 
    return factores_primos 

if __name__ == '__main__':
    main()
