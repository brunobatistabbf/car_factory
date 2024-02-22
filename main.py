import car_factory.car_factory
from car_factory.car_factory import IFabricaCarros
from car_factory.car_factory import FabricaToyota
from car_factory.car_factory import FabricaHonda

def cliente(factory: IFabricaCarros) -> None:
    if factory == FabricaToyota:
        carroSedan = factory.carroSedan()
        carroSUV = factory.carroSUV()
        novoCarroSUV = factory.carroSUV(suv="RAV4")
        print(f"{carroSedan.exibirInfoSedan()}")
        print(f"{carroSUV.exibirInfoSUV()}")
        print(f"{novoCarroSUV.exibirInfoSUV()}")
    else:
        carroSedan = factory.carroSedan()
        carroSUV = factory.carroSUV()
        novoCarroSUV = factory.carroSUV(suv="CRV")
        print(f"{carroSedan.exibirInfoSedan()}")
        print(f"{carroSUV.exibirInfoSUV()}")
        print(f"{novoCarroSUV.exibirInfoSUV()}")


if __name__ == '__main__':
    print("Primeira Fabrica de Automoveis: Toyota")
    cliente(FabricaToyota())

    print("Segunda Fabrica de Automoveis: Honda")
    cliente(FabricaHonda())
