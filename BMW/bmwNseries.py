from BMW.bmw import BMW

class BMWnSeries(BMW):

    def __init__(self,Hp,engine):

        super().__init__(Hp,engine)

BMW535i = BMWnSeries(450,"Inline-6 Twin Turbo N54")

