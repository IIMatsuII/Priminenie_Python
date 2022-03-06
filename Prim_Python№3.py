def closest_mod_5(x):
    if x % 5 == 0:
        return x
    elif x % 5 == 1:
        return x + 4
    elif x % 5 == 2:
        return x + 3
    elif x % 5 == 3:
        return x + 2
    elif x % 5 == 4:
        return x + 1