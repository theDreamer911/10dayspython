from abc import ABC, abstractmethod


class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass


class TextBox(UIControl):
    def draw(self):
        print('TextBox')


class DropDownList(UIControl):
    def draw(self):
        print("DropDownList")


class EatLongLast(UIControl):
    def draw(self):
        print("BusyOfEating")


def draw(controls):
    for control in controls:
        control.draw()


# ddl = DropDownList()
# textbox = TextBox()
# eat = EatLongLast()
# # print(isinstance(ddl, UIControl))
# # draw(ddl)
# draw([ddl, textbox, eat])
