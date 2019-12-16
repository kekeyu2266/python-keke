import types


class Student(object):
    def __init__(self, name, score):  # self是默认方法__init__的第一个参数
        self.name = name
        self.score = score

    def print_score(self):
        print("%s:%s" % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            print("A")
            return "A"
        elif self.score >= 60:
            print("B")
            return "B"
        else:
            print("C")
            return "C"


keke = Student("keke", 100)  # 已有__init__方法的情况下，创建实例必须指定方法的参数
lisa = Student("lisa", 99)
haha = Student("haha", 20)
keke.print_score()
lisa.print_score()
haha.print_score()
keke.get_grade()
lisa.get_grade()
haha.get_grade()

print("-----------------")
# 访问控制，私有方法


class Stu(object):
    def __init__(self, name, scroe):
        self.__name = name  # 私有变量，无法修改
        self.__score = scroe

    def print_score(self):
        print("%s:%s" % (self.__name, self.__score))

    def get_grade(self):
        if self.__score >= 90:
            print("A")
            return "A"
        elif self.__score >= 60:
            print("B")
            return "B"
        else:

            print("C")
            return "C"

    def get_scroe(self):
        print(self.__score)
        return self.__score

    def get_name(self):
        print(self.__name)
        return self.__name

    def set_name(self, name):
        self.__name = name

    def set_scroe(self, score):
        self.__score = score


kk = Stu("keke", 100)
pp = Stu("pp", 32)
kk.print_score()
kk.get_grade()
kk.get_name()
kk.set_name("44")
kk.get_name()


# 练习
# 请把下面的Student对象的gender字段对外隐藏起来，用get_gender()和set_gender()代替，并检查参数有效性：


class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender

    def get_gender(self):
        print(self.__gender)
        return self.__gender

    def set_gender(self, gender):
        if gender == 'male' or gender == 'female':
            self.__gender = gender
        else:
            raise ValueError('error gender')


bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')

print("-----------------")
# 继承和多态


class Animal(object):
    def run(self):
        print("Animal is running")


class Pig(Animal):
    pass  # 继承父类的子类，直接可以使用父类的方法


class Dog(Animal):
    def run(self):  # 虽然继承父类方法，但是子类可以改写父类方法
        print("Dog is running")

    def eat(self):  # 子类可以增加方法，父类无法调用子类新增的方法
        print("Dog is eatting")


class Cat(Animal):
    def run(self):
        print("Cat is running")

    def eat(self):
        print("Cat is eatting")


dd = Dog()  # dd是Dog类型，也是Animal类型，这叫多态
cc = Cat()
pp = Pig()
pp.run()
dd.run()
cc.run()
dd.eat()
cc.eat()
# pp.eat()  pp没有eat这种方法


def run_tw(aa):
    aa.run()
    aa.run()


run_tw(Animal())
# Animal is running
# Animal is running

run_tw(Dog())
# Dog is running
# Dog is running

run_tw(Cat())
# Cat is running
# Cat is running


class Tort(Animal):
    def run(self):
        print("Tort is running slowly")


run_tw(Tort())
# Tort is running slowly
# Tort is running slowly


# 判断类型
# 使用type
print(type(123) == type(456))
print(type('1234sd') == type("蒋定价格"))
print(type('1234sd') == str)
print(type(abs) == type(max))
print("-----------------")


def fn():
    pass


# 需要improt types
print(type(fn) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)
print("-----------------")

# 使用isinstance
print(isinstance(pp, Animal))
print(isinstance(kk, Animal))
print(isinstance(dd, Animal))
print(isinstance(dd, Dog))
print("-----------------")
print(isinstance("123", str))
print(isinstance(123, int))
# isinstance的第二个参数可以是一个tuple，相当于or
print(isinstance([1, 2, 3], (list, tuple)))


# 使用dir
print(dir("abc"))  # 获取一个对象的所有属性与方法

print(len("123"))
print("123".__len__())

print("-----------------")
# 使用getattr(),setattr(),hasattr()


class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x*self.x


obj = MyObject()
print(hasattr(obj, "x"))
print(hasattr(obj, "t"))
print(getattr(obj, "x"))
print(obj.power())
setattr(obj, "x", 10)
print(getattr(obj, "x"))
print(obj.power())
print(getattr(obj, "z", "错误"))
print(hasattr(obj, "power"))

# 实例属性和类属性

# 练习，为了统计学生人数，可以给Student类增加一个类属性，每创建一个实例，该属性自动增加：


class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1


# 测试:
if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')
