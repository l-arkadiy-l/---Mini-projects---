input_string = input()
if input_string == ''.join(reversed(input_string)):
    print('Палиндром')
else:
    print('Не палиндром')
