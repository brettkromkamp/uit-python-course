# Introductory Python Course 2021 - UiT
# By Brett Alistair Kromkamp (brettkromkamp@gmail.com - https://brettkromkamp.com)


# ================================================================================
# Naive file handling
file = open("hello.txt", "w")
file.write("Naive file handling...")
file.close()

# ================================================================================
# Safely open the file
file = open("hello.txt", "w")
try:
    file.write("Safely write to the file...")
finally:
    # Make sure to close the file after using it
    file.close()

# ================================================================================
# Safely open the file
file = open("hello.txt", "w")
try:
    file.write("Safely write to the file with exception handling...")
except Exception as error:
    print(f"An error occurred while writing to the file: {error}")
finally:
    # Make sure to close the file after using it
    file.close()

# ================================================================================
# The 'with' statement approach
with open("hello.txt", mode="w") as file:
    file.write("Safely write to the file with the 'with' statement...")

import os

with os.scandir(".") as entries:
    for entry in entries:
        print(entry.name, "->", entry.stat().st_size, "bytes")

# ================================================================================
class HelloContextManager:
    def __enter__(self):
        print("Entering the context...")
        return "Hello, World!"

    def __exit__(self, exc_type, exc_value, exc_tb):
        print("Leaving the context...")


with HelloContextManager() as hello:
    print(hello)

# ================================================================================
class WritableFile:
    def __init__(self, file_path):
        self.file_path = file_path

    def __enter__(self):
        self.file_object = open(self.file_path, mode="w")
        return self.file_object

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file_object:
            self.file_object.close()


with WritableFile("hello.txt") as writable_file:
    writable_file.write("Safely write to the file with the WritableFile class...")

# ================================================================================
from time import perf_counter, sleep


class Timer:
    def __enter__(self):
        self.start = perf_counter()
        self.end = 0.0
        return lambda: self.end - self.start

    def __exit__(self, *args):
        self.end = perf_counter()


with Timer() as timer:
    # Time-consuming code goes here...
    sleep(0.5)

timer()

# ================================================================================
from contextlib import contextmanager


@contextmanager
def hello_context_manager():
    print("Entering the context...")
    yield "Hello, World!"
    print("Leaving the context...")


with hello_context_manager() as hello:
    print(hello)


@contextmanager
def writable_file(file_path):
    file = open(file_path, mode="w")
    try:
        yield file
    finally:
        file.close()


with writable_file("hello.txt") as file:
    file.write("Write to the file using @contextmanager - from the contextlib library...")
