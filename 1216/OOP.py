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
