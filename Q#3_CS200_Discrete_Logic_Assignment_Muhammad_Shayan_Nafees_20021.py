#Q#3 CS200 Discrete Logic Homework Muhammad Shayan Nafees 20021



# Let say m and n are integers.
# Example:

m = 3  #  value for m.
n = 2  #  value for n.

# a. Check if 6m + 8n is even.
isEven = (6*m + 8*n) % 2 == 0

# b. Check if 10mn + 7 is odd.
isOdd = (10*m*n + 7) % 2 == 1

# c. Check if m^2 - n^2 is composite when m > n > 0.
# A number is composite if it is not prime and greater than 1.
def isPrime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def isComposite(num):
    return num > 1 and not isPrime(num)

is_m2_n2_composite = isComposite(m**2 - n**2)

#Results
print("6m + 8n is even:", isEven)
print("10mn + 7 is odd:", isOdd)
print("m^2 - n^2 is composite when m > n > 0:", is_m2_n2_composite)



'''Output:  
# 6m + 8n is even: True
# 10mn + 7 is odd: True
# m^2 - n^2 is composite when m > n > 0: False'''