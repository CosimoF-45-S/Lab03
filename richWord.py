class RichWord:
    def __init__(self, parola):
        self._parola = parola
        self._corretta = None

    @property
    def parola(self):
        return self._parola

    @property
    def corretta(self):
        return self._corretta

    @corretta.setter
    def corretta(self, boolValue):
        self._corretta = boolValue

    def __str__(self):
        if self._corretta:
            return f"{self._parola} è corretta"
        else:
            return f"{self._parola} è sbagliata"
