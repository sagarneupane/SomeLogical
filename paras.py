



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