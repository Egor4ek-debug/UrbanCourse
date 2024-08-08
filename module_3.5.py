def get_multiplied_digits(digital):
    if digital == 1:
        return 1
    else:
        return digital * get_multiplied_digits(digital - 1)


print(get_multiplied_digits(5))
