from code.settings import current_mode_option

class GameLogic:
    def __init__(self):
        # Битборды
        self.bitboard_0 = 0
        self.bitboard_x = 0

        # Очки
        self.score_0 = 0
        self.score_x = 0

    def cell_check(self, position):
        mask = 1 << position
        return not (bool(mask & self.bitboard_x)) or (bool(mask and self.bitboard_0))

    def set_bitboard(self, name, position):
        pass