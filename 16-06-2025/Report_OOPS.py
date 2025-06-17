'''
You have atteded a skill Development Training program ffor 15 days on python program
task:
Write a python program to give detailed report of 15 days python training that includes
1.Day
2.topics covered
3.efficiency
4.number of aassignment questions solved
5.number of hacker rank questions solved
6.Ratings achived on hackerrank for that particular day
7.certifications completed (include name of certificate)
8.Duration of class
9.Rating of the class on scale of 5
    1.being worst
    2.being bad
    3.being average
    4.being good
    5.being best
'''
class Report():
    def __init__(self,day,topics_covered,efficiency,assignments,hackerrank,Rating_day,certifications,Rating):
        print("object created")
        self.Day = day
        self.Topics_covered = topics_covered
        self.Efficiency = efficiency
        self.Assignments = assignments
        self.Hackerrank = hackerrank
        self.Rating_day = Rating_day
        self.Certifications = certifications
        self.Rating = Rating

def Display_report(self):
    print(f"Report for Day: {self.Day}")
    print(f"Topics covered: {self.Topics_covered}")
    print(f"Rate the effeciency on the scale of 5: {self.Efficiency}")
    print(f"Number of assignments questions solved: {self.Assignments}")
    print(f"Number of Hacker rank questions solved: {self.Hackerrank}")
    print(f"Rating achieved in hackerrank on that particular day: {self.Rating_day}")
    print(f"Certifications completed on that day: {self.Certifications}")
    print(f"Give overall Rating for that day on a scale of 5: {self.Rating}")

Day_1 = Report("1","Basics of python","5","10","3","bronze","1 - Basics of python","5")
Display_report(Day_1)