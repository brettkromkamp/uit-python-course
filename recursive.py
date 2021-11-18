# Introductory Python Course 2021 - UiT
# By Brett Alistair Kromkamp (brettkromkamp@gmail.com - https://brettkromkamp.com)


def countdown(count):
    print(count)
    if count > 0:  # Guard condition
        countdown(count - 1)
    else:
        print("Lift-off!")


def process_list(lis):
    print(lis[0])
    if len(lis) > 1:  # Guard condition
        process_list(lis[1:])


if __name__ == "__main__":
    countdown(10)
    lis1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "Done!"]
    process_list(lis1)
