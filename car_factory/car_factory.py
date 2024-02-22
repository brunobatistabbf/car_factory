from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Tuple


class IFabricaCarros(ABC):

    @abstractmethod
    def carroSedan(self) -> ICarroSedan:
        pass

    @abstractmethod
    def carroSUV(self) -> IcarroSUV:
        pass


class FabricaToyota(IFabricaCarros):

    def carroSedan(self) -> ICarroSedan:
        return Corolla()

    def carroSUV(self, suv="Corolla Cross"):
        if(suv == "Corolla Cross"):
            return CorollaCross()
        else:
            return RAV4()

class FabricaHonda(IFabricaCarros):

    def carroSedan(self) -> ICarroSedan:
        return Civic()

    def carroSUV(self, suv="HRV"):
        if(suv == "HRV"):
            return HRV()
        else:
            return CRV()

#abstract product A
class ICarroSedan(ABC):
    @abstractmethod
    def exibirInfoSedan(self):
        pass

class Corolla(ICarroSedan):
    def exibirInfoSedan(self):
        print("\n")
        print("--Corolla--")
        print("Cor: Branco")
        print("Valor: R$ 148.000,00")
        print("Ano: 2024")
        print("Motor: 2.0")
        print("Potência: 175cv")
        print("\n")

class Civic(ICarroSedan):
    def exibirInfoSedan(self):
        print("\n")
        print("--CIVIC--")
        print("Cor: Branco")
        print("Valor: R$ 259.000,00")
        print("Ano: 2024")
        print("Motor: 2.0")
        print("Potência: 297HP")
        print("\n")

#abstract product B
class IcarroSUV(ABC):
    @abstractmethod
    def exibirInfoSUV(self):
        pass

class CorollaCross(IcarroSUV):
    def exibirInfoSUV(self):
        print("\n")
        print("--Corolla Cross--")
        print("Cor: Cinza Granito")
        print("Valor: R$ 164.000,00")
        print("Ano: 2024")
        print("Motor: 2.0 DUAL")
        print("Potência: 177cv")
        print("\n")

class HRV(IcarroSUV):
    def exibirInfoSUV(self):
        print("\n")
        print("--HRV--")
        print("Cor: Cinza Granito")
        print("Valor: R$ 195.800,00")
        print("Ano: 2024")
        print("Motor: 1.5L")
        print("Potência: 177HP")
        print("\n")

class RAV4(IcarroSUV):
    def exibirInfoSUV(self):
        print("\n")
        print("--RAV 4--")
        print("Cor: Branco")
        print("Valor: R$ 344.800,00")
        print("Ano: 2024")
        print("Motor: 2.5")
        print("Potência: 222HP")
        print("\n")

class CRV(IcarroSUV):
    def exibirInfoSUV(self):
        print("\n")
        print("--CR-V--")
        print("Cor: Cinza")
        print("Valor: R$ 189.800,00")
        print("Ano: 2019")
        print("Motor: 1.5")
        print("Potência: 200cv")
        print("\n")
