# multiprocessing = running tasks in parallel on different
# cpu cores, bypasses GIL used for threading
# multiprocessing = better for cpu bound tasks (heavy cpu)
# multithreading = better for io bound tasks (waiting around for input)

from multiprocessing import Process, cpu_count
import time


def counter(num):
    count = 0
    while count < num:
        count += 1


def main():
    print("cpu count: ", cpu_count())