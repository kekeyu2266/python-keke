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
