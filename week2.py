# Find out the 2 largest variables in the array


def Multiplication(data_len, data_int):
    # read the file
    # file_path = "dataset.txt"  # Replace with the path to your text file
    # with open(file_path, "r") as file:
    #    data = file.read()

    # data_int = list(map(int, data.split(",")))
    # find out the largest 2 data
    largest = 0
    secondlargest = 0
    for i in range(0, data_len):
        if data_int[i] > largest:
            secondlargest = largest
            largest = data_int[i]
        elif data_int[i] > secondlargest:
            secondlargest = data_int[i]
        # print(largest)
        # print(secondlargest)

    return(largest * secondlargest)


# Read the number of elements
n = int(input())

# Read the list of elements
arr = list(map(int, input().split()))
print(Multiplication(n, arr))

