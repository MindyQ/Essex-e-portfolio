# Unit 3 · Principles of Computer Science

> Algorithmic thinking — comparing two classic sorting strategies in Python.

## Task / Assignment
Implement and compare **bubble sort** (loop-based) vs **quicksort** (recursive, divide-and-conquer),
measure their time complexity, and discuss real-world use.

Key findings:

| Dataset size | Bubble sort (comparisons) | Quicksort (comparisons) | Speed gap |
|---|---|---|---|
| 7 | 21 | 13 | 1.6× |
| 100 | 5,000 | 670 | 7.5× |
| 1,000 | 500,000 | 10,000 | 50× |
| 10,000 | 50,000,000 | 133,000 | 376× |
| 100,000 | 5,000,000,000 | 1,660,000 | ~3,000× |

- **Bubble sort** — `O(n²)`, two nested loops, simple to write, fine for tiny tasks / learning, rarely used
  in production at scale.
- **Quicksort** — `O(n log n)` average, recursive split; far faster on big data (inventory / DB result
  sorting), but a careless pivot can hit its `O(n²)` worst case.

## Associated source files
| File | Type | Notes |
|------|------|-------|
| `Unit3 algorithm analysis.docx` | Word | Full comparison write-up + performance table |

## Takeaway
Choose the algorithm to fit the data size; divide-and-conquer wins decisively as datasets grow.
