class fileRead():
    def __init__(self):
        self.filename = None
        self.fileRead = None
        self.file = None
        self.tasksArray = []

    def setFilename(self, filename):
        try:
            self.file = open(filename, 'r')
            self.fileRead = self.file.read()
            self.file.close()
            self.filename = filename
        except:
            print('File not found')

    def getRead(self):
        return self.fileRead
    
    def getFilename(self):
        return self.filename
    
    def getLines(self):
        try:
            return self.fileRead.splitlines()
        except:
            return ["None"]

    def getTasksArray(self, filename):
        self.setFilename(filename)
        self.tasksArray = self.getLines()
        for i in range(len(self.tasksArray)):
            self.tasksArray[i] = self.tasksArray[i].split(',')
        self.file.close()
        # for i in line:
        #     print("1"+i)
        return self.tasksArray
    

# to_use !!!
# my_file_read = fileRead()
# print("___________________________________")
# print(my_file_read.getTasksArray(r'demo_3002\1.txt'))

