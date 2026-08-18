from abc import ABC,abstractmethod

class BMW(ABC):

    def __init__(self,Hp,engine):

        self.brand = 'BMW'
        self.Hp = Hp
        self.engine = engine
        self.slogan = "Its Bayerische Motoren Werke !!"

        print("Great Choice Buddy, always a BMW")

    def build_car(self,Model,Color):

        self.model = Model
        self.color = Color

    def get_Drive_mode(self):

        return "Comfy Drive"
    
    @abstractmethod
    def tuning(self,Booster):
        pass


