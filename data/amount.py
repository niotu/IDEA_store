class Amount:
    def __init__(self):
        self.amount = '1'

    def get_value(self):
        return self.amount

    def decrease(self):
        self.amount = str(int(self.amount) - 1)

    def increase(self):
        print(1)
        self.amount = str(int(self.amount) - 1)

    def kill(self):
        self.kill()
