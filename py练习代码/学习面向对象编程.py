class Person:
    def __init__(self, name, age, height):
        self.name = name
        self._age = age
        self.height = height
        print("Person created")

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if 0 > value or value > 150:
            raise ValueError("age must be between 0 and 150")
        elif not isinstance(value, int):
            raise TypeError("age must be an integer")
        else:
            self._age = value

class Student(Person):   #Python 中子类会继承父类的所有非私有属性和方法（包括 property 装饰的属性）
    def __init__(self, hobby, name, age, height):
        self.hobby = hobby
        super().__init__(name, age, height)

xiaoming = Person("xiapming",18,180)
xiaoming.age = 20
print(xiaoming.age)

lihua =Student("reading", "lihua", 17, 170)
