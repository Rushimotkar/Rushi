# Function to sort an array using Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Function to sort an array using Shell Sort
def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    # Start with a big gap, then reduce the gap
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            # Shift earlier gap-sorted elements up until the correct location for arr[i] is found
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr

# Function to store and sort percentages, then display top 5 scores
def store_and_sort_percentages():
    # Array to store second-year percentages
    percentages = []

    # Input: Number of students
    n = int(input("Enter the number of students: "))

    # Input: Percentages of students
    for i in range(n):
        percentage = float(input(f"Enter percentage for student {i+1}: "))
        percentages.append(percentage)

    # Sorting the percentages using Insertion Sort
    insertion_sorted_percentages = insertion_sort(percentages.copy())
    print("\nPercentages sorted using Insertion Sort:")
    print(insertion_sorted_percentages)

    # Sorting the percentages using Shell Sort
    shell_sorted_percentages = shell_sort(percentages.copy())
    print("\nPercentages sorted using Shell Sort:")
    print(shell_sorted_percentages)

    # Display the top 5 scores from Shell Sort
    print("\nTop 5 scores:")
    top_5_scores = shell_sorted_percentages[-5:] if len(shell_sorted_percentages) >= 5 else shell_sorted_percentages
    for score in reversed(top_5_scores):  # Reversed to display top scores in descending order
        print(score)

# Run the program
store_and_sort_percentages()
