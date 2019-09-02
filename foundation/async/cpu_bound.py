import time
from concurrent.futures import ProcessPoolExecutor


def cpu_bound(number):
    print(sum(i * i for i in range(number)))


def calculate_sums(numbers):
    for number in numbers:
        cpu_bound(number)


NUMBER = 10000000


def main():
    start_time = time.perf_counter()
    numbers = [NUMBER + x for x in range(20)]
    calculate_sums(numbers)
    end_time = time.perf_counter()
    print("Calculation takes {} seconds".format(end_time - start_time))


def multi_cpu_main():
    start_time = time.perf_counter()

    with ProcessPoolExecutor() as executor:
        executor.map(cpu_bound, list(range(NUMBER, NUMBER + 20)))
    end_time = time.perf_counter()
    print("Calculation takes {} seconds".format(end_time - start_time))


if __name__ == "__main__":
    # main()  # Calculation takes 29.3912804 seconds
    multi_cpu_main()
