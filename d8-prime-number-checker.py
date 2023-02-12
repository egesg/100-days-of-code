def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

# Don't change any of the code below
n = int(input("Check this number: "))
prime_checker(number=n)

# Check this number: 4678754
# It's not a prime number.