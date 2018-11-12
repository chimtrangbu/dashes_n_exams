def check_wave(merged_list):
    flag = merged_list[0] > merged_list[1]
    pos = 1
    while pos < len(merged_list) - 1:
        if merged_list[pos] == merged_list[pos + 1]:
            return False
        cur_flag = merged_list[pos] > merged_list[pos + 1]
        if cur_flag == flag:
            return False
        else:
            flag = not flag
            pos = pos + 1
    return True


def can_wave(input_list):
    sorted_list = sorted(input_list)
    n = len(sorted_list)
    if n == 0:
        return False
    elif n == 1:
        return True
    elif n == 2:
        return False if merged_list[0] == merged_list[1] else True
    else:
        mid = n//2
        list1 = sorted_list[:mid]
        list2 = sorted_list[mid:]
        merged_list = []
        for i in range(len(list2)):
            merged_list.append(list2[i])
            try:
                merged_list.append(list1[i])
            except IndexError:
                pass
        print(merged_list)
        return check_wave(merged_list)

print(can_wave([1,2,3,4,5,6,2,2,2,2,2,1]))
