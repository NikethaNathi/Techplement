class Contact:
    def __init__(self):
        self.book = []
        self.names = []
        self.numbers = []
        self.emails = []

    def create(self, name, number, email):
        self.book.append([name, number, email])
        self.names.append(name)
        self.numbers.append(number)
        self.emails.append(email)
        print(name, 'contact created successfully...!')

    def update(self, name=False, number=False):
        #--------------------------------------Update using names---------------------------------#
        if name:
            if name in self.names:
                inames = [i for i, x in enumerate(self.names) if x == name]
                print('No. of contacts found:', len(inames), inames)
                c = 1
                for iname in inames:
                    print(c, 'name:', self.names[iname], 'details:', self.book[iname], '\n')
                    c += 1
                while True:
                    inp = input("Press 'y' to continue or 'n' to exit:")
                    if inp == 'y':
                        nm_i = int(input('Enter index of listed contact above:'))
                        try:
                            data = inames[nm_i - 1]
                            print('\nDetail', self.book[data])
                            print(1, '- Name: ', self.book[data][0])
                            print(2, '- Number: ', self.book[data][1])
                            print(3, '- Email:', self.book[data][2])
                            print(0, '- Exit')
                            while True:
                                ch = int(input('Enter index of listed contact above:'))
                                if ch == 1:
                                    ch_name = input('Enter name to update:')
                                    self.book[data][0] = ch_name
                                    self.names[data] = ch_name
                                elif ch == 2:
                                    ch_number = input('Enter Number to update:')
                                    self.book[data][1] = ch_number
                                    self.numbers[data] = ch_number
                                elif ch == 3:
                                    ch_email = input('Enter Email to update:')
                                    self.book[data][2] = ch_email
                                    self.emails[data] = ch_email
                                elif ch == 0:
                                    break
                                else:
                                    print("Invalid choice.")
                            print('#--------updated contact------#')
                            print(self.book[data])
                        except IndexError:
                            print('Index not found...!')
                    else:
                        break
            else:
                print('Name not found...!')

        #---------------------------------------- Update using numbers-----------------------------------#
        elif number:
            if number in self.numbers:
                inumbers = [i for i, x in enumerate(self.numbers) if x == number]
                print('No. of contacts found:', len(inumbers))
                c = 1
                for inumber in inumbers:
                    print(c, 'Number:', self.numbers[inumber], 'details:', self.book[inumber], '\n')
                    c += 1
                while True:
                    inp = input("Press 'y' to continue or 'n' to exit:")
                    if inp == 'y':
                        nm_i = int(input('Enter index of listed contact above:'))
                        try:
                            data = inumbers[nm_i - 1]
                            print('\nDetail', self.book[data])
                            print(1, '- Name: ', self.book[data][0])
                            print(2, '- Number: ', self.book[data][1])
                            print(3, '- Email:', self.book[data][2])
                            print(0, '- Exit')
                            while True:
                                ch = int(input('Enter index of listed contact above:'))
                                if ch == 1:
                                    ch_name = input('Enter name to update:')
                                    self.book[data][0] = ch_name
                                    self.names[data] = ch_name
                                elif ch == 2:
                                    ch_number = input('Enter Number to update:')
                                    self.book[data][1] = ch_number
                                    self.numbers[data] = ch_number
                                elif ch == 3:
                                    ch_email = input('Enter Email to update:')
                                    self.book[data][2] = ch_email
                                    self.emails[data] = ch_email
                                elif ch == 0:
                                    break
                                else:
                                    print("Invalid choice.")
                            print('#--------updated contact------#')
                            print(self.book[data])
                        except IndexError:
                            print('Index not found...!')
                    else:
                        break
            else:
                print('Number not found...!')

    def delete(self, name=False, number=False):
        if name:
            if name in self.names:
                inames = [i for i, x in enumerate(self.names) if x == name]
                if len(inames) > 0:
                    print('No. of contacts found:', len(inames))
                    c = 1
                    for iname in inames:
                        print(c, 'Name:', self.names[iname], 'Details:', self.book[iname])
                        c += 1
                    inp = input("Press 'y' to continue or 'n' to exit:")
                    if inp == 'y':
                        nm_i = int(input('Enter index of listed contact above:'))
                        try:
                            data = inames[nm_i - 1]
                            print('\nDetails:', self.book[data])
                            f = input('Are you sure you want to DELETE?(y/n):')
                            if f == 'y':
                                del self.book[data]
                                del self.numbers[data]
                                del self.names[data]
                                del self.emails[data]
                                print('#-------Updated contact book--------#')
                                print('\nName Entries:', self.names)
                                print('\nNumber Entries:', self.numbers)
                        except IndexError:
                            print('Index not found...!')
                    else:
                        print('No contacts deleted.')
            else:
                print('No contact found...!')

        elif number:
            if number in self.numbers:
                inumbers = [i for i, x in enumerate(self.numbers) if x == number]
                if len(inumbers) > 0:
                    print('No. of contacts found:', len(inumbers))
                    c = 1
                    for inumber in inumbers:
                        print(c, 'Number:', self.numbers[inumber], 'Details:', self.book[inumber])
                        c += 1
                    inp = input("Press 'y' to continue or 'n' to exit:")
                    if inp == 'y':
                        nm_i = int(input('Enter index of listed contact above:'))
                        try:
                            data = inumbers[nm_i - 1]
                            print('\nDetails:', self.book[data])
                            f = input('Are you sure you want to DELETE?(y/n):')
                            if f == 'y':
                                del self.book[data]
                                del self.numbers[data]
                                del self.names[data]
                                del self.emails[data]
                                print('#-------Updated contact book--------#')
                                print('\nName Entries:', self.names)
                                print('\nNumber Entries:', self.numbers)
                        except IndexError:
                            print('Index not found...!')
                    else:
                        print('No contacts deleted.')
            else:
                print('No contact found...!')

    def phonebook(self):
        print('\nTotal contacts found:', len(self.book))
        for contact in self.book:
            print('\nName:', contact[0])
            print('Phone Number:', contact[1])
            print('Email:', contact[2])

    def search(self, number=False, name=False):
        if name:
            if name in self.names:
                inames = [i for i, x in enumerate(self.names) if x == name]
                c = 1
                for iname in inames:
                    print(c, 'Name:', self.names[iname], 'Details:', self.book[iname], '\n')
                    c += 1
            else:
                print('No contact found...!')
        elif number:
            if number in self.numbers:
                inumbers = [i for i, x in enumerate(self.numbers) if x == number]
                c = 1
                for inumber in inumbers:
                    print(c, 'Number:', self.numbers[inumber], 'Details:', self.book[inumber], '\n')
                    c += 1
            else:
                print('No contact found...!')
        else:
            print('No contact found...!')

