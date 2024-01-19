import pygame
import sys
import time

# Инициализация pygame
pygame.init()

# Создание окна
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

# Загрузка изображения
image = pygame.image.load('test.png')

# Начальная прозрачность
alpha = 0
start_num = 0.1

# Главный цикл программы
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Установка прозрачности изображения
    image.set_alpha(alpha)

    # Отрисовка изображения на экране
    screen.fill((255, 255, 255))  # Очистка экрана
    screen.blit(image, (0, 0))    # Отображение изображения

    # Обновление экрана
    pygame.display.flip()

    if start_num != 10:
        start_num = (start_num / 2) + 5
        alpha = start_num * 25.5
        image.set_alpha(alpha)
        time.sleep(0.1)
    else:
        print("\rend", end='')

    # Задержка для управления скоростью изменения прозрачности
    pygame.time.delay(10)

# Завершение работы pygame
pygame.quit()
sys.exit()