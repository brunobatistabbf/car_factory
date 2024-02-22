from __future__ import annotations
from abc import ABC, abstractmethod


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

    def carroSUV(self) -> IcarroSUV:
        return CorollaCross()

class FabricaHonda(IFabricaCarros):

    def carroSedan(self) -> ICarroSedan:
        return Civic()

    def carroSUV(self) -> IcarroSUV:
        return HRV()

#abstract product A
class ICarroSedan(ABC):
    @abstractmethod
    def exibirInfoSedan(self):
        pass

class Corolla(ICarroSedan):
    def exibirInfoSedan(self):
        print("Cor: Branco")
        print("Valor: R$ 148.000,00")
        print("Ano: 2024")
        print("Motor: 2.0")
        print("Potência: 175cv")

class Civic(ICarroSedan):
    def exibirInfoSedan(self):
        print("Cor: Branco")
        print("Valor: R$ 259.000,00")
        print("Ano: 2024")
        print("Motor: 2.0")
        print("Potência: 297HP")

#abstract product B
class IcarroSUV(ABC):
    @abstractmethod
    def exibirInfoSedan(self):
        pass

class CorollaCross(IcarroSUV):
    def exibirInfoSedan(self):
        print("Cor: Cinza Granito")
        print("Valor: R$ 164.000,00")
        print("Ano: 2024")
        print("Motor: 2.0 DUAL")
        print("Potência: 177cv")

class HRV(IcarroSUV):
    def exibirInfoSedan(self):
        print("Cor: Branco")
        print("Valor: R$ 259.000,00")
        print("Ano: 2024")
        print("Motor: 2.0")
        print("Potência: 297HP")
