'''Создайте тип данных (человек) Human, определите
атрибуты и методы для работы с ним.
Человек ест, спит, ходит на работу и отдыхает на
протяжении 70 лет. С 18 лет человек начинает работать
и в 65 лет выходит на пенсию.'''

class Human:
    def __init__(self, new_name):
        self.name = new_name
        self._age = 0
        print('Родился человек по имени', self.name,'!')
        
    def eating(self):
        print(self.name,'кушает.')

    def sleeping(self):
        print(self.name,'спит.')
        

    def working(self):
        if 18 >= self._age:
            print(self.name,'еще не работает.')
        elif self._age >= 65:
            print(self.name,'на пенсии.')
        else:
            print(self.name,'работает.')
        
        
    def relaxing(self):
        print(self.name,'отдыхает.')

    def get_age(self):
        return self._age
        
    def age_plus(self):
        self._age += 1
              

class Life:
    def life(self, human, years=70):
        while years:
            human.age_plus()
            print('Возраст',human.get_age())
            human.eating()
            human.sleeping()
            human.working()
            human.relaxing()
            years -= 1
            print('')


petr = Human('Петр')
life_petr = Life()
life_petr.life(petr)

