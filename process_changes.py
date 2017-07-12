# class that will process a file
class DataProcessor(object):

    def __init__(self):
        self.authors = {}
        self.daysOfTheWeek = {}
        self.data = ''
    
    # returns the number of authors
    def getNumAuthors(self):
        return len(self.authors)
    
    # returns the number of days 
    def getNumDays(self):
        return len(self.daysOfTheWeek)
        
    # returns the number of lines in the file    
    def getNumLines(self):
        return len(self.data)
        
    # loads a given file and reads each line 
    def loadFile(self, file_name):    
        # attempts to open the file, print an error if it cant
        try:
            my_file = open(file_name,'r')
            self.data = my_file.readlines()
        except IOError : 
            print 'Could not read file'
            return -1
            
    # uses the first three letters of a day to return the full day name    
    def convertDayName(self,day):
        # list of days 
        days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
        dayName = None          # variable to store the current day 
        # loops through list of days 
        for d in days:
            # if the first three letters of current day equals the day, then return that day 
            if d[:3] == day:
                dayName = d
        return dayName        
     
    # reads each commit line to find the author and the date
    def readLines(self):
        index = 0               # current line in file 
        sep = 72*'-' + '\n'     # each commit line is preceded by 72 hyphens
        # continue looping until a break is encountered
        while True:
            try:
                # parse each of commit line and split by | 
                details = self.data[index + 1].split('|')
                # retrieve the author with spaces at end removed
                author = details[1].strip()
                # add it to dictionary if not already in it, else increment its count 
                self.authors[author] = self.authors.get(author,0)+1
                # retrieve the date with spaces at the end removed, then split it by spaces 
                date = details[2].strip().split()
                # retrieve the day portion and remove the first and last characters
                day = date[3][1:-1]
                # call function to return the full day name 
                dayName = self.convertDayName(day)
                # if the day was found, add it to dictionary or increment its count 
                if dayName != None:  
                    self.daysOfTheWeek[dayName] = self.daysOfTheWeek.get(dayName,0)+1
                # find next line 
                index = self.data.index(sep,index+1)
            except IndexError:
                break

    # returns the author with the most commits 
    def mostCommitsByAuthor(self):
        highestAuthor = None    # variable to store the author wih the highest number of commits  
        highestCommits = None   # variable to store the highest number of commits 
        # loop through dictionary
        for x in self.authors.items():
            # if set to default value or current author count is greater, then set variables 
            if highestAuthor == None or x[1] > highestCommits:
                highestAuthor = x[0]
                highestCommits = x[1]
        # use of formatting to return variables within message 
        return '%s had the most commits with %d' % (highestAuthor,highestCommits)

    # returns the day with the most commits 
    def mostCommitsByDay(self):
        highestDay = None       # variable to store the day with the highest number of commits
        highestCommits = 0      # variable to store the highest number of commits  
        # loop through dictionary
        for day in self.daysOfTheWeek.items():
            # if set to default value or current day count is greater, then set variables
            if highestDay == None or day[1] > highestCommits:
                highestDay = day[0]
                highestCommits = day[1] 
        return '%s was the day with the most commits with %d' %(highestDay, highestCommits)
        
   # returns the average number of commits 
    def averageCommits(self) :
        numCommits = 0           # variable to store the number of commits 
        # loop through dictionary and increment the total commits by the value 
        for x in self.authors.items():
            numCommits = numCommits + x[1]
        # divide the total commits by the number of author to calculate the average 
        average = numCommits/float(len(self.authors))
        return 'average number of commits is %g' %(average) 
    

# run only from command line 
if __name__ == '__main__':
    # file to be searched 
    changes_file = 'changes_python.log'
    # instance of class 
    dataprocessor = DataProcessor()
    # if the file was found, then perform functions 
    if dataprocessor.loadFile(changes_file) != -1:
        dataprocessor.readLines()
        print dataprocessor.mostCommitsByAuthor()
        print dataprocessor.averageCommits()
        print dataprocessor.mostCommitsByDay()
                       