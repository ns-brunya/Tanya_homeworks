list_ = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0
while i <= len(list_):
    if list_[i] != 0:
        if list_[i] > 0:
            print(list_[i])
            i += 1
        else:
            break
