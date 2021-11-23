import timeit


def counting_sort(new_list):
    count_array = [0] * (find_max(new_list) + 1)
    for item in new_list:
        count_array[item] += 1
    index = 0
    for i in range(len(count_array)):
        item = i
        frequency = count_array[i]
        for j in range(frequency):
            new_list[index] = item
            index += 1

    return new_list


def stable_counting_sort(new_list):
    count_array = [None] * (find_max(new_list) + 1)
    for i in range(len(count_array)):
        count_array[i] = []
    for item in new_list:
        count_array[item].append(item)
    index = 0
    print(count_array)
    for i in range(len(count_array)):
        item = i
        frequency = len(count_array[i])
        for j in range(frequency):
            new_list[index] = item
            index += 1

    return new_list


def find_max(list):
    max = list[0]
    # time complexity O(n) to find max
    for item in list:
        if item > max:
            max = item
    return max


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    list_a = [6, 7, 3, 4, 1, 5, 1, 3]
    time = timeit.timeit(lambda: print(stable_counting_sort(list_a)), number= 1)

    print(time)