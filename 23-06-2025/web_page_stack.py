'''
write a py porg to simulate the behaviour of a web browsers back button when a user visits a new page push it to the stack 
when user clicks back pop the top page and go back to the previous page 
'''
class Browser():
    def __init__(self):
        self.history = []
    def visit(self,page1):
        self.history.append(page1)
        print(f"visited page {page1}")
    def undo(self):
        if len(self.history)>1:
            self.history.pop()
            print(f"back to {self.history[-1]}")
        else:
            print("No pages to comeback")
browser = Browser()
browser.visit('google.com')
browser.visit('instagram.com')
browser.visit('github.com')
browser.undo()
browser.undo()
browser.undo()