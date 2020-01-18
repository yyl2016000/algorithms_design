def BubbleSort_raw(in_list : list):
    for i in range(len(in_list), 1, -1):
        for j in range(1, i):
            if in_list[j] < in_list[j-1]:
                in_list[j-1], in_list[j] = in_list[j], in_list[j-1]

def BubbleSort_better(in_list : list):
    for i in range(len(in_list), 1, -1):
        flag = 1
        for j in range(1, i):
            if in_list[j] < in_list[j-1]:
                in_list[j-1], in_list[j] = in_list[j], in_list[j-1]
                flag = 0
        if flag == 1:
            break

if __name__ == '__main__':
    in_list = list(map(int, input("Please input a num list, splitted by ' ':").split()))
    mode = int(input("Please select mode:\n1.raw\n2.better\n"))
    BubbleSort_raw(in_list) if mode == 1 else BubbleSort_better(in_list)
    print("Sorted list is", in_list)