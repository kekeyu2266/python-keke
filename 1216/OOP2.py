# 限制实例的属性和方法
class Stu(object):
    __slots__ = ("name", "age")  # 限制该类的属性只能从这两个里面出，该限制对其子类无效（子类需要自行指定）


class Stu(object):
    # def __init__(self, name, score):
    #    self.name = name
    #   self.score = score

    def get_score(self):
        print(self.score)
        return self.score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError("得分必须是整数")
        if value < 0 or value > 100:
            raise ValueError("1-100分以内")
        self.score = value


s = Stu()
s.set_score(20)
s.get_score()
r = Stu()
r.set_score(10)
r.get_score()
