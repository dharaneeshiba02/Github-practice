from BMW.bmw import BMW

class Msport(BMW):

    def __init__(self,Hp,engine):

        super().__init__(Hp,engine)

        print("M - Mid ? , No its a Monster")

    def tuning(self,Booster):

        Turbo = int(Booster * 0.90)

        self.Hp = self.Hp + Turbo

        print("Tuned Successfully ")
        print("Turbo :",Turbo)
        print("Your Hp is set to : ",self.Hp)

    

BmwM5 = Msport(617,"V8")
BmwM5.tuning(50)
