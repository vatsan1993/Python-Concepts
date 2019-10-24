class Employee:


    def __init__(self, first, last, pay):
        self._first= first
        self._last=last
        self._pay= pay

    @property
    def last(self):
        return self._last

    @property
    def first(self):
        return self._first
    @property
    def fullname(self):
        return self.first+" "+self.last

    @property
    def pay(self):
        return self._pay

    @first.setter
    def first(self, first):
        self._first=first

    @last.setter
    def last(self, last):
        self._last=last

