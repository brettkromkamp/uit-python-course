# Introductory Python Course 2021 - UiT
# By Brett Alistair Kromkamp (brettkromkamp@gmail.com - https://brettkromkamp.com)

import asyncio  # https://docs.python.org/3/library/asyncio.html
import time

DURATION = 1


async def task():
    print("Step 1")

    # Simulating some kind of time-intensive I/O-based process (that will take one second to complete). Non-blocking call.
    await asyncio.sleep(DURATION)

    print("Step 2")


async def main():
    await asyncio.gather(task(), task(), task())  # Asynchronously execute three tasks


if __name__ == "__main__":
    now = time.perf_counter()
    asyncio.run(main())  # Asynchronous event loop
    elapsed_time = time.perf_counter() - now
    print(f"{__file__} executed in {elapsed_time:0.2f} seconds.")
