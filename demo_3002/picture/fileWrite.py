class fileWrite():
    def __init__(self):
        self.filename = None
    def del_fw(self):
        del self
    def setFilename(self, filename):
        self.filename = filename

    def println(self, lines):
        if self.filename is None:
            print('No filename set')
            return False
        try:
            with open(self.filename, 'w') as f:
                for i, line in enumerate(lines):
                    f.write("{line}\n")
            print(f"File written to {self.filename} successfully.")
        except:
            print('Error writing file.')

    def print(self, lines):
        if self.filename is None:
            print('No filename set')
            return False
        try:
            with open(self.filename, 'w') as f:
                for line in lines:
                    f.write(line)
            print(f"File written to {self.filename} successfully.")
        except:
            print('Error writing file.')

#to_use !!!
# my_file_write = fileWrite()
# my_file_write.setFilename(r'demo_3002\test123.txt')
# my_file_write.println(["print('Hello World1')", "print('Hello World')"])
# my_file_write.print(["print('Hello World1')", "print('Hellld2')"])
