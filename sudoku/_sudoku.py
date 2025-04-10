def possibleNumberInference(grid):
    # 初始化候选值集
    result = [[0 for _ in range(9)] for _ in range(9)]
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell != 0:
                result[i][j] = {cell}
            else:
                result[i][j] = set(range(1,10))
    # 循环推理
    new_value = True
    while(new_value):            
        new_value = False
        for i, row in enumerate(result):
            for j, cell in enumerate(row):
                if len(cell) != 1:
                    # 获取当前单元格的候选值
                    candidates = cell.copy()
                    # 检查行
                    for k in range(9):
                        if k != j and len(result[i][k]) == 1:
                            candidates -= result[i][k]
                    # 检查列
                    for k in range(9):
                        if k != i and len(result[k][j]) == 1:
                            candidates -= result[k][j]
                    # 检查宫格
                    box_row = i // 3 * 3
                    box_col = j // 3 * 3
                    for k in range(box_row, box_row + 3):
                        for l in range(box_col, box_col + 3):
                            if (k != i or l != j) and len(result[k][l]) == 1:
                                candidates -= result[k][l]
                    if cell != candidates:
                        new_value = True
                        result[i][j] = candidates
    
    return result 

def lastRemainingCellInference(grid):
    # 初始化结果集（深拷贝原始网格）
    result = [row[:] for row in grid]
    # 循环推理
    # 遍历数字1-9，对每个数字，检查每个宫格中是否存在该数字
    # 若不存在，检查宫格的行，列方向，排除掉不可填写该数字的单元格
    # 若最后只剩余一个可填写的单元格，则填写该数字
    changed = True
    while changed:
        changed = False
        
        # 遍历数字1-9
        for num in range(1, 10):
            # 检查每个3x3宫格
            for box_row in range(0, 9, 3):
                for box_col in range(0, 9, 3):
                    # 检查该数字是否已在宫格中存在
                    num_exists = False
                    for i in range(box_row, box_row + 3):
                        for j in range(box_col, box_col + 3):
                            if result[i][j] == num:
                                num_exists = True
                                break
                        if num_exists:
                            break
                    
                    if num_exists:
                        continue  # 数字已存在，跳过该宫格
                    
                    # 记录可填位置
                    possible_positions = []
                    
                    # 检查宫格内每个空单元格
                    for i in range(box_row, box_row + 3):
                        for j in range(box_col, box_col + 3):
                            if result[i][j] == 0:  # 只检查空单元格
                                # 检查行方向是否可填
                                row_valid = True
                                for k in range(9):
                                    if result[i][k] == num:
                                        row_valid = False
                                        break
                                
                                # 检查列方向是否可填
                                col_valid = True
                                for k in range(9):
                                    if result[k][j] == num:
                                        col_valid = False
                                        break
                                
                                if row_valid and col_valid:
                                    possible_positions.append((i, j))
                    
                    # 如果只剩一个可填位置
                    if len(possible_positions) == 1:
                        i, j = possible_positions[0]
                        result[i][j] = num
                        changed = True
                        print(f"Filled number {num} at position ({i}, {j})")
    
    return result

#测试用例
if __name__ == "__main__":
    grid1 = [
        [2, 0, 0, 0, 7, 0, 0, 3, 8],
        [0, 0, 0, 0, 0, 6, 0, 7, 0],
        [3, 0, 0, 0, 4, 0, 6, 0, 0],
        [0, 0, 8, 0, 2, 0, 7, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 7, 0, 3, 0, 4, 0, 0],
        [0, 0, 4, 0, 8, 0, 0, 0, 9],
        [0, 6, 0, 4, 0, 0, 0, 0, 0],
        [9, 1, 0, 0, 6, 0, 0, 0, 2],
    ]
    grid2 = [
        [0, 7, 0, 4, 0, 8, 0, 2, 9],
        [0, 0, 2, 0, 0, 0, 0, 0, 4],
        [8, 5, 4, 0, 2, 0, 0, 0, 7],
        [0, 0, 8, 3, 7, 4, 2, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 2, 6, 1, 7, 0, 0],
        [0, 0, 0, 0, 9, 3, 6, 1, 2],
        [2, 0, 0 ,0 ,0, 0, 4, 0, 3],
        [1, 3, 0, 6, 4, 2, 0, 7, 0],
    ]
    grid3 = [
        [0, 0, 0, 0, 0, 4, 1, 0, 3],
        [0, 0, 6, 0, 8, 0, 0, 4, 0],
        [1, 0, 0, 0, 3, 9, 0, 0, 0],
        [3, 4, 5, 9, 0, 7, 0, 8, 2],
        [0, 6, 7, 4, 2, 0, 0, 0, 1],
        [0, 1, 0, 5, 6, 0, 0, 0, 0],
        [6, 2, 1, 8, 9, 0, 0, 0, 0],
        [4, 9, 0, 3, 0, 0, 2, 1, 5],
        [0, 7, 3, 1, 4, 0, 9, 0, 8],
    ]
    
    print("Possible Number Inference Result for grid2:")
    result = possibleNumberInference(grid2)
    for line in result:
        print(line)
    print("\nLast Remaining Cell Inference Result for grid1:")
    result = lastRemainingCellInference(grid1)
    for line in result:
        print(line)