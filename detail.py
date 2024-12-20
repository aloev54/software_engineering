class Detail:
    '''
    Класс деталь.
    Данный класс представляет сущность детали.
    Имеет следующие поля:
        - Код детали;
        - Адрес ячейки;
        - Количество деталей в ячейке.
    '''

    def __init__(self, code=None, address=None, count=None):
        self.detail_code = code #Код детали
        self.cell_address = address #Адрес ячейки
        self.cell_count = count #Количество в ячейке

    def __repr__(self):
        return f"Detail(code={self.detail_code}, cell={self.cell_address}, cell_count={self.cell_count})"