class Person:
    def __init__(self, name):
        self._name = name
        self._type = "Human"

    def present_name(self):
        print(f'Meu nome é {self._name}')

    def present_type(self):
        print(f'Meu tipo é {self._type}')


pessoa = Person("Ayla")
pessoa.present_name()
pessoa.present_type()


class Student(Person):
    def __init__(self, name, course):
        super().__init__(name)  # chama o construtor da classe base
        self._course = course
        self._type = "Student"

    def present_course(self):
        print(f'{self._name} é estudante do curso: {self._course}')


student1 = Student("Ayla", "programação")
student1.present_name()  # herda da classe base
student1.present_course()
student1.present_type()
