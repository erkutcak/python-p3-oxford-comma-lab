def oxford_comma(items):
    if len(items) == 1:
        return items[0]
    elif len(items) == 2:
        return "{} and {}".format(items[0], items[1])
    elif len(items) == 3:
        return "{}, {}, and {}".format(items[0], items[1], items[2])
    else:
        return f"{', '.join(items[:-1])}, and {items[-1]}"
