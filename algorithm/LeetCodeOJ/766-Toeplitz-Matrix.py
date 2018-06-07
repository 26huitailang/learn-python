def solution(matrix):
    """访问宽和高的一边的元素，以及他们对应的对角线上的元素"""
    rows = len(matrix)
    columns = len(matrix[0])
    if rows == 1:
        return True
    if columns == 1:
        return True
    line_vertical = [(x, 0) for x in range(rows)]
    line_horizontal = [(0, x) for x in range(1, columns)]  # 不要重复使用第一个元素
    print(line_horizontal, line_vertical)

    for point in line_vertical:
        point_value = matrix[point[0]][point[1]]
        for i in range(1, rows - point[0]):  # 这条line有多少个元素
            if i + 1 > columns:
                break
            if point_value != matrix[point[0]+i][point[1]+i]:
                return False

    for point in line_horizontal:
        point_value = matrix[point[0]][point[1]]
        for i in range(1, columns - point[1]):  # 这条line有多少个元素
            print(i)
            if i + 1 > rows:
                break
            if point_value != matrix[point[0]+i][point[1]+i]:
                return False
    return True

if __name__ == '__main__':
    matrix_items = [
            [[1,2,3,4],[5,1,2,3],[9,5,1,2]],
            [[1,2],[2,2]],
            [[65, 98, 57]],
            [[11,74,7,93],[40,11,74,7]],
            [[87]],
            ]
    solution(matrix_items[0]) == True
    solution(matrix_items[1]) == False
    solution(matrix_items[2]) == True
    solution(matrix_items[3]) == True
    solution(matrix_items[4]) == True

"""good one
for i in range(0,len(matrix)-1):
    if matrix[i][:-1] != matrix[i+1][1:]:
        return False
return True
"""
