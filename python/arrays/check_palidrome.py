def check_palindrom(input_str):
    # print(input_str)
    backwards = []
    forwards = []
    n = len(input_str)
    for idx in range(len(input_str)-1, -1, -1):
        val = input_str[idx].lower()
        if val.isalpha():
            backwards.append(val)

        val_f = input_str[n - idx- 1].lower()
        if val_f.isalpha():
            forwards.append(val_f)

   # print(f"{''.join(forwards)} {''.join(backwards)}")
    return ''.join(forwards) == ''.join(backwards)


input_str = input()

print(check_palindrom(input_str))