import sys


def readCsv():
    all_data = []
    columns_descriptions = []

    file_path = "EntradaMenor.csv"

    # Treating error while opening the file.
    try:
        file = open(file_path, "r")
    except IOError:
        print("\nNão foi possível abrir o arquivo com o caminho indicado:", file_path)
        sys.exit()

    # Save all csv data in a list of lists, removing '\n' at the last line element.
    for line in file:
        if not columns_descriptions:
            columns_descriptions = line.split(",")
            columns_descriptions[-1] = columns_descriptions[-1].strip("\n")
        else:
            line_splitted = line.split(",")
            line_splitted[-1] = line_splitted[-1].strip("\n")
            all_data.append(line_splitted)

    file.close()

    return all_data, columns_descriptions


def selectionSort(dataset):
    for currently_checked_position in range(len(dataset)):
        lower_position = currently_checked_position

        for position_searched in range(currently_checked_position+1, len(dataset)):
            if int(dataset[lower_position][0]) > int(dataset[position_searched][0]):
                lower_position = position_searched

        temporary_register = dataset[currently_checked_position]
        dataset[currently_checked_position] = dataset[lower_position]
        dataset[lower_position] = temporary_register

    return dataset


def insertionSort(dataset):
    for currently_checked_position in range(1, len(dataset)):
        currently_checked_data = dataset[currently_checked_position]

        position_searched = currently_checked_position - 1

        while (position_searched > -1) and int(currently_checked_data[0]) < int(dataset[position_searched][0]):
            dataset[position_searched + 1] = dataset[position_searched]
            position_searched = position_searched - 1

        dataset[position_searched + 1] = currently_checked_data

    return dataset


def bubbleSort(dataset):
    final_position_to_be_checked = len(dataset) - 1
    occurred_swap = True

    while (final_position_to_be_checked > 0) and occurred_swap:
        occurred_swap = False

        for currently_checked_position in range(final_position_to_be_checked):
            if int(dataset[currently_checked_position][0]) > int(dataset[currently_checked_position + 1][0]):
                occurred_swap = True
                temporary = dataset[currently_checked_position]
                dataset[currently_checked_position] = dataset[currently_checked_position+1]
                dataset[currently_checked_position+1] = temporary

        final_position_to_be_checked = final_position_to_be_checked - 1

    return dataset


dataset, dataset_descriptions = readCsv()
sorted_data = bubbleSort(dataset)

for data in sorted_data:
    print(data[0])
