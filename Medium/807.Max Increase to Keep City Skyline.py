class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        解题思路：
        1. 求出从上方或下方看天际线时建筑物的高度，得到一个一维数组row_max_list
        2. 求出从左侧或右侧看天际线时建筑物的高度，得到一个一维数组col_max_list
        3. 最终得到的二维数组其实是求min(max(所在行)，max(所在列))
        4. 初始化一个height_add=0
        5. min(max(所在行)，max(所在列))-grid[i][j]得到每个建筑物增加高度，累加之后就得到了增加的总高度

        :param grid:二维数组，每个数字代表该位置建筑物的高度
        :return:建筑物增加的高度
        """
        row_max_list = []
        for row in grid:
            row_max_list.append(max(row))
        col_max_list = []
        for j in range(len(grid[0])):
            one_list = []
            for i in range(len(grid)):
                one_list.append(grid[i][j])
            col_max_list.append(max(one_list))
        height_add = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                height_add += min(row_max_list[i], col_max_list[j])-grid[i][j]
        return height_add


if __name__ == "__main__":
    grid = [[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]
    print(Solution().maxIncreaseKeepingSkyline(grid))
