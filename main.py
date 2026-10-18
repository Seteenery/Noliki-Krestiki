import sys
import pygame as pg
from code.settings import WIDTH, HEIGHT, FPS, TITLE, BG_COLOR

class Game:
    def __init__(self): # при запуске
        pg.init() # инициализация pg
        self.screen = pg.display.set_mode((WIDTH, HEIGHT)) # отрисовка дисплея
        pg.display.set_caption(TITLE) # вывод названия окна
        self.clock = pg.time.Clock() # отслеживание времени и FPS
        self.running = True # переключатель состояния игры

    def run(self): # запускает бесконечный игровой цикл
        while self.running: # сам цикл
            self.handle_events() # проверка различных событий (того что нажал игрок)
            self.draw() # очищает окно каждый кадр
            self.clock.tick(FPS) # устанавливает лимит FPS
        pg.quit() # если переключатель выключается - выключает процессы pg
        sys.exit() # закрывает сам процесс программы

    def handle_events(self): # проверка событий (нажатий клавиш)
        for event in pg.event.get(): # собирает список из всего что сделал игрок
            if event.type == pg.QUIT: # если закрывается окно, выключает игру
                self.running = False

    def update(self): # логика игры (победы, ходы)
        pass

    def draw(self): # визуализация игры (окно)
        self.screen.fill(BG_COLOR) # очищает все что было в окне, и заливает всё цветом "BG_COLOR" (происходит в скрытом холсте (двойная буферизация)
        pg.display.flip() # сразу выводит изображение из скрытого холста в видимый


# запуск игры
if __name__ == "__main__": # проверяет что файл (игра) запущена непосредственно пользователем
    game = Game() # создание объекта для класса Game()
    game.run() # включается бесконечный цикл