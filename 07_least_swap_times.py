from typing import List


def least_swap_times(array: List[int]) -> int:
    # x_cnt: 0 的个数, y_cnt: 1 的个数
    x_cnt, y_cnt, array_len = 0, 0, len(array)
    for num in array:
        if num == 0:
            x_cnt += 1
    y_cnt = array_len - x_cnt

    left_cnt, right_cnt = 0, 0
    if x_cnt < y_cnt:
        for i in range(x_cnt):
            if array[i] == 0:
                left_cnt += 1
            if array[array_len - i - 1] == 0:
                right_cnt += 1
        return x_cnt - max(left_cnt, right_cnt)
    else:
        for i in range(y_cnt):
            if array[i] == 1:
                left_cnt += 1
            if array[array_len - i - 1] == 1:
                right_cnt += 1
        return y_cnt - max(left_cnt, right_cnt)


if __name__ == '__main__':
    case = [
        ([1, 1, 1, 1, 0, 1], 1),
        ([0, 1, 0, 0, 0, 0], 1),
        ([0], 0),
        ([1], 0),
        ([1, 1], 0),
        ([1, 0, 1, 0, 1, 0], 1)
    ]

    for c in case:
        assert c[1] == least_swap_times(c[0])
