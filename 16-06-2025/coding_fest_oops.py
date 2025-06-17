class Report():
    def __init__(self,day,activities,participants,project,technologies,ppt_given,winner,runner,b_performer,host):
        print("object created")
        day = input("enter Day: ")
        self.Day = day
        
        activities = input("Activities of the day including timeline: ")
        self.Activities = activities
        
        participants = input("Number of Participants for the day: ")
        self.Participants = participants
        
        project = input("enter the project names: ")
        self.Project = project
        
        technologies = input("Technologies used: ")
        self.Technologies = technologies
        
        ppt_given = input("enter how many ppt demonistrations given: ")
        self.Ppt_given = ppt_given

        winner = input("enter winner name: ")
        self.Winner = winner

        runner = input("enter runner name: ")
        self.Runner = runner

        b_performer = input("enter best performer name: ")
        self.B_performer = b_performer

        host = input("enter the host name: ")
        self.Host = host        
def Display_report(self):
    print(f"Report for Day: {self.Day}")
    print(f"Activities of the day including timeline: {self.Activities}")
    print(f"Number of Participants for the day: {self.Participants}")
    print(f"Technologies used are: {self.Technologies}")
    print(f"The number of ppt presentations given are: {self.Ppt_given}")
    print(f"The winner of the day is: {self.Winner}")
    print(f"The runner of the day is {self.Runner}")
    print(f"The best performer of the day is: {self.B_performer}")
    print(f"The event was hosted by : {self.Host}")
Day_1 = Report("{day}","{activities}","{participants}","{project}","{technologies}","{ppt_given}","{winner}","{runner}","{b_performer}","{host}")
Display_report(Day_1)
Day_2 = Report("{day}","{activities}","{participants}","{project}","{technologies}","{ppt_given}","{winner}","{runner}","{b_performer}","{host}")
Display_report(Day_2)
Day_3 = Report("{day}","{activities}","{participants}","{project}","{technologies}","{ppt_given}","{winner}","{runner}","{b_performer}","{host}")
Display_report(Day_3)
Day_4 = Report("{day}","{activities}","{participants}","{project}","{technologies}","{ppt_given}","{winner}","{runner}","{b_performer}","{host}")
Display_report(Day_4)
Day_5 = Report("{day}","{activities}","{participants}","{project}","{technologies}","{ppt_given}","{winner}","{runner}","{b_performer}","{host}")
Display_report(Day_5)
Day_6 = Report("{day}","{activities}","{participants}","{project}","{technologies}","{ppt_given}","{winner}","{runner}","{b_performer}","{host}")
Display_report(Day_6)