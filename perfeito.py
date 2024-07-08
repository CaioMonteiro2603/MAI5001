def is_perfect_number(num):
    divisors_sum = sum([i for i in range(1, num) if num % i == 0])
    return divisors_sum == num

def perfect_numbers_between(min_value, max_value):
    perfect_numbers = [num for num in range(min_value, max_value + 1) if is_perfect_number(num)]
    return perfect_numbers

min_value, max_value = map(int, input().split())

perfect_nums = perfect_numbers_between(min_value, max_value)

if perfect_nums:
    for num in perfect_nums:
        print(num)
else:
    print("Não foi encontrado número perfeito")
