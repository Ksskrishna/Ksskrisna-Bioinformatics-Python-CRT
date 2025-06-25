class Sort():
    def __init__(self):
        self.size = int(input("print the size of list: "))
        self.list = []
    def sort(self):
        for i in range(self.size):
            temp = int(input("enter the elements in the list: "))
            self.list.append(temp)
            count = 0
        print(self.list)
        for i in range(self.size):
            for j in range(self.size-i-1):
                count = count+1
                if self.list[j]>self.list[j+1]:
                    self.list[j],self.list[j+1] = self.list[j+1],self.list[j]
                    print(self.list)
        print(f"sorted array: {self.list}")
        print(count)

    
list1 = Sort()
list1.sort()