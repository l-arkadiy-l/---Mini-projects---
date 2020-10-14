input()
numbers = list(map(int, input().split()))
sum_positive = sum(list(filter(lambda x: x > 0, numbers)))
product_numbers = 1
if numbers.index(min(numbers)) + 1 < numbers.index(max(numbers)):
    for i in range(numbers.index(min(numbers)) + 1, numbers.index(max(numbers))):
        product_numbers *= numbers[i]
else:
    for i in range(numbers.index(max(numbers)) + 1, numbers.index(min(numbers))):
        product_numbers *= numbers[i]
print(sum_positive, product_numbers)
