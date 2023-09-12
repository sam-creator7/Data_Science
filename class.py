class Chat:
    def __init__(self, n, i):
        self.name = n
        self.interest = i

    def work(self):
        if self.interest == 'Data':
            print(self.name, " is in Data")
        elif self.interest == 'Management':
            print(self.name, " loves management")

    def say(self):
        print(self.name, ' says hi!!')


samarth = Chat("Samarth","Management")
samarth.work()
samarth.say()

