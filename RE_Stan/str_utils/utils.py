def reverse_string_slicing(s):
     return s[::-1]


def reverse_string_swap(s):
    s_list = list(s)
    for i in range(len(s_list)//2):
        s_list[i], s_list[len(s)-1 - i] = s_list

        return ''.join(s_list)