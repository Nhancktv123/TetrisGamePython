import pygame, sys
from game import Game
from colors import Colors

pygame.init()

# cài đặt font chữ và các bề mặt hiển thị văn bản
title_font = pygame.font.Font(None, 40)  # Font chữ cho tiêu đề
score_surface = title_font.render("Score", True, Colors.white)
next_surface = title_font.render("Next", True, Colors.white)
game_over_surface = title_font.render("GAME OVER", True, Colors.white)

# tạo các hình chữ nhật (rect) để chứa điểm số và xem trước khối tiếp theo
score_rect = pygame.Rect(320, 55, 170, 60)
next_rect = pygame.Rect(320, 215, 170, 180)

# tạo màn hình chơi game với kích thước 500x620 pixel
screen = pygame.display.set_mode((500, 620))
pygame.display.set_caption("Python Tetris")

# clock điều khiển tốc độ khung hình của game, đảm bảo game chạy mượt mà
clock = pygame.time.Clock()

# khởi tạo đối tượng Game
game = Game()

# để cập nhật trò chơi mỗi 250ms, giúp khối rơi tự động
GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 250)

while True:
    # xử lý các sự kiện
    for event in pygame.event.get():
        # nếu người dùng đóng cửa sổ
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # xử lý sự kiện nhấn phím
        if event.type == pygame.KEYDOWN:
            # nếu game kết thúc và người dùng nhấn phím bất kỳ, reset game
            if game.game_over == True:
                game.game_over = False
                game.reset()

            if event.key == pygame.K_LEFT and game.game_over == False:
                game.move_left() # di chuyển khối sang trái

            if event.key == pygame.K_RIGHT and game.game_over == False:
                game.move_right() # di chuyển khối sang phải

            if event.key == pygame.K_DOWN and game.game_over == False:
                game.move_down() # di chuyển khối xuống dưới
                game.update_score(0, 1) # tăng điểm khi khối được di chuyển xuống

            if event.key == pygame.K_UP and game.game_over == False:
                game.rotate() # xoay khối

        # cập nhật game khi sự kiện GAME_UPDATE xảy ra
        if event.type == GAME_UPDATE and game.game_over == False:
            game.move_down()

    # vẽ các thành phần lên màn hình
    score_value_surface = title_font.render(str(game.score), True, Colors.white) # Hiển thị điểm

    screen.fill(Colors.dark_blue) # tô màu nền cho màn hình
    screen.blit(score_surface, (365, 20, 50, 50)) # vẽ tiêu đề "Score" lên màn hình
    screen.blit(next_surface, (375, 180, 50, 50)) # vẽ tiêu đề "Next" lên màn hình

    # nếu game kết thúc, hiển thị "GAME OVER"
    if game.game_over == True:
        screen.blit(game_over_surface, (320, 450, 50, 50))

    # vẽ hình chữ nhật và điểm số
    pygame.draw.rect(screen, Colors.light_blue, score_rect, 0, 10) # vẽ HCN cho khu vực điểm số
    screen.blit(score_value_surface, score_value_surface.get_rect(centerx = score_rect.centerx,
        centery = score_rect.centery)) # vẽ điểm số
    pygame.draw.rect(screen, Colors.light_blue, next_rect, 0, 10) # vẽ HCN cho khu vực xem khối tiếp theo
    game.draw(screen) # vẽ toàn bộ trạng thái game lên màn hình

    # cập nhật màn hình hiển thị
    pygame.display.update()

    # điều khiển tốc độ khung hình
    clock.tick(60) # 60fps
