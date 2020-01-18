def SelectionSort(in_list : list):
    for i in range(len(in_list) - 1):
        min_position = i
        for j in range(i + 1, len(in_list)):
            if in_list[j] < in_list[i]:
                min_position = j 
        in_list[i], in_list[min_position] = in_list[min_position], in_list[i]

if __name__ == '__main__':
    in_list = input("Please input a num list, splitted by ' ':").split()
    in_list = list(map(int, in_list))
    SelectionSort(in_list)
    print("Sorted list is", in_list)