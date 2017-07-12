from process_changes import * 
import unittest 

# class to test the data processor functionality
class TestDataProcessor(unittest.TestCase):

    # setup the test class 
    def setUp(self):
        self.dataprocessor = DataProcessor()
        self.dataprocessor.loadFile('changes_python.log')
     
    # function to test getNumAuthors()
    def testGetNumAuthors(self):
        result = self.dataprocessor.getNumAuthors()
        self.assertEqual(0,result)
        
    # function to test getNumDays()
    def testGetNumDays(self):
        result = self.dataprocessor.getNumDays()
        self.assertEqual(0,result)
        
    # function to test getNumLines()
    def testGetNumLines(self):
        result = self.dataprocessor.getNumLines()
        self.assertEqual(5255,result)
          
    # function to test loadFile()
    def testLoadFile(self):
        # file that exists
        result = self.dataprocessor.loadFile('changes_python.log')
        self.assertEqual(None,result)
        # file that doesnt exist 
        result = self.dataprocessor.loadFile('filename.log')
        self.assertEqual(-1,result)
      
    # function to test readLines()
    def testReadLines(self):
        result = self.dataprocessor.readLines()
        self.assertEqual(None,result)
        # now test getNumAuthors() and getNumDays() again 
        result = self.dataprocessor.getNumAuthors()
        self.assertEqual(10,result)
        result = self.dataprocessor.getNumDays()
        self.assertEqual(5,result)
     
    # function to test convertDayName()
    def testConvertDayName(self):
        result = self.dataprocessor.convertDayName('Mon')
        self.assertEqual('Monday',result)
        result = self.dataprocessor.convertDayName('Wed') 
        self.assertEqual('Wednesday',result)
        result = self.dataprocessor.convertDayName('Fri') 
        self.assertEqual('Friday',result)
        result = self.dataprocessor.convertDayName('Hello world')
        self.assertEqual(None,result)
     
    # function to test mostCommitsByAuthor()
    def testMostCommitsByAuthor(self):
        self.dataprocessor.readLines()
        result = self.dataprocessor.mostCommitsByAuthor()
        # split the result based on spaces 
        result = result.split()
        # extract the author and commits from their respective positions
        author = result[0]
        commits = int(result[6])
        self.assertEqual('viacheslav.vdovenko',author)
        self.assertEqual(191,commits)
       
    # function to test mostCommitsByDay()       
    def testMostCommitsByDay(self):
        self.dataprocessor.readLines()
        result = self.dataprocessor.mostCommitsByDay()
        result = result.split()
        day = result[0]
        commits = int(result[9])
        self.assertEqual('Thursday',day)
        self.assertEqual(118,commits)
        
    # function to test averageCommits()       
    def testAverageCommits(self):
        self.dataprocessor.readLines()
        result = self.dataprocessor.averageCommits()
        result = result.split()
        average = float(result[5])
        self.assertEqual(42.2,average)

# run only from command line         
if __name__ == '__main__':
    # calls any functions that are preceded by test 
    unittest.main()