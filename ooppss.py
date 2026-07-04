# class person:
#     name="swetha"
# p1=person()
# print(p1.name)
'''constructor'''
#class players:
#    def __init__(self,name,role,jersey,team):
#        self.name = name
#        self.role = role
#        self.jersey = jersey
#        self.team = team
# p1=players("dhoni","wicket keeper",7,"csk")
# p2=players("bumrah","bowler",93,"mi")
# print(p2.team)
# p3=players("Pandya","All rounder","33","RCB")
# print(p3.team)
'''single inheritance'''
# class Vehicle:
#     def move(self):
#        print("Vehicle is moving")
# class Car(Vehicle):
#    pass
# c1 = Car()
# c1.move()
# class csk:
#     def whistle(self):
#         print("whistle podu")
# class dhoni(csk):
#     pass
# d1=dhoni()
# d1.whistle()
# '''hierarchical inheritance'''
#
# class ipl:
#     def org(self):
#         print("tata ipl")
#
# class dhoni(ipl):
#     def whistle(self):
#         print("whistle podu-csk yellow team")
# class virat(ipl):
#     def lolly(self):
#         print("ee sala cup namde-rcb red team")
# # d1 = dhoni()
# # print(d1.org())
# # print(d1.whistle())
# v1=virat()
# print(v1.org())
# v1.lolly()
#
# class A:
#      def showA(self):
#         print("Class A")
# class B(A):
#    def showB(self):
#         print("Class B")
# class C(A):
#    def showC(self):
#         print("Class C")
# class D(B, C):
#    def showD(self):
#         print("Class D")
# d1 = D()
# d1.showA()
# d1.showB()
# d1.showC()
# d1.showD()
#

"""polymorphism"""
# class Animal:
#    def sound(self):
#        print("Animal makes sound")
# class Dog(Animal):
#   def sound(self):
#        print("Dog barks")
#
# d1 = Dog()
#
# d1.sound()
#
# class player:
#     def play(self):
#         print('playing')
# class wicket(player):
#     def play(self):
#         print("wicket keeper keeping wickets")
# class batsman(player):
#     def play(self):
#         print("batsman hits the balls")
# class bowler(player):
#     def play(self):
#         print("yorker ")
# virat=player()
# virat.play()
# dhoni=wicket()
# dhoni.play()
# bumrah=bowler()
# bumrah.play()
# rutu=batsman()
# rutu.play()

'''encapsulation'''
'''public'''
# class player:
#
#    def __init__(self):
#        self.name= "messi"
# p1=player()
# print(p1.name)
'''protected'''
# class player:
#
#    def __init__(self):
#        self._name= "messi"
# p1=player()
# print(p1._name)
# class bcci:
#
#    def __init__(self):
#        self._salary = 50000
#
# class dhoni(bcci):
#
#    def show(self):
#        print(self._salary)
#
# d1=dhoni()
# d1.show()
# '''private'''
# class bcci:
#
#    def __init__(self):
#        self.__salary = 50000
#
# class dhoni(bcci):
#
#    def show(self):
#        print(self.__salary)
#
# d1=dhoni()
# d1.show()


# class bcci:
#
#    def __init__(self):
#
#        self.__balance = 50000
#
#    def show_balance(self):
#
#        print("Balance =", self.__balance)
#
# b1 = bcci()
# b1.show_balance()

#abstraction
'''without abstraction'''
# class movie:
#     def open(self):
#         print('open book my show')
#     def class1 (self):
#         print("choose your class")
#     def seats(self):
#         print("choose your seats")
#     def snacks(self):
#         print("choose your snacks")
#     def pay(self):
#         print("paythe bill")
#     def review(self):
#         print("give your reviewsl")
# m1=movie()
# m1.open()
# m1.class1()
# m1.seats()
# m1.snacks()
# m1.pay()
# m1.review()

'''with abstraction'''
from abc import ABC, abstractmethod
class arrs(ABC):
    @abstractmethod
    def ticket_booking(self):
        pass
class movie(arrs):
    def open(self):
        print('open book my show')
    def class1 (self):
        print("choose your class")
    def seats(self):
        print("choose your seats")
    def snacks(self):
        print("choose your snacks")
    def pay(self):
        print("paythe bill")
    def review(self):
        print("give your reviewsl")

    def ticket_booking(self):
        self.open()
        self.class1()
        self.seats()
        self.snacks()
        self.pay()
        self.review()
m1=movie()
m1.ticket_booking()


