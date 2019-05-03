import _thread
import time

class Carro:
    def SetType(self, type):
        self._Type = type

    def GetType(self):
        return self._Type

    def SetModel(self, model):
        self._Model = model

    def GetModel(self):
        return self._Model

    def SetPrice(self, price):
        self._Price = price

    def GetPrice(self):
        return self._Price

    def SetMilesDrive(self, milesDrive):
        self._MilesDrive = milesDrive

    def GetMilesDrive(self):
        return self._MilesDrive

    def SetOwner(self, owner):
        self._Owner = owner

    def GetOwner(self):
        return self._Owner

    def GetCurrentPrice(self):
        return self._Price - (self._MilesDrive * 10)


def main():
    myCar = Carro()
    myCar.SetType("BMW")
    myCar.SetModel(2015)
    myCar.SetPrice(26000)
    myCar.SetMilesDrive(15)
    myCar.SetOwner("Araujo")
    PrecoAtual = myCar.GetCurrentPrice()
    print("New price {}".format(PrecoAtual))

    myCar2 = Carro()
    myCar.SetType("Ferrari")
    myCar.SetModel(2017)
    myCar.SetPrice(27000)
    myCar.SetMilesDrive(8)
    myCar.SetOwner("Araujo")
    PrecoAtual = myCar.GetCurrentPrice()
    print("New price {}".format(PrecoAtual))


main()
