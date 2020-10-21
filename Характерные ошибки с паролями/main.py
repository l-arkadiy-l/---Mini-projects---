dict_error = {}


class PasswordError(Exception):
    def __init__(self, error):
        self.error = error
        try:
            dict_error[error] += 1
        except KeyError:
            dict_error[error] = 1


class LengthError(PasswordError):
    pass


class LetterError(PasswordError):
    pass


class DigitError(PasswordError):
    pass


class SequenceError(PasswordError):
    pass


class CheckPassword:
    def __init__(self, password):
        self.password = password

    def check_length(self):
        return len(self.password) > 8

    def is_three_sequence(self, value: str) -> bool:
        def check(d: dict, a: str, b: str, c: str):
            return all(isinstance(d.get(char), int) for char in (a, b, c)) and \
                   (d[a] - d[b] == 1 and d[b] - d[c] == 1 or d[c] - d[b] == 1 \
                    and d[b] - d[a] == 1)

        # \n для разрыва последовательности, где начинается другой ряд
        eng = dict(zip('qwertyuiop\nasdfghjkl\nzxcvbnm', range(26)))
        rus = dict(zip('йцукенгшщзхъ\nфывапролджэё\nячсмитьбю', range(32)))
        for i in range(len(text := value.lower()) - 2):
            if check(eng, text[i], text[i + 1], text[i + 2]) \
                    or check(rus, text[i], text[i + 1], text[i + 2]):
                return False
        return True

    def check_symbols(self):
        if self.password == self.password.lower() or \
                self.password == self.password.upper():
            return False
        return True

    def check_number(self):
        return [True for i in self.password if i in '1234567890']

    def check_combination(self):
        return self.is_three_sequence(self.password)


def check_password(password, all_password):
    password = CheckPassword(password)
    try:
        if password.password in all_password:
            PasswordError('WordError')
        if not password.check_length():
            PasswordError('LengthError')
        if not password.check_symbols():
            PasswordError('LetterError')
        if not password.check_number():
            PasswordError('DigitError')
        if not password.check_combination():
            PasswordError('SequenceError')
    except PasswordError:
        return 'LengthError'


if __name__ == '__main__':
    with open('top-9999-words.txt') as f:
        all_password = [i for i in f.read().split('\n')]
    with open('top 10000 passwd.txt') as f_password:
        passwords = f_password.read()
        for password in passwords.split('\n'):
            try:
                assert check_password(password, all_password) == 'ok'
            except AssertionError:
                pass

    for i in sorted(dict_error):
        print('{}: {}'.format(i, dict_error[i]))
