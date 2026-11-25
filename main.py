import sys
import pygame as pg
from code.settings import WIDTH, HEIGHT, FPS, TITLE, BG_COLOR, LINE_COLOR, TXT_COLOR, GRID_MODES, LINE_DOWN_COLOR, current_mode_option, game_mode_option, FONT, SIZE_FONT
from code.game_logic import GameLogic

class Game:
    def __init__(self): # при запуске
        pg.init() # инициализация pg
        self.screen = pg.display.set_mode((WIDTH, HEIGHT), pg.RESIZABLE) # отрисовка окна
        pg.display.set_caption(TITLE) # вывод названия окна
        self.clock = pg.time.Clock() # отслеживание времени и FPS
        self.running = True # переключатель состояния игры
        self.font = pg.font.Font(FONT, SIZE_FONT)

        self.state = "MENU"

        # Режим игры (поле)
        self.current_mode = current_mode_option # размер поля
        self.game_mode = game_mode_option # Режим игры (PvP или PvE)
        self.apply_grid_settings()

        # Кнопки лаунчера
        self.btn_grid_rect = pg.Rect(0, 0, 300, 50)
        self.btn_mode_rect = pg.Rect(0, 0, 300, 50)
        self.btn_start_rect = pg.Rect(0, 0, 300, 60)

        # Логика
        self.game_logic = GameLogic()
        self.current_turn = "O" # кто начинает игру
    def apply_grid_settings(self):
        self.cell_size = GRID_MODES[self.current_mode]["cell_size"]
        self.line_count = GRID_MODES[self.current_mode]["line_count"]

    def run(self): # запускает бесконечный игровой цикл
        while self.running: # сам цикл
            self.handle_events() # проверка различных событий (того что нажал игрок)
            self.draw() # очищает окно каждый кадр
            self.clock.tick(FPS) # устанавливает лимит FPS

        pg.quit() # если переключатель выключается - выключает процессы pg
        sys.exit() # закрывает сам процесс программы


    def handle_events(self): # проверка событий (нажатий клавиш) в игре
        for event in pg.event.get(): # собирает список из всего что сделал игрок
            if event.type == pg.QUIT: # если закрывается окно, выключает игру
                self.running = False

            if self.state == "MENU":
                self.handle_events_menu(event)
            elif self.state == "GAME":
                self.handle_events_game(event)

    def handle_events_menu(self, event):  # проверка событий (нажатий клавиш) в меню
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:  # ЛКМ
            mouse_pos = event.pos

            if self.btn_grid_rect.collidepoint(mouse_pos):
                modes = list(GRID_MODES.keys())
                next_index = (modes.index(self.current_mode) + 1) % len(modes)
                self.current_mode = modes[next_index]
                self.apply_grid_settings()

            elif self.btn_mode_rect.collidepoint(mouse_pos):
                self.game_mode = "PvE" if self.game_mode == "PvP" else "PvP"

            elif self.btn_start_rect.collidepoint(mouse_pos):
                self.game_logic.reset(self.current_mode)
                self.state = "GAME"

    def handle_events_game(self, event):  # проверка событий (нажатий клавиш) в игре
        if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            self.state = "MENU"

    def update(self): # логика игры (победы, ходы)
        pass

    def make_bot_move(self): # свзязь между файлом ИИ и кодом
        pass

    def draw_menu(self): # рисует меню
        current_w, current_h = self.screen.get_size()  # реальные размеры окна
        center_x = current_w // 2

        self.btn_grid_rect.center = (center_x, current_h // 2 - 80)
        self.btn_mode_rect.center = (center_x, current_h // 2)
        self.btn_start_rect.center = (center_x, current_h // 2 + 100)

        title_surf = self.font.render("НАСТРОЙКИ ИГРЫ", True, TXT_COLOR)
        self.screen.blit(title_surf, title_surf.get_rect(center=(center_x, current_h // 2 - 170)))

        def draw_button(rect, text, color, color_txt):
            pg.draw.rect(self.screen, color, rect, border_radius=10)
            pg.draw.rect(self.screen, LINE_COLOR, rect, width=3, border_radius=10)
            txt_surf = self.font.render(text, True, color_txt)
            self.screen.blit(txt_surf, txt_surf.get_rect(center=rect.center))

        draw_button(self.btn_grid_rect, f"Поле: {self.current_mode}x{self.current_mode}", BG_COLOR, TXT_COLOR)
        draw_button(self.btn_mode_rect, f"Режим: {self.game_mode}", BG_COLOR, TXT_COLOR)
        draw_button(self.btn_start_rect, "ИГРАТЬ", LINE_DOWN_COLOR, TXT_COLOR)

    def draw_grid(self): # рисует игровую сетку в зависимости от режима
        current_w, current_h = self.screen.get_size() # реальные размеры окна
        min_size_window = min(current_w, (current_h - 100)) # вычисляет меньшую сторону окна, с учетом того что нужно оставить 100 px в высоте для отрисовки интерфейса
        middle_width_window = (current_w - min_size_window) // 2 # сколько нужно прибавить к координате x для центрирования в окне
        current_cell_size = (min_size_window - 50) // self.cell_size

        for i in range(1, self.line_count + 1): # отрисовывает линии сетки, исходя из размера поля
            pos = (i * current_cell_size) + 25 # координата для отрисовки линий внутри игрового поля от размера поля
            pg.draw.line(self.screen, LINE_COLOR, (middle_width_window + pos, 25), (middle_width_window + pos, min_size_window - 25), 5) # отрисовка горизонтальных линий
            pg.draw.line(self.screen, LINE_COLOR, (middle_width_window + 25, pos), (middle_width_window + min_size_window - 25, pos), 5) # отрисовка вертикальных линиий

        pg.draw.line(self.screen, LINE_DOWN_COLOR, (middle_width_window + 10, min_size_window), (middle_width_window + min_size_window - 10, min_size_window), 5) # отрисовка нижней линии для разделения интерфеса и поля

    def draw_player_cell(self): # рисует обводку ячейки для выбора куда поставить 0 и X
        pass

    def draw(self): # визуализация игры (окно)
        self.screen.fill(BG_COLOR) # очищает все что было в окне, и заливает всё цветом "BG_COLOR" (происходит в скрытом холсте (двойная буферизация)
        if self.state == "MENU":
            self.draw_menu()
        elif self.state == "GAME":
            self.draw_grid() # отрисовывает сетку
            self.draw_player_cell() # отрисовка обводки ячейки
        pg.display.flip() # выводит изображение из скрытого холста в видимый


# запуск игры
if __name__ == "__main__": # проверяет что файл (игра) запущена непосредственно пользователем
    game = Game() # создание объекта для класса Game()
    game.run() # включается бесконечный цикл