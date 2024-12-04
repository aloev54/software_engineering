class Detail:
    '''
    Данный класс представляет сущность детали
    '''

    def __init__(self, code=None, address=None, count=None):
        self.detail_code = code #Код детали
        self.cell_address = address #Адрес ячейки
        self.cell_count = count #Количество в ячейке
