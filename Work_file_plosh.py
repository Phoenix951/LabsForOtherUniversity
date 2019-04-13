# программа для работы с файлами и вывода результатов подсчетов на основе данных из файла
import numpy as np

class Figure(object):
    def __init__(self, name):
        self.name = name

    def info(self):
        """Метод для вывода информации по данным"""
        print()
        
    def read_file(self):
        """Метод для чтения файла с данными"""
        with open(self.name, 'r', encoding='utf-8') as old_file:
            nums = old_file.read().split("\n\n")
        return nums

    def write_file(self):
        """Метод для записи полученных значений в файл"""
        with open("result.txt", 'w', encoding='utf-8') as new_file:
            new_file.write("") 

    def cube(self):
        """Метод для выведения данных для куба"""
        for i in self.read_file():
            if "Куб" in i:
                newcube = i
        return newcube

    def ball(self):
        """Метод для выведения данных для шара"""
        for i in self.read_file():
            if "Шар" in i:
                newball = i
        return newball

    def piramid(self):
        """Метод для выведения данных для пирамиды"""
        for i in self.read_file():
            if "Пирамида" in i:
                newpir = i
        return newpir
        
class Cube(Figure):
    def info(self):
        print(Figure.cube(self))

    def calcul(self):
        """Метод вычисления площади и объема для куба"""
        lines = Figure.cube(self).split("\n")
        for line in lines:
            if line.startswith("Ребро:"):
                rebro = int(line.split()[1])
           
        self.volume = rebro ** 2
        self.square = rebro ** 2
        print("\tПлощадь поверхности равна: ", self.square)
        print("\tОбъем куба равен: ", self.volume, "\n")

    def write_file(self):
        with open("result.txt", 'w', encoding='utf-8') as new_file:
            new_file.write("Куб:\n\tПлощадь поверхности равна: " + str(self.square) + 
                           "\n\tОбъем куба равен: " + str(self.volume) + "\n")


class Ball(Figure):
    def info(self):
        print(Figure.ball(self))

    def calcul(self):
        """Метод вычисления площади и объема для шара"""
        lines = Figure.ball(self).split("\n")
        for line in lines:
            if line.startswith("Радиус:"):
                radius = int(line.split()[1])
            
        self.volume = 4/3*np.pi*radius**3
        self.square = 4*np.pi*radius**2
        print("\tПлощадь поверхности шара равна: ", self.square)
        print("\tОбъем шара равен: ", self.volume, "\n")

    def write_file(self):
        with open("result.txt", 'a', encoding='utf-8') as new_file:
            new_file.write("Шар:\n\tПлощадь поверхности шара равна: " + str(self.square) + 
                           "\n\tОбъем шара равен: " + str(self.volume) + "\n")

class Piramid(Figure):
    def info(self):
        print(Figure.piramid(self))

    def calcul(self):
        """Метод вычисления площади и объема для пирамиды"""
        lines = Figure.piramid(self).split("\n")
        for line in lines:
            if line.startswith("Сторона основания:"):
                bot_side = int(line.split()[2])
            elif line.startswith("Длина высоты:"):
                height_len = int(line.split()[2])
            elif line.startswith("Длина боковой стороны:"):
                side_len = int(line.split()[3])
            elif line.startswith("Высота боковой поверхности:"):
                height_side_len = float(line.split()[3])
                
        self.volume = 1/3*height_len*bot_side**2
        self.square = 4*2*bot_side*height_side_len
        print("\tПлощадь поверхности пирамиды равна: ", self.square)
        print("\tОбъем пирамиды равен: ", self.volume, "\n")

    def write_file(self):
        with open("result.txt", 'a', encoding='utf-8') as new_file:
            new_file.write("Пирамида:\n\tПлощадь поверхности пирамиды равна: " + str(self.square) + 
                           "\n\tОбъем пирамиды равен: " + str(self.volume) + "\n")

class Main():
    def complite(self):
        """Метод для выполнения"""
        # название файла
        namefile = 'ploshadi.txt'
        # выполнения вычислений для кубов
        cube1 = Cube(namefile)
        cube1.info()
        cube1.calcul()
        cube1.write_file()

        # выполнение вычислений для шара
        ball1 = Ball(namefile)
        ball1.info()
        ball1.calcul()
        ball1.write_file()

        # выполнение вычислений для пирамиды
        piram1 = Piramid(namefile)
        piram1.info()
        piram1.calcul()
        piram1.write_file()

# запуск главной фукции
execution = Main()
execution.complite()
