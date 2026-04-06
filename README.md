# Sorting Assignment

**Data Structures – Python Assignment 1, Spring 2026**

## Student Name(s)

- Itamar Bahat 205805856
- name of the other student. 

## Selected Algorithms

| ID | Algorithm |
|----|-----------|
| 1  | Bubble Sort |
| 4  | Merge Sort |
| 5  | Quick Sort |

## How to Run

```bash
# Install dependencies (only needed once)
pip install matplotlib numpy

# Example: compare algorithms 1, 4, 5 on sizes 100–10000, noise type 1 (5%), 10 reps
python run_experiments.py -a 1 4 5 -s 100 500 1000 3000 5000 10000 -e 1 -r 10
```

### Command-line arguments

| Flag | Description |
|------|-------------|
| `-a` | Algorithm IDs (1=Bubble, 2=Selection, 3=Insertion, 4=Merge, 5=Quick) |
| `-s` | Array sizes to test |
| `-e` | Experiment type: `1` = 5% noise, `2` = 20% noise |
| `-r` | Number of repetitions per (algorithm, size) pair |

## Results

### result1.png – Random Arrays

![result1](result1.png)

Bubble Sort is clearly the slowest algorithm. Its runtime grows quadratically (O(n²)), reaching ~3.1 seconds at n=10,000, while Merge Sort and Quick Sort remain nearly flat and close to zero throughout. This matches their theoretical O(n log n) complexity, which grows much more slowly than O(n²). The shaded band around Bubble Sort widens at larger sizes, reflecting greater run-to-run variance as the algorithm takes longer.

### result2.png – Nearly Sorted Arrays (5% noise)

![result2](result2.png)

On nearly sorted input, Bubble Sort improves significantly compared to result1 (~1.75s vs ~3.1s at n=10,000 — nearly 44% faster). This is due to the early-termination optimization: when a full pass over the array produces no swaps, the algorithm stops immediately. On a nearly sorted array (only 5% of elements displaced), most passes after the first few produce no swaps, so the algorithm exits early rather than completing all O(n²) passes. Merge Sort and Quick Sort are essentially unchanged — their O(n log n) performance is not sensitive to the initial order of elements. The overall ranking stays the same, confirming that Merge Sort and Quick Sort are consistently superior to Bubble Sort regardless of input order.
