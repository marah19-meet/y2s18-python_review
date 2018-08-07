class Superheros():
    def __init__(self,name,superpower,strength):
        self.name=name
        self.superpower=superpower
        self.strength=strength
        print("my name is"+self.name + "my strength is" + str(self.strength))
    def save_civillian(self):
        print(self.name,self.strength)




superman = Superheros("superman","flying",100)
