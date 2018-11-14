#objects which are stored in organized

from abc import ABC, abstractmethod

class item(ABC):

    def __init__ (self, priority, title):
        self.title = title
        self.priority = priority

    def __str__ (self):
            return self.title + 'Prio: ' + str(self.priority)

    @abstractmethod
    def prt (self):
        pass

class note(item):

    def __init__ (self, priority, title, desc):
        super().__init__(priority, title)
        self.type = 'NOTE'
        self.desc = desc

    def __str__(self):
        return self.type + ' ' + self.title + ' Prio ' + str(self.priority) + ' ' + self.desc

    def prt(self):
        pass

class vcard(item):

    def __init__ (self, priority, title, pict):
        super().__init__(priority, title)
        self.type = 'VCARD'
        self.picture = picture

    def __str__ (self):
        self.type + ' ' + self.title + ' Prio ' + str(self.priority) + ' ' + self.picture
