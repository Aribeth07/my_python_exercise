
lower = int(input("Start? "))
upper = int(input("End? "))

def check_prime(x, y):
    prime_list = []
    for num in range(x, y+1):
        if num > 1:              # all primes are greater than 1
            k = int(num**0.5)+1  # same result, way faster
            for i in range(2, k):
                if (num % i) == 0:
                    break
            else:
                prime_list.append(num)
    return prime_list
            
prime_list = check_prime(lower, upper)
length = len(prime_list)       
per = length / (upper-lower+1)  

p = input("Do you wanna see the number list?(y/N): ") 
if  p == "y":                    # "no" by default
    print(f"Primes between {lower} and {upper} are:\n{prime_list}")
print(f"Total primes count: {length}")
print(f"Percentage: {per:.2%}")