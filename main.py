import sys
import pygame as pg
from code.settings import WIDTH, HEIGHT, FPS, TITLE, BG_COLOR, LINE_COLOR, GRID_MODES, Game_Grid, LINE_DOWN_COLOR

class Game:
    def __init__(self): # при запуске
        pg.init() # инициализация pg
        self.screen = pg.display.set_mode((WIDTH, HEIGHT)) # отрисовка окна
        pg.display.set_caption(TITLE) # вывод названия окна
        self.clock = pg.time.Clock() # отслеживание времени и FPS
        self.running = True # переключатель состояния игры

        # Режим игры (поле)
        self.current_mode = 4  # размер поля
        self.cell_size = GRID_MODES[self.current_mode]["cell_size"]
        self.line_count = GRID_MODES[self.current_mode]["line_count"]

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

    def draw_grid(self): # рисует игровую сетку в зависимости от режима
        for i in range(1, self.line_count):
            pos = (i * self.cell_size) + 25 # координата для отрисовки линий внутри игрового поля от размера поля
            pg.draw.line(self.screen, LINE_COLOR, (25, pos), ((WIDTH - 25), pos), 5) # отрисовка горизонтальных линий
            pg.draw.line(self.screen, LINE_COLOR, (pos, 25), (pos, (WIDTH - 25)), 5) # отрисовка вертикальных линиий

        pg.draw.line(self.screen, LINE_DOWN_COLOR, (5, WIDTH), ((WIDTH - 5), WIDTH), 5) # отрисовка нижней линии для разделения интерфеса и поля



    def draw(self): # визуализация игры (окно)
        self.screen.fill(BG_COLOR) # очищает все что было в окне, и заливает всё цветом "BG_COLOR" (происходит в скрытом холсте (двойная буферизация)
        self.draw_grid() # отрисовывает сетку
        pg.display.flip() # выводит изображение из скрытого холста в видимый


# запуск игры
if __name__ == "__main__": # проверяет что файл (игра) запущена непосредственно пользователем
    game = Game() # создание объекта для класса Game()
    game.run() # включается бесконечный цикл