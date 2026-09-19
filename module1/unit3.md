# Unit 3 · Principles of Computer Science

> Comparing two classic sorting algorithms — bubble sort and quicksort — in complexity, behaviour, and real-world use.

## The two algorithms
Bubble sort is a loop-based, iterative algorithm. It repeatedly walks the list, compares two adjacent items, and swaps them if they are in the wrong order. Two nested `for` loops complete the process, giving a time complexity of **O(n²)**.

Quicksort, by contrast, is a recursive divide-and-conquer algorithm. It splits the list into a left part and a right part, then recursively repeats this split-and-sort on each sub-list. Its time complexity is **O(n log n)**.

## Performance on growing datasets
Both run quickly on small datasets, but the speed gap widens sharply as data grows:

| Items in dataset | Bubble sort (comparisons) | Quicksort (comparisons) | Speed gap |
|---|---|---|---|
| 7 | 21 | 13 | 1.6× |
| 100 | 5,000 | 670 | 7.5× |
| 1,000 | 500,000 | 10,000 | 50× |
| 10,000 | 50,000,000 | 133,000 | 376× |
| 100,000 | 5,000,000,000 | 1,660,000 | ~3,000× |

## Practical implications
Bubble sort has simple logic and easy code, but becomes very inefficient for large datasets, so it is rarely used in production software — it is mostly limited to small tasks and beginner learning.

Quicksort runs much faster on large data thanks to divide-and-conquer, and is widely used to sort huge datasets such as inventories and database results. Its worst case (O(n²)) can be triggered more easily than bubble sort's, but engineers avoid it with careful pivot selection, making quicksort a reliable high-performance choice for real-world big-data tasks.
