def solution(nums):
    sorted_nums = nums.copy()
    sorted_nums.sort()
    index_list = []
    for i in range(len(nums)):
        if nums[i] != sorted_nums[i]:
            index_list.append(i)

    if not index_list:
        return 0
    else:
        return index_list[-1] - index_list[0] + 1


if __name__ == '__main__':
    nums = [2, 6, 4, 8, 10, 9, 15]
    solution(nums) == 5
