class Detail:
    '''
    Данный класс представляет сущность детали
    '''

    def __init__(self, code=None, address=None, count=None):
        self.detail_code = code
        self.cell_address = address
        self.cell_count = count
