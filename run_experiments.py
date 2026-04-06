# run_experiments.py
# Data Structures - Python Assignment 1, Spring 2026
# Sorting algorithm comparison experiments

import argparse
import random
import time
import numpy as np
import matplotlib.pyplot as plt


# ─────────────────────────────────────────────
# Part A – Sorting Algorithm Implementations
# ─────────────────────────────────────────────

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break


def selection_sort(arr):
    pass


def insertion_sort(arr):
    pass


def merge_sort(arr):
    if len(arr) <= 1:
        return
    mid = len(arr) // 2
    left, right = arr[:mid], arr[mid:]
    merge_sort(left)
    merge_sort(right)
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]; i += 1
        else:
            arr[k] = right[j]; j += 1
        k += 1
    while i < len(left):
        arr[k] = left[i]; i += 1; k += 1
    while j < len(right):
        arr[k] = right[j]; j += 1; k += 1


def quick_sort(arr, low=None, high=None):
    if low is None:
        low, high = 0, len(arr) - 1
    if low >= high:
        return
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    p = i + 1
    quick_sort(arr, low, p - 1)
    quick_sort(arr, p + 1, high)


# ─────────────────────────────────────────────
# Algorithm registry (ID → name, function)
# ─────────────────────────────────────────────

ALGORITHMS = {
    1: ("Bubble Sort",    bubble_sort),
    2: ("Selection Sort", selection_sort),
    3: ("Insertion Sort", insertion_sort),
    4: ("Merge Sort",     merge_sort),
    5: ("Quick Sort",     quick_sort),
}


# ─────────────────────────────────────────────
# Array generators
# ─────────────────────────────────────────────

def random_array(n):
    """Return an array of n random integers."""
    return [random.randint(0, 10 * n) for _ in range(n)]


def nearly_sorted_array(n, noise_ratio):
    """Return a sorted array with noise_ratio fraction of elements swapped."""
    arr = list(range(n))
    num_swaps = int(n * noise_ratio)
    for _ in range(num_swaps):
        i, j = random.randrange(n), random.randrange(n)
        arr[i], arr[j] = arr[j], arr[i]
    return arr


# ─────────────────────────────────────────────
# Timing helper
# ─────────────────────────────────────────────

def measure(sort_fn, arr):
    """Return elapsed seconds for sort_fn on a copy of arr."""
    data = arr.copy()
    start = time.perf_counter()
    sort_fn(data)
    return time.perf_counter() - start


def run_trials(sort_fn, array_gen, sizes, repetitions):
    """
    For each size, run sort_fn `repetitions` times and return
    (means, stds) as two lists aligned with sizes.
    """
    means, stds = [], []
    for n in sizes:
        times = [measure(sort_fn, array_gen(n)) for _ in range(repetitions)]
        means.append(np.mean(times))
        stds.append(np.std(times))
    return means, stds


# ─────────────────────────────────────────────
# Part B – Random-array experiment → result1.png
# ─────────────────────────────────────────────

def experiment_random(algo_ids, sizes, repetitions):
    plt.figure(figsize=(10, 6))
    for aid in algo_ids:
        name, fn = ALGORITHMS[aid]
        means, stds = run_trials(fn, lambda n: random_array(n), sizes, repetitions)
        means = np.array(means)
        stds  = np.array(stds)
        plt.plot(sizes, means, marker='o', label=name)
        plt.fill_between(sizes, means - stds, means + stds, alpha=0.2)

    plt.xlabel("Array size (n)")
    plt.ylabel("Runtime (seconds)")
    plt.title("Runtime Comparison (Random Arrays)")
    plt.legend()
    plt.tight_layout()
    plt.savefig("result1.png", dpi=150)
    plt.close()
    print("Saved result1.png")


# ─────────────────────────────────────────────
# Part C – Nearly-sorted experiment → result2.png
# ─────────────────────────────────────────────

NOISE_LEVELS = {1: 0.05, 2: 0.20}

def experiment_nearly_sorted(algo_ids, sizes, noise_ratio, repetitions):
    plt.figure(figsize=(10, 6))
    for aid in algo_ids:
        name, fn = ALGORITHMS[aid]
        gen = lambda n, r=noise_ratio: nearly_sorted_array(n, r)
        means, stds = run_trials(fn, gen, sizes, repetitions)
        means = np.array(means)
        stds  = np.array(stds)
        plt.plot(sizes, means, marker='o', label=name)
        plt.fill_between(sizes, means - stds, means + stds, alpha=0.2)

    pct = int(noise_ratio * 100)
    plt.xlabel("Array size (n)")
    plt.ylabel("Runtime (seconds)")
    plt.title(f"Runtime Comparison (Nearly Sorted, noise={pct}%)")
    plt.legend()
    plt.tight_layout()
    plt.savefig("result2.png", dpi=150)
    plt.close()
    print("Saved result2.png")


# ─────────────────────────────────────────────
# Part D – Command-line interface
# ─────────────────────────────────────────────

def parse_args():
    parser = argparse.ArgumentParser(
        description="Sorting algorithm runtime comparison (Assignment 1)"
    )
    parser.add_argument(
        "-a", nargs="+", type=int, required=True,
        metavar="ID",
        help="Algorithm IDs to compare: 1=Bubble 2=Selection 3=Insertion 4=Merge 5=Quick"
    )
    parser.add_argument(
        "-s", nargs="+", type=int, required=True,
        metavar="N",
        help="Array sizes to test (e.g. 100 500 1000)"
    )
    parser.add_argument(
        "-e", type=int, choices=[1, 2], default=1,
        help="Experiment type for result2: 1=5%% noise, 2=20%% noise"
    )
    parser.add_argument(
        "-r", type=int, default=5,
        metavar="REPS",
        help="Number of repetitions per (algorithm, size) pair"
    )
    return parser.parse_args()


def main():
    args = parse_args()

    for aid in args.a:
        if aid not in ALGORITHMS:
            raise ValueError(f"Unknown algorithm ID: {aid}. Choose from 1–5.")

    sizes = sorted(args.s)
    print(f"Algorithms : {[ALGORITHMS[a][0] for a in args.a]}")
    print(f"Sizes      : {sizes}")
    print(f"Repetitions: {args.r}")
    print(f"Noise level: {int(NOISE_LEVELS[args.e] * 100)}%\n")

    # Part B
    experiment_random(args.a, sizes, args.r)

    # Part C
    experiment_nearly_sorted(args.a, sizes, NOISE_LEVELS[args.e], args.r)


if __name__ == "__main__":
    main()
