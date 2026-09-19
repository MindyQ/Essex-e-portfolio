# Unit 3 · Principles of Computer Science

In this work, I will use Python to sort a list of numbers from smallest to largest with two algorithms: a loopbased algorithm called bubble sort and a recursivebased algorithm called quicksort. I will compare their timecomplexity and efficiency, and furthermore discuss their realworld practical applications.
**Bubble Sort:****Quick Sort****:**

Figure 1                                     Figure 2
 **Comparison****of****performances between bubble sort and quick sort.**
| Number of items in dataset | Bubble Sort (Number of comparisons) | Quick Sort(Number of comparisons) | Speed Gap |
| --- | --- | --- | --- |
| 7 | 21 | 13 | 1.6× |
| 100 | 5,000 | 670 | 7.5× |
| 1,000 | 500,000 | 10,000 | **50×** |
| 10,000 | 50,000,000 | 133,000 | **376×** |
| 100,000 | 5,000,000,000 | 1,660,000 | **~3,000** |


Bubble sort is a loopbased iterative sorting algorithm. It repeatedly goes through the list, compares two adjacent items, and swaps them if they are in the wrong order. Two nested forloops are used to complete this process. The time complexity is O(n2)). Quick sort, in contrast, is a recursive divideandconquer algorithm. It breaks the original list into a left list and a right list, and recursively repeats this splitandsort process on each sublist. Its time complexity is O(n log n).
These two algorithms perform differently with smallsized datasets and large datasets. For smallsized datasets, both algorithms run very quickly. However, the speed gap becomes larger as the datasets get bigger. Bubble sort has the advantages of simple logic and easy-to-write code, but it becomes very inefficient for large datasets because it has to scan the remaining list to find the minimum value in every recursive call. With large datasets, quick sort runs much faster by using a divideandconquer strategy to achieve farbetter performance. However, its worst case can be easily triggered; quicksort can become very slow, which is much more common compared to bubble sort’s worst case. 
Bubble sort is rarely used in professional productionlevel software for largescale data processing. It is mostly limited to small tasks and beginner‑level learning. 
In practical business systems, quick sort is widely used to sort huge datasets such as inventories and database result, thanks to its fast averagecase. Even though quicksort carries a small risk of worstcase O(n2 )performance, engineers can avoid this problem with careful pivotselection strategies, making it a reliable highperformance solution for realworld largedata tasks.
