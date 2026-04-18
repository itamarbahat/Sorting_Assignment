# Sorting Assignment

**Data Structures – Python Assignment 1, Spring 2026**

## Student Name(s)

- Itamar Bahat 205805856
- Yotam Vortman 206913238
 

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

Each figure contains two panels. The **left panel (linear scale)** shows the dramatic practical difference: Bubble Sort reaches ~3 seconds at n=10,000 while Merge Sort and Quick Sort are nearly invisible near zero. The **right panel (log scale)** reveals the growth rates of all three algorithms: Bubble Sort's steeper slope corresponds to O(n²) complexity, while Merge Sort and Quick Sort have a clearly shallower slope consistent with O(n log n). The shaded bands show standard deviation across 10 repetitions.

### result2.png – Nearly Sorted Arrays (5% noise)

![result2](result2.png)

On nearly sorted input, Bubble Sort improves significantly: ~1.75s vs ~3s at n=10,000 (about 44% faster). This is due to the **early-termination optimization** — when a full pass produces no swaps, the algorithm stops immediately. On a nearly sorted array (only 5% of elements displaced), most passes after the first few produce no swaps, so the algorithm exits far earlier than O(n²) passes. This effect is visible on the log scale panel: Bubble Sort's line shifts downward compared to result1, while Merge Sort and Quick Sort are essentially unchanged — their O(n log n) performance is insensitive to input order. The overall ranking remains the same regardless of input type.
