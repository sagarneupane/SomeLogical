
# This program prints the prime numbers 
# Here you need to tell program upto which number you want to print prime
# Foreg give n = 10 then program will give you list of prime numbers upto 10 . i.e 2,3,5,7


def primenumber(n):
    
    list_prime = []
    
    for i in range(2,n):
        count = 0
        for j in range(1,i):
            if i%j == 0:
                count+=1
        if count < 2:
            list_prime.append(i)
    
    return list_prime

n = int(input("Enter the number:"))
print(f"The prime numbers upto {n} are:: ",primenumber(n+1))