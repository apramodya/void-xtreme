def classic_round(number):
    int_num = int(number)
    if number - int_num >= 0.5:
        return int_num + 1
    else:
        return int_num
