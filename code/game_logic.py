from code.settings import current_mode_option

class GameLogic:
    def __init__(self):
        # Битборды
        self.bitboard_0 = 0
        self.bitboard_x = 0

        # Очки
        self.score_0 = 0
        self.score_x = 0

        # Win Комбинации
        self.win_combinations = {
            "31": [
                0b000000111,
                0b000111000,
                0b111000000,

                0b001001001,
                0b010010010,
                0b100100100,

                0b100010001,
                0b001010100
            ]
        }

    # Проверка занятости
    def cell_check(self, position):
        mask = 1 << position
        return not (bool(mask & self.bitboard_x)) or (bool(mask & self.bitboard_0))

    # Установить бит
    def set_bitboard(self, name, position):
        if self.cell_check(position):
            mask = 1 << position
            if name == "0":
                self.bitboard_0 |= mask
            if name == "x":
                self.bitboard_x |= mask

    # Проверка победы
    def win_check(self, igra):
        combinations = self.win_combinations[igra]
        if igra == "31":
            for i in range(len(combinations)):
                mask = combinations[i]
                if (self.bitboard_x & mask) == mask: # победа x
                    return "x"
                if (self.bitboard_0 & mask) == mask: # победа 0
                    return "0"
            return "n" # без побед