class Checkpoints:
    def __init__(self):
        self._checkpoints = {}

    def __getitem__(self, page_number: int):
        return self._checkpoints[str(page_number)]

    def __setitem__(self, page_number: int, data: dict):
        self._checkpoints[str(page_number)] = data

    def __repr__(self):
        return self._checkpoints.__repr__()

    @property
    def is_empty(self):
        return not self._checkpoints
