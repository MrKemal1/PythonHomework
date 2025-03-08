def isPrime(number):
    prime=False
    for i in range(2,int(number**0.5)+1): # Bir sayı kareköküne kadar olan değerlere bölünemezse sonraki sayılara da bölünmez
        if number%i==0:
            prime=False
            break
        else:
            prime=True
            
    if prime==True:
        print(f"{number} is a prime number")
    else:
        print(f"{number} isn't a prime number")
   

while True:
    number=int(input("Please enter a number: " ))
    if number<=2 and number>=0:
        print("The smallest prime number is 2")
    elif number<0:
        print("Please enter a positive number")
    else:
        break
    
isPrime(number)

 