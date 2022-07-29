class game_place:
    """ Класс который содержит в себе состояние игрового поля.
    список place_cros[] содержит словари которые представляют все диагонали.
    {'1-1': 0... - ячейка 1-нолик, 10-крестикб 0-пусто"""
    place_cros = []

    # реализуем все диагонали в списке
    # 1 - нолик, 10-крестик 0-пусто
    def __init__(self):
        # горизонтали
        self.place_cros.append({'1-1': 0, '1-2': 0, '1-3': 0})
        self.place_cros.append({'2-1': 0, '2-2': 0, '2-3': 0})
        self.place_cros.append({'3-1': 0, '3-2': 0, '3-3': 0})
        # вертикали
        self.place_cros.append({'1-1': 0, '2-1': 0, '3-1': 0})
        self.place_cros.append({'2-1': 0, '2-2': 0, '2-3': 0})
        self.place_cros.append({'3-1': 0, '3-2': 0, '3-3': 0})
        # диагонали
        self.place_cros.append({'1-1': 0, '2-2': 0, '3-3': 0})
        self.place_cros.append({'3-1': 0, '2-2': 0, '1-3': 0})

    def ver_game_state(self):
        """ Определение статуса игры. возвращает строковое значение, кто победил, игра не начата, игра идет"""
        sum_all = 0
        str_out = ''
        #перебираем васть список пересечений
        for i, v in enumerate(self.place_cros):
            sum_cros = 0
            #в каждом пересечении суммируем ячейки
            for k, val in v.items():
                sum_cros += val
                sum_all += val
            if sum_cros == 3:
                str_out = 'Победили нолики'
                break
            elif sum_cros == 30:
                str_out = 'Победили крестики'
                break

        if sum_all == 0:
            str_out = 'Игра не начата'
        else:
            str_out = 'Идет игра'

        return str_out
