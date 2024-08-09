def get_multiplied_digits(digital):
    number_str = str(digital)
    if len(number_str) == 1:
        return int(number_str)

    return int(number_str[0]) * get_multiplied_digits(int(number_str[1:]))


print(get_multiplied_digits(40203))
