class Visitor:
    def __init__(self, name, age, visitor_type,preferences= None):
        self.name = name
        self.age = age
        self.visitor_type = visitor_type
        self.preferences = preferences