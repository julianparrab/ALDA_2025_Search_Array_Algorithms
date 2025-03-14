import sys
from searchArray import algorithms
from searchArray import execution_time_gathering
import matplotlib.pyplot as plt

if __name__ == "__main__":
    minimum_size = 100000
    maximum_size = 1000000
    step = 100000
    samples_by_size = 1
    target = 50
    
    table = execution_time_gathering.take_execution_time(minimum_size, maximum_size, step, samples_by_size, target)

    print("Size | Position | Linear | Binary | Ternary | Jump | Interpolation")
    for row in table:
        print(row)

    # Get Data for Plot Size vs Execution Time
    sizes = [row[0] for row in table]
    positions = [row[1] for row in table]    
    Linear = [row[2] for row in table]
    Binary = [row[3] for row in table]
    Ternary = [row[4] for row in table]
    Jump = [row[5] for row in table]
    Interpolation = [row[6] for row in table]

    fig, (plt1, plt2) = plt.subplots(2, 1, figsize=(8,8))

    # Execution Time Plot
    plt1.plot(sizes, Linear, label="Linear O(n log n)", marker="o")
    plt1.plot(sizes, Binary, label="Binary O(n log n)", marker="s")
    plt1.plot(sizes, Ternary, label="Ternary O(n log n)", marker="^")
    plt1.plot(sizes, Jump, label="Jump O(n^2)", marker="d")
    plt1.plot(sizes, Interpolation, label="Interpolation O(n^2)", marker="x")
    plt1.set_xlabel("Input Size")
    plt1.set_ylabel("Execution Time (ms)")
    plt1.set_title("Size vs Execution Time of Search Algorithms")
    plt1.legend()

    plt2.plot(positions, Linear, linestyle='', label="Linear O(n log n)", marker="o")
    plt2.plot(positions, Binary, linestyle='', label="Binary O(n log n)", marker="s")
    plt2.plot(positions, Ternary, linestyle='', label="Ternary O(n log n)", marker="^")
    plt2.plot(positions, Jump, linestyle='', label="Jump O(n^2)", marker="d")
    plt2.plot(positions, Interpolation, linestyle='', label="Interpolation O(n^2)", marker="x")
    plt2.set_xlabel("Target Position")
    plt2.set_ylabel("Execution Time (ms)")
    plt2.set_title("Target Position vs Execution Time of Search Algorithms")
    plt2.legend()

    plt.tight_layout()

    plt.show()
