"""
Ömer Ammura - 234210074
Emad CheikhElichreh - 224210087
Mohammad nikpour -  234210005
Eldar Semnov - 224210122
"""


class Visitor:
    def __init__(self, name, age, visitor_type,preferences= None):
        self.name = name
        self.age = age
        self.visitor_type = visitor_type
        self.preferences = preferences