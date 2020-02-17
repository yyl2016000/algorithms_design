def SequentialSearch(in_list : list, target : int):
    for index,i in enumerate(in_list):
        if i == target:
            return index
    return -1

if __name__ == "__main__":
    in_list = input("Please input a num list, splitted by ' ':").split()
    in_list = list(map(int, in_list))
    print("The list is:", in_list)
    target = int(input("Please input target num:"))
    result = SequentialSearch(in_list, target)
    if result == -1:
        print("Search Failed!")
    else:
        print("First target num's index is:", result)