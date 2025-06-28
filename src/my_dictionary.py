class my_dictionary(dict):
    """Dictionary that accumulates values for existing keys."""

    def __init__(self):
        super().__init__()

    def add(self, key, value):
        """Add ``value`` to ``key`` accumulating if key exists."""
        self[key] = self.get(key, 0) + value
