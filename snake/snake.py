import pygame
import random

# Inisialisasi Pygame dan mengatur tampilan
pygame.init()
width, height = 1500, 1000
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

# Warna dan ukuran objek
snake_block = 20
snake_speed = 10
snake_color = (0, 255, 0)
fruit_color = (255, 0, 0)

# Fungsi untuk menggambar ular
def draw_snake(snake_positions):
    for pos in snake_positions:
        pygame.draw.rect(screen, snake_color, pygame.Rect(pos[0], pos[1], snake_block, snake_block))

# Fungsi untuk menghasilkan posisi buah
def spawn_fruit():
    return [random.randint(0, (width - snake_block) // snake_block) * snake_block,
            random.randint(0, (height - snake_block) // snake_block) * snake_block]

def show_game_over(score):
    font = pygame.font.Font(None, 74)
    text = font.render("Game Over!", True, (255, 0, 0))
    screen.blit(text, (width // 2 - text.get_width() // 2, height // 2 - text.get_height() // 2))
    
    font = pygame.font.Font(None, 36)
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (width // 2 - score_text.get_width() // 2, height // 2 + 50))
    
    restart_text = font.render("Press R to Restart or Q to Quit", True, (255, 255, 255))
    screen.blit(restart_text, (width // 2 - restart_text.get_width() // 2, height // 2 + 100))
    
    pygame.display.flip()

    # Menunggu input dari pemain
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    waiting = False  # Restart permainan
                elif event.key == pygame.K_q:
                    pygame.quit()
                    exit()

def main():
    while True:
        snake_positions = [[100, 100]]
        direction = (1, 0)  # Arah awal (kanan)
        fruit_position = spawn_fruit()
        score = 0

        while True:
            screen.fill((0, 0, 0))
            pygame.draw.rect(screen, fruit_color, pygame.Rect(fruit_position[0], fruit_position[1], snake_block, snake_block))
            
            # Menangani event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and direction != (0, 1):
                        direction = (0, -1)
                    elif event.key == pygame.K_DOWN and direction != (0, -1):
                        direction = (0, 1)
                    elif event.key == pygame.K_LEFT and direction != (1, 0):
                        direction = (-1, 0)
                    elif event.key == pygame.K_RIGHT and direction != (-1, 0):
                        direction = (1, 0)

            # Menggerakkan ular
            new_head = [snake_positions[0][0] + direction[0] * snake_block, 
                        snake_positions[0][1] + direction[1] * snake_block]
            
            # Cek tabrakan dengan dinding
            if (new_head[0] < 0 or new_head[0] >= width or 
                new_head[1] < 0 or new_head[1] >= height or 
                new_head in snake_positions):
                show_game_over(score)  # Tampilkan Game Over
                break  # Keluar dari loop permainan

            snake_positions.insert(0, new_head)

            # Cek apakah ular memakan buah
            if new_head == fruit_position:
                score += 1
                fruit_position = spawn_fruit()  # Buat buah baru
            else:
                snake_positions.pop()  # Hapus ekor ular jika tidak memakan buah

            draw_snake(snake_positions)

            # Menampilkan skor
            font = pygame.font.Font(None, 36)
            score_text = font.render("Score: " + str(score), True, (255, 255, 255))
            screen.blit(score_text, (10, 10))

            pygame.display.flip()
            clock.tick(snake_speed)

if __name__ == "__main__":
    main()