class List(list):
    _index_from = 0
    
    def set_index_from(self, index):
        self._index_from = index

    def __getitem__(self, index):
        if type(index) is slice:
            return super().__getitem__(index)
        else:
            if self._index_from + index > len(self):
                return super().__getitem__(self._index_from)

            return super().__getitem__(self._index_from + index)
