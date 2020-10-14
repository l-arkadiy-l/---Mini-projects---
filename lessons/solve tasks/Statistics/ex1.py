input()
days = input()
days_odd = list(filter(lambda x: int(x) % 2 == 0, days.split()))
days_even = list(filter(lambda x: int(x) % 2 != 0, days.split()))
true_false = len(days_odd) >= len(days_even)
if true_false:
    true_false = 'YES'
else:
    true_false = 'NO'
print(' '.join(days_even), ' '.join(days_odd), true_false, sep='\n')
