from collections import namedtuple

Module = namedtuple('Module', ['code', 'title', 'ects'])

CA1_MODULES = {'CA103': Module('CA103', 'Computer Systems', 5),
               'CA106': Module('CA106', 'Web Design', 5),
               'CA115': Module('CA115', 'Digital Innovation', 5),
               'CA116': Module('CA116', 'Computer Programming I', 10),
               'CA117': Module('CA117', 'Computer Programming II', 10),
               'CA169': Module('CA169', 'Networks and Internet', 5),
               'CA170': Module('CA170', 'Operating Systems', 5),
               'CA172': Module('CA172', 'Problem Solving', 5),
               'MS121': Module('MS121', 'IT Mathematics', 10)}

class Student(object):

    def __init__(self, idnum, surname, firstname):
        self.idnum = idnum
        self.surname = surname
        self.firstname = firstname
        self.mods = CA1_MODULES
        self.marks = {code: 0 for code in self.mods.keys()}

    def __str__(self):
        name = '{} : {} {}'.format(self.idnum,
                                   self.firstname,
                                   self.surname)
        uline = '-' * len(name)
        results = '\n'.join([code + ' : ' + self.mods[code].title + ' : ' + str(self.marks[code]) for code in sorted(self.mods.keys())])
        pm = 'Precision mark: {:.2f}'.format(self.precision_mark())
        if self.passed():
            outcome = 'Pass'
        elif self.passed_by_compensation():
            outcome = 'Pass by compensation'
        else:
            outcome = 'Fail'

        return '\n'.join([name, uline, results, pm, outcome])

    def add_mark(self, name, mark):
        self.marks[name] = mark

    def precision_mark(self):
        weighted = [self.mods[code].ects * self.marks[code] for code in self.mods]
        return sum(weighted) / sum([self.mods[code].ects for code in self.mods])

    def passed(self):
        return all(self.marks[code] > 40 for code in self.mods)

    def passed_by_compensation(self):
        if self.precision_mark() < 0.45:
            return False
        total = sum([self.mods[code].ects for code in self.mods])
        creds_failed = sum([self.mods[code].ects for code in self.mods if self.marks[code] < 40])
        if creds_failed / total > 1 / 6:
            return False

        if any([self.marks[code] < 35 for code in self.mods]):
            return False

         return True
