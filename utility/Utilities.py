import time


def clear_console():
    print("\033[H\033[J", end="")

def ask_for_string(message: str) -> str:
    return input(message)

def clear_line(times=1):
    for x in range(times):
        output = "\033[A"
        for y in range(50):
            output += " "
        output += "\033[A"
        print(output)

def ask_for_int(message: str) -> int:
    first_loop = True
    while True:
        user_input = input(message)
        try:
            return int(user_input)
        except ValueError:
            if first_loop:
                clear_line()
            else:
                clear_line(2)
            print('Try again - a number this time.')
            first_loop = False

def ask_for_positive_int(message: str, higher_limit=None) -> int:
    first_loop = True
    while True:
        user_number = ask_for_int(message)

        if user_number < 1:
            if first_loop:
                clear_line()
            else:
                clear_line(2)

            print(f"Positive numbers please.")

            first_loop = False
        elif higher_limit is not None and user_number > higher_limit:
            if first_loop:
                clear_line()
            else:
                clear_line(2)

            print(f"Max you can input is {higher_limit}.")

            first_loop = False
        else:
            return user_number

def ask_for_bool(message: str) -> bool:
    first_loop = True
    while True:
        decision = input(message)
        if decision.lower() == 'y':
            return True
        elif decision.lower() == 'n':
            return False
        else:
            if first_loop:
                clear_line()
            else:
                clear_line(2)

            print("Y or N please.")

            first_loop = False

def pause_for_dramatic_effect():
    time.sleep(3)
