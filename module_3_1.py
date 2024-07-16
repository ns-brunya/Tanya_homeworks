calls = 0


def count_calls():
    global calls
    calls += 1
    return calls


def string_info(stroka):
    count_calls()
    tuple_ = list()
    tuple_.append(len(stroka))
    tuple_.append(stroka.lower())
    tuple_.append(stroka.upper())
    return tuple(tuple_)


def is_contains(stroka, spisok):
    c = 0
    count_calls()
    stroka = stroka.lower()
    for i in spisok:
        if stroka in i.lower():
            c += 1
    if c != 0:
        return True
    else:
        return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
