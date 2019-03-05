import math

class Presenter:
    def __init__(self, total):
        self.total = total
        self.current = 0
    def present(self):
        self.current += 1
        current = self.current / self.total * 100
        progress = u'\u275a'
        count = math.floor(current / 10)
        for _ in range(count):
            progress += '\u275a\u275a'
        print(progress + "%.2f" % round(current,2) + "%", end="\r")