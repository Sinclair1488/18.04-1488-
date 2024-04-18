def ask_password():
    pasw = 'qwerty'
    c = 0
    while c != 3:
        p_pasw = input()
        c += 1
        if pasw == p_pasw:
            print('Пароль принят')
        else:
            print("В доступе отказано")


print(ask_password())
