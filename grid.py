import pygame
from colors import Colors

# lớp này đại diện cho lưới của game
class Grid:
    # phương thức init khởi tạo đối tượng lưới
    def __init__(self):
        # lưới này có 20 hàng và 10 cột
        self.num_rows = 20
        self.num_cols = 10
        self.cell_size = 30 # size từng ô (pixel)
        # tạo lưới với các giá trị ban đầu là 0 (nghĩa là ô trống)
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]
        # self.grid = [
        #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        # ]
        # lấy màu cho các ô từ lớp Colors
        self.colors = Colors.get_cell_colors()

    # in ra lưới hiện tại trong console
    def print_grid(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                print(self.grid[row][column], end=" ")
            print()

    # kiểm tra xem một vị trí (hàng, cột) có nằm trong lưới hay không (không cho khối đi ra ngoài lưới)
    def is_inside(self, row, column):
        if row >= 0 and row < self.num_rows and column >= 0 and column < self.num_cols:
            return True
        return False

    # kiểm tra xem một ô trong lưới có trống (giá trị là 0) hay không
    def is_empty(self, row, column):
        if self.grid[row][column] == 0:
            return True
        return False

    # kiểm tra xem một hàng trong lưới có đầy (không còn ô trống) hay không
    def is_row_full(self, row):
        for column in range(self.num_cols):
            if self.grid[row][column] == 0:
                return False
        return True

    # xóa toàn bộ các ô trong một hàng (đặt giá trị về 0)
    def clear_row(self, row):
        for column in range(self.num_cols):
            self.grid[row][column] = 0

    # di chuyển một hàng xuống dưới một số hàng nhất định
    def move_row_down(self, row, num_rows):
        for column in range(self.num_cols):
            self.grid[row + num_rows][column] = self.grid[row][column]
            self.grid[row][column] = 0

    # xóa tất cả các hàng đã đầy và di chuyển các hàng phía trên xuống dưới
    def clear_full_rows(self):
        completed = 0
        for row in range(self.num_rows-1, 0, -1):
            if self.is_row_full(row):
                self.clear_row(row)
                completed += 1
            elif completed > 0:
                self.move_row_down(row, completed)
        return completed

    # đặt lại toàn bộ lưới về trạng thái ban đầu (tất cả các ô đều trống)
    def reset(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                self.grid[row][column] = 0

    # vẽ lưới lên màn hình Pygame
    def draw(self, screen):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                cell_value = self.grid[row][column]
                cell_rect = pygame.Rect(column*self.cell_size + 11, row*self.cell_size + 11,
                                        self.cell_size - 1, self.cell_size - 1) #pygame.Rect(x, y, w, h)
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect) #(surface, color, rect)