class Lamp(object):
    def __init__(self, on=False):
        self.on = on

    def turn_on(self):
        if self.on is False:
            self.on = True

    def turn_off(self):
        if self.on is True:
            self.on = False

    def toggle(self):
        self.on = not self.on
