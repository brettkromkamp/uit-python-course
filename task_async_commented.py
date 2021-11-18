import asyncio  # https://docs.python.org/3/library/asyncio.html
import time

DURATION = 1

# Native coroutine
async def task():
    print("Step 1")

    # The 'await' keyword passes control back to the event loop (i.e., it suspends the execution of the surrounding coroutine).
    # So, the task() function/coroutine will be suspended and resumed when process() is ready.

    # Simulating some kind of time-intensive I/O-based process (that will take one second to complete). Non-blocking call.
    p = await process()  # await asyncio.sleep(DURATION)

    print("Step 2")


async def process():
    await asyncio.sleep(DURATION)


async def main():
    await asyncio.gather(task(), task(), task())  # Asynchronously execute three tasks


if __name__ == "__main__":
    now = time.perf_counter()
    asyncio.run(main())  # Asynchronous event loop
    elapsed_time = time.perf_counter() - now
    print(f"{__file__} executed in {elapsed_time:0.2f} seconds.")
