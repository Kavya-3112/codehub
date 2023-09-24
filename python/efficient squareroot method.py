import math

def get_divisors(n):
    divisors = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            if n // i != i:
                divisors.append(n // i)
    
    divisors.sort()  # Sort the divisors in ascending order
    return divisors

# Example usage:
num = 7
divisors = get_divisors(num)
print(divisors)