# Menu driven program
menu = '''
          1. Create
          2. Update
          3. List Contacts
          4. Search
          5. Delete
          6. Exit
'''

if __name__ == "__main__":
    c = Contact()
    
    a = True
    while a:
        print('\n', menu, '\n')
        choice = int(input('\nEnter your choice:'))
        if choice == 1:
            name = input('Enter Name:')
            phone = input('Enter phone number:')
            email = input('Enter your email:')
            c.create(name, phone, email)
        elif choice == 2:
            k = True
            while k:
                print('''
                    1. Update through name
                    2. Update through number
                    3. Exit
                ''')
                inp = int(input('Enter choice:'))
                if inp == 1:
                    name = input('Enter Name:')
                    c.update(name=name)
                elif inp == 2:
                    number = input('Enter Number:')
                    c.update(number=number)
                else:
                    k = False
        elif choice == 3:
            c.phonebook()
        elif choice == 4:
            k = True
            while k:
                print('''
                    1. Search through name
                    2. Search through number
                    3. Exit
                ''')
                inp = int(input('Enter choice:'))
                if inp == 1:
                    name = input('Enter name:')
                    c.search(name=name)
                elif inp == 2:
                    number = input('Enter number:')
                    c.search(number=number)
                else:
                    k = False
        elif choice == 5:
            k = True
            while k:
                print('''
                    1. Delete through name
                    2. Delete through number
                    3. Exit
                ''')
                inp = int(input('Enter choice:'))
                if inp == 1:
                    name = input('Enter name:')
                    c.delete(name=name)
                elif inp == 2:
                    number = input('Enter number:')
                    c.delete(number=number)
                else:
                    k = False
        elif choice == 6:
            a = False
        else:
            print("Invalid choice!")
            break
