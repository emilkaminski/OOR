#definition of organized class

from oclasses.items import note

class organizer (object):

    def __init__ (self, name, size, pages):

        self.name = name
        self.size = size
        self.pages = pages

        self.actions_que = {
            '1':self.new_note,
            '2':self.new_vcard,
            '3':self.list,
            '9':'break'
        }

        print('Organizer for ',self.name,' has been initiated. Enjoy!\n')

    def open(self):

        while(1):

            print('Organized owned by ',self.name,' opened.')
            print(self.pages,self.size,'pages waiting for you.\n')
            print("""Tell me what do you want to do:

                1- Add a new NOTE
                2- Add a new VCARD
                3- List all
                9- Close organizer""")

            selection = input()
            action = self.actions_que.get(selection)

            if  action == 'break': break
            elif action:
                action()
            else:
                print('Invalid command')

    def new_note(self):
        print ('Adding new note')
        new_item = note(1,'Note test','This is test note')
        self.notes.append(new_item)

    def new_vcard(self):
        print ('Adding new vcard')
        new_item = note(1,'VCard test','This is test vcard')
        self.notes.append(new_item)

    def list(self):
        for nt in self.notes:
            print(nt)
