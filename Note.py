class Note:
    def __init__(self, name, sname, number, bdate):
        self.name = name
        self.sname = sname
        self.number = number
        self.bdate = bdate
        self.next = None
    def __eq__(self, other):
        if other:
            return self.name==other.name and self.sname==other.sname\
            and self.number==other.number and self.bdate==other.bdate
