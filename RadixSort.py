import math


def num_rad_sort(nums, b):
    """
    num_rad_sort takes in an unsorted NON-EMPTY list of numbers
    and will sort them according to the base which should be >= 2
    :param nums: the list of elements to be sorted
    :param b: the base of the numbers
    :return: a sorted list
    :complexity:    time -  O((n+b)*logbM
                    space - O(n+b) (Total space)
                            O(b) (aux space)
    Credit to Week 02 lecture video for the idea on how to make counting sort stable
    """
    if b < 2:
        print("Base needs to be higher")
        return
    if len(nums) < 2:
        return nums
    m = max(nums)
    k = math.ceil(math.log(m + 1, b))
    for col in range(k):
        # Creating an empty count array
        count_array = [None] * b
        # Making sure that each element is a new list in the count array
        for i in range(len(count_array)):
            count_array[i] = []
        # Looping through nums to get the count
        for element in nums:
            item = (element // b ** col) % b
            count_array[item].append(element)
        index = 0
        # looping through the count array to get the order of nums
        for i in range(len(count_array)):
            frequency = len(count_array[i])
            for j in range(frequency):
                nums[index] = count_array[i][j]
                index += 1
    return nums
