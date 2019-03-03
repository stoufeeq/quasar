import numpy as np


class arrayTraverse():
    def __init__(self):
        self.val = 0
        self.path = [i_a[0][0]]
        self.row_max = np.shape(i_a)[0] - 1
        self.col_max = np.shape(i_a)[1] - 1

    def down(self, inp_arr, i, j):
        if i < self.row_max:
            return inp_arr[i+1][j]
        else:
            return 0

    def right(self, inp_arr, i, j):
        if j < self.col_max:
            return inp_arr[i][j+1]
        else:
            return 0

    def traverse_arr(self, inp_arr, i, j):
        print(inp_arr[i:,j:])
        if self.down(inp_arr, i, j) > self.right(inp_arr, i, j):
            print("down we go", "new i:", i+1, "j: ", j, inp_arr[i+1][j])
            self.path.append(inp_arr[i+1][j])
            self.traverse_arr(inp_arr, i+1, j)
        elif self.down(inp_arr, i, j) < self.right(inp_arr, i, j):
            print("right we go", "i:", i, "new j: ", j+1, inp_arr[i][j+1])
            self.path.append(inp_arr[i][j+1])
            self.traverse_arr(inp_arr, i, j+1)


i_a = np.array([[1,2,3,1,5],[4,9,6,4,3],[7,8,9,8,10],[3,4,5,1,9],[3,4,5,6,1]])
tr = arrayTraverse()
tr.traverse_arr(i_a, 0, 0)
print(tr.path)