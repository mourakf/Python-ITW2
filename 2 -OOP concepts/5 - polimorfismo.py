# sobrescrever o comportamento da classe base
# polimorfismo com herança
class Animal:
    def __init__(self):
        self.__number_patas = -1
        self.__has_wings = False

    @property
    def number_patas(self):
        return self.__number_patas

    @property
    def has_wings(self):
        return self.__has_wings

    def emitir_som(self):
        print("...")


class Dog(Animal):
    def __init__(self):
        super().__init__()
        self.__number_patas = 4
        self.__has_wings = False

    @property
    def has_wings(self):
        return self.__has_wings

    def brinca(self):
        print("brinca de bolinha")

    @property
    def number_patas(self):
        return self.__number_patas


class Cat(Animal):
    def __init__(self):
        self.__number_patas = 4
        self.__has_wings = False

    @property
    def number_patas(self):
        return self.__number_patas

    @property
    def has_wings(self):
        return self.__has_wings

    def emitir_som(self):
        print('miau')


class Calopsita(Animal):
    def __init__(self):
        self.__number_patas = 2
        self.__has_wings = True

    @property
    def has_wings():
        return self.__has_wings

    def emitir_som(self):
        print('pi')

    def voar(self):
        print("Voando")

    @property
    def number_patas(self):
        return self.__number_patas


def processar_animal(animal: Animal):
    print(f'Este animal tem {animal.number_patas}')
    print(f'Este animal tem asas? {animal.has_wings}')
    animal.emitir_som()
    if isinstance(animal, Calopsita):
        animal.voar
    if isinstance(animal, Dog):
        animal.brinca()


dog1 = Dog()
cat1 = Cat()

processar_animal(dog1)
processar_animal(cat1)
