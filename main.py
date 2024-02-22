import car_factory.car_factory
from car_factory.car_factory import  IFabricaCarros
from car_factory.car_factory import FabricaToyota
from car_factory.car_factory import FabricaHonda


def cliente(factory: IFabricaCarros) -> None:
    carroSedan = factory.carroSedan()
    carroSUV = factory.carroSedan()

    print(f"{carroSedan.exibirInfoSedan()}")
    print(f"{carroSUV.exibirInfoSedan()}")


if __name__ == '__main__':
    print("Primeira Fabrica de Automoveis: Toyota")
    cliente(FabricaToyota())

    print("Primeira Fabrica de Automoveis: Toyota")
    cliente(FabricaHonda())


