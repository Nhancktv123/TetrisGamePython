from colors import Colors
import pygame
from position import Position

# lớp này đại diện cho một khối trong game. Mỗi khối có thể có nhiều trạng thái quay (rotation states)
class Block:
    # khởi tạo một khối với ID, từ đó xác định màu sắc và loại khối. Các thuộc tính khác bao gồm kích thước ô, độ lệch hàng và cột, trạng thái quay, và mảng màu sắc
    def __init__(self, id):
        self.id = id
        self.cells = {}
        self.cell_size = 30
        self.row_offset = 0
        self.column_offset = 0
        self.rotation_state = 0
        self.colors = Colors.get_cell_colors()

    # di chuyển khối theo số lượng hàng và cột được chỉ định.
    def move(self, rows, columns):
        self.row_offset += rows
        self.column_offset += columns

    # lấy danh sách các vị trí (Position) của các ô trong khối hiện tại, có tính đến độ lệch của khối
    def get_cell_positions(self):
        tiles = self.cells[self.rotation_state]
        moved_tiles = []
        for position in tiles:
            position = Position(position.row + self.row_offset, position.column + self.column_offset)
            moved_tiles.append(position)
        return moved_tiles

    # xoay khối sang trạng thái quay tiếp theo
    def rotate(self):
        self.rotation_state += 1
        if self.rotation_state == len(self.cells):
            self.rotation_state = 0

    # hoàn tác việc xoay khối, trở về trạng thái quay trước đó
    def undo_rotation(self):
        self.rotation_state -= 1
        if self.rotation_state == -1:
            self.rotation_state = len(self.cells) - 1

    # vẽ khối lên màn hình Pygame
    def draw(self, screen, offset_x, offset_y):
         tiles = self.get_cell_positions()
         for tile in tiles:
             tile_rect = pygame.Rect(offset_x + tile.column * self.cell_size,
                                     offset_y + tile.row * self.cell_size, self.cell_size - 1, self.cell_size - 1)
             pygame.draw.rect(screen, self.colors[self.id], tile_rect)