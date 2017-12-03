def get_value(char):
    if char in "123456789":
        return int(char)
    elif char.lower() == 'x' or char == '/':
        return 10
    elif char == '-':
        return 0
    else:
        raise ValueError()


def score(game):
    result = 0
    frame = 1
    in_first_half = True

    for rolling in range(len(game)):
        if game[rolling] == '/':
            result += 10 - last
        else:
            result += get_value(game[rolling])

        if frame < 10  and get_value(game[rolling]) == 10:
            if game[rolling] == '/':
                result += get_value(game[rolling + 1])
            elif game[rolling].lower() == 'x':
                result += get_value(game[rolling + 1])

                if game[rolling + 2] == '/':
                    result += 10 - get_value(game[rolling + 1])
                else:
                    result += get_value(game[rolling + 2])

        last = get_value(game[rolling])
        
        if not in_first_half:
            frame += 1

        in_first_half = not in_first_half

        if game[rolling].lower() == 'x':
            in_first_half = True
            frame += 1

    return result