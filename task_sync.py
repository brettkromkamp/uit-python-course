# Introductory Python Course 2021 - UiT
# By Brett Alistair Kromkamp (brettkromkamp@gmail.com - https://brettkromkamp.com)

import time

DURATION = 1


def task():
    print("Step 1")

    # Simulating some kind of I/O call that take a long time (that will take one second to complete). Blocking call.
    time.sleep(DURATION)

    print("Step 2")


def main():
    for _ in range(3):  # Call three separate tasks to be executed
        task()


if __name__ == "__main__":
    now = time.perf_counter()
    main()
    elapsed_time = time.perf_counter() - now
    print(f"{__file__} executed in {elapsed_time:0.2f} seconds.")
