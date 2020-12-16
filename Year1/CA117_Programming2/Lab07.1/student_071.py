class Student(object):
    def __init__(self, surname, forename, sid, modlist=None):
        self.sid = sid
        self.surname = surname
        self.forename = forename
        self.modlist = modlist

    def add_module(self, s):
        if self.modlist is None:
            self.modlist = []
        if s not in self.modlist:
            self.modlist.append(s)

    def del_module(self, s):
        if s in self.modlist:
            self.modlist.remove(s)

    def print_details(self):
        print("ID:", self.sid)
        print("Surname:", self.surname)
        print("Forename:", self.forename)
        print("Modules:", *self.modlist)
