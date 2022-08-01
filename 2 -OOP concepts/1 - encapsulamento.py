# definir a classe pessoa
class Person:
    def __init__(self, name, age, document, profession):
        self._name = name
        self._age = age
        self.__document = document
        self.profession = profession

    def __str__(self):
        return f"Nome:{self._name}, idade: {self._age}, documento: {self._document}, profissão: {self.profession}"


pessoa1 = Person("Ayla", 25, 2131313, "dev")
print(pessoa1)
