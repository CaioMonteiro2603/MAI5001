def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_numbers_between(min_value, max_value):
    prime_numbers = []
    for num in range(min_value, max_value + 1):
        if is_prime(num):
            prime_numbers.append(num)
    return prime_numbers

min_value, max_value = map(int, input().split())

prime_numbers = prime_numbers_between(min_value, max_value)

if prime_numbers:
    print(*prime_numbers)
else:
    print("Não há números primos")
