from django.shortcuts import render
import time


def home(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        byte_str = myfile.file.read()
        # Convert to a "unicode" object
        text_obj = byte_str.decode('UTF-8')
        columns_descriptions, all_data = read_csv(text_obj.splitlines())
        #
        # print("ORDENAÇÃO selectionSort")

        sorted_data, selection_sort_time = selectionSort(all_data)
        
        # # print("ORDENAÇÃO insertionSort")
        #
        sorted_data, insertion_sort_time = insertionSort(all_data)

        # # print("ORDENAÇÃO bubbleSort")
        sorted_data, bubble_sort_time = bubbleSort(all_data)

        # # print("ORDENAÇÃO shellSort")
        sorted_data, shell_sort_time = shellSort(all_data)

        return render(request, 'result.html', {'columns_descriptions': columns_descriptions,
                                               'sorted_data': sorted_data,
                                               'selection_sort_time': selection_sort_time,
                                               'insertion_sort_time': insertion_sort_time,
                                               'bubble_sort_time': bubble_sort_time,
                                               'shell_sort_time': shell_sort_time})
    else:
        # Nothing to do
        pass

    return render(request, 'home.html')


def read_csv(file):
    all_data = []
    columns_descriptions = []

    # Save all csv data in a list of lists, removing '\n' at the last line element.
    for line in file:
        if not columns_descriptions:
            columns_descriptions = line.split(",")
            columns_descriptions[-1] = columns_descriptions[-1].strip("\n")
        else:
            line_splitted = line.split(",")
            line_splitted[-1] = line_splitted[-1].strip("\n")
            all_data.append(line_splitted)

    return columns_descriptions, all_data


def selectionSort(dataset):
    sorted_data = list(dataset)
    time_initial = time.time()
    for currently_checked_position in range(len(sorted_data)):
        lower_position = currently_checked_position

        for position_searched in range(currently_checked_position+1, len(sorted_data)):
            if int(sorted_data[lower_position][0]) > int(sorted_data[position_searched][0]):
                lower_position = position_searched

        temporary_register = sorted_data[currently_checked_position]
        sorted_data[currently_checked_position] = sorted_data[lower_position]
        sorted_data[lower_position] = temporary_register

    time_final = time.time() - time_initial
    return sorted_data, time_final


def insertionSort(dataset):
    sorted_data = list(dataset)
    time_initial = time.time()
    for currently_checked_position in range(1, len(sorted_data)):
        currently_checked_data = sorted_data[currently_checked_position]

        position_searched = currently_checked_position - 1

        while (position_searched > -1) and int(currently_checked_data[0]) < int(sorted_data[position_searched][0]):
            sorted_data[position_searched + 1] = sorted_data[position_searched]
            position_searched = position_searched - 1

        sorted_data[position_searched + 1] = currently_checked_data

    time_final = time.time() - time_initial
    return sorted_data, time_final


def bubbleSort(dataset):
    sorted_data = list(dataset)
    time_initial = time.time()
    final_position_to_be_checked = len (sorted_data) - 1
    occurred_swap = True

    while (final_position_to_be_checked > 0) and occurred_swap:
        occurred_swap = False

        for currently_checked_position in range(final_position_to_be_checked):
            if int(sorted_data[currently_checked_position][0]) > int(sorted_data[currently_checked_position + 1][0]):
                occurred_swap = True
                temporary = sorted_data[currently_checked_position]
                sorted_data[currently_checked_position] = sorted_data[currently_checked_position+1]
                sorted_data[currently_checked_position+1] = temporary

        final_position_to_be_checked = final_position_to_be_checked - 1

    time_final = time.time() - time_initial
    return sorted_data, time_final

def shellSort(dataset):
    sorted_data = list(dataset)
    time_initial = time.time()

    dataset_length = len(sorted_data)
    gap = int(dataset_length / 2)
    while gap > 0:
            for num in range(gap, dataset_length):
                data = sorted_data[num]
                position = num
                while position >= gap and int(data[0]) < int(sorted_data[position - gap][0]):
                    sorted_data[position] = sorted_data[position - gap]
                    position = position - gap
                    sorted_data[position] = data
            gap = int(gap / 2)

    time_final = time.time() - time_initial
    return sorted_data, time_final