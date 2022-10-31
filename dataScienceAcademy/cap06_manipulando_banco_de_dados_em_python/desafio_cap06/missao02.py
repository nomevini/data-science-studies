def isPrime(number):
    counter = 0
    
    if number == 2: return True 

    for x in range(2, number):
        if number % x == 0:
            # not is a prime number
            return False
        counter += 1
    if counter:
        return True

def prime_numbers(init, end):
    prime = filter(lambda x : isPrime(x), list(range(init, end + 1)))
    return list(prime)

print(prime_numbers(0, 100))

