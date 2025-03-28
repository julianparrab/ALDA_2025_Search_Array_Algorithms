# ALDA_2025_Search_Array_Algorithms

Repository for Workshop 2: Search in Array Algorithms. This project focuses on implementing and analyzing various search algorithms, highlighting their importance, complexity, and practical applications.

## Project Structure

The project is organized as follows:
ALDA_2025_Search_Array_Algorithms/ │ ├── searchArray/ # Core implementation of search algorithms │ ├── algorithms.py # Implementation of search algorithms │ ├── execution_time_gathering.py # Script to measure execution time of algorithms │ ├── test/ # Unit tests for the project │ ├── test_algorithms.py # Tests for search algorithms │ ├── test_data_generator.py # Tests for data generation utilities │ ├── data/ # Directory for input or generated data (if applicable) │ └── example_data.txt # Example data file (if used) │ ├── results/ # Directory for storing results and graphs │ ├── execution_time_graphs/ # Graphs comparing algorithm performance │ └── summary.txt # Summary of results │ ├── app.py # Main script to run the analysis ├── requirements.txt # Python dependencies for the project ├── README.md # Project documentation └── .gitignore # Files and directories to ignore in version control

## Importance of Search Algorithms

Search algorithms are fundamental in computer science as they enable efficient data retrieval from structures. Their importance lies in:

- **Performance Optimization:** Choosing the right algorithm can significantly reduce execution time.
- **Scalability:** Efficient algorithms are essential for handling large datasets.
- **Practical Applications:** From databases to information retrieval systems, search algorithms are key in many domains.

## Implemented Algorithms

This project includes the implementation of the following search algorithms:

1. **Linear Search:**
   - **Complexity:** 
     - Best case: O(1)
     - Average case: O(n)
     - Worst case: O(n)
   - **Description:** Sequentially traverses the array to find the target element.

2. **Binary Search:**
   - **Complexity:** 
     - Best case: O(1)
     - Average case: O(log n)
     - Worst case: O(log n)
   - **Description:** Divides a sorted array into halves to locate the target element.

3. **Ternary Search:**
   - **Complexity:** 
     - Best case: O(1)
     - Average case: O(log₃ n)
     - Worst case: O(log₃ n)
   - **Description:** Similar to binary search but splits the array into three parts.

4. **Jump Search:**
   - **Complexity:** 
     - Best case: O(1)
     - Average case: O(√n)
     - Worst case: O(√n)
   - **Description:** Skips blocks of elements to reduce the number of comparisons.

5. **Interpolation Search:**
   - **Complexity:** 
     - Best case: O(1)
     - Average case: O(log log n)
     - Worst case: O(n)
   - **Description:** Estimates the position of the target element in uniformly distributed arrays.

## Implementation

The algorithms are implemented in the file [`searchArray/algorithms.py`](searchArray/algorithms.py). Additionally, tools for measuring execution time for different input sizes are provided in [`searchArray/execution_time_gathering.py`](searchArray/execution_time_gathering.py).

## Testing

The project includes unit tests to ensure the correctness of the algorithms and data generators. Tests are located in:

- [`test/test_algorithms.py`](test/test_algorithms.py): Tests for search algorithms.
- [`test/test_data_generator.py`](test/test_data_generator.py): Tests for random data generators.

## Execution

To analyze the algorithms and generate comparative graphs, use the main script [`app.py`](app.py). This script measures execution time and generates graphs showing the relationship between input size and execution time.

## Results
The results include graphs comparing the execution time of the algorithms based on input size and target position. These visualizations highlight the performance differences between the algorithms.

The analysis was conducted using a dataset with a minimum size of **1 million elements** and a maximum size of **10 million elements**, incrementing by steps of 1 million. For each dataset size, a **target value of -1** was used to simulate the **worst-case scenario** for all search algorithms, as this value is guaranteed not to exist in the dataset.

The results include the following:

1. **Size vs Execution Time:** A graph showing the relationship between the input size and the execution time for each algorithm.
2. **Target Position vs Execution Time:** A graph showing the relationship between the target position (or lack thereof) and the execution time for each algorithm.

The graphs were generated using **Matplotlib**, a Python library for data visualization. These visualizations highlight the performance differences between the implemented search algorithms, showcasing their time complexity in practice.

### Result Graphs

![`Data Runtime`](media/Data%20Results.png)

![`Runtime`](media/Time%20Algorithms%20target%20-1.png)

### Analysis of Results

#### Linear Search (O(n)):
- As expected, the execution time of linear search increases linearly with the size of the input. This means that as the list grows, the time required to find an element grows proportionally.
- This graph clearly demonstrates that linear search is the least efficient for large datasets.

#### Binary Search (O(log n)), Ternary Search (O(log₃ n)), and Interpolation Search (O(log log n)):
- These algorithms show a much slower growth in execution time as the input size increases.
- This confirms their efficiency for large datasets, as the search time increases logarithmically or even more slowly.
- Among these, **interpolation search** is the most efficient, as shown in the top graph.

#### Jump Search (O(√n)):
- This algorithm exhibits intermediate performance between linear search and logarithmic searches.
- Its execution time increases more slowly than linear search but faster than binary, ternary, and interpolation searches.

These observations highlight the importance of selecting the appropriate search algorithm based on the size and characteristics of the dataset. For large datasets, logarithmic or interpolation-based searches are significantly more efficient than linear or jump searches.


## Conclusions

## Conclusions

This project demonstrates how different search algorithms have advantages and disadvantages depending on the use case. Choosing the right algorithm can make a significant difference in terms of efficiency and performance.

- For large datasets, logarithmic search algorithms (binary, ternary, interpolation) are significantly more efficient than linear search.
- Jump search offers a balance between the simplicity of linear search and the efficiency of logarithmic searches.
- The position of the target element directly affects the execution time of linear search but does not significantly impact the other algorithms shown in the graph.
- Interpolation search demonstrates the best performance among all the algorithms analyzed in this project.




