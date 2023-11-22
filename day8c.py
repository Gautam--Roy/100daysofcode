# Challenge - Prime numbers


def prime_checker(number):
    if number > 100:
        print("Please use a number less than 100")
        return
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False

    if is_prime:
        print(f"The number {number} is prime ")
    else:
        print(f"The number {number} is not prime ")


n = int(input("Enter a numner to check for prime: "))
prime_checker(n)
