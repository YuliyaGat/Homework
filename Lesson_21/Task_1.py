class My_cont:
    counter = 0

    def __init__(self, file, method):
        self.file = file
        self.method = method

    def __enter__(self):
        print('enter')
        self.file = open(self.file, self.method)
        My_cont.counter += 1
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit')
        print(exc_type, exc_val, exc_tb)
        if exc_type == ZeroDivisionError:
            print('There is a mistake')
        self.file.close()
        return True

if __name__ == '__main__':
    with My_cont('phonebook.json', 'r') as file:
        f = file.read()
        #int('a')
        #1 / 0
    print(f)
    print(file.closed)
    print(My_cont.counter)
