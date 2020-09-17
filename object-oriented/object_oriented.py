#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2020/9/6 12:52
# @Author  : 雪成
# @Software: PyCharm
class Person:
    def __init__(self, name, sex, job, hp, weapon, ad):
        self.name = name
        self.sex = sex
        self.job = job
        self.hp = hp
        self.weapon = weapon
        self.ad = ad

    def give(self, dog):
        if dog.hp > self.ad:
            dog.hp -= self.ad
            print(f'{self.name}攻击了{dog.name},{dog.name}掉了{self.ad}点血,{dog.name}还剩下{dog.hp}点血')
        else:
            dog.hp = 0
            print(f'{self.name}攻击了{dog.name},{dog.name}掉了{self.ad}点血,{dog.name}还剩下{dog.hp}点血,你已经死了')


class Dog:
    def __init__(self, name, kind, hp, ad):
        self.name = name
        self.kind = kind
        self.hp = hp
        self.ad = ad

    def lick(self, person):
        if person.hp > self.ad:
            person.hp -= self.ad
            print(f'{self.name}舔了{person.name}一下,{person.name}掉了{self.ad}点血,{person.name}还剩{person.hp}点血')
        else:
            person.hp = 0
            print(f'{self.name}舔了{person.name}一下,{person.name}掉了{self.ad}点血,{person.name}还剩{person.hp}点血，你已经死了')


if __name__ == '__main__':
    alex = Person('Alex', '不详', '搓澡工人', 250, '搓澡巾', 1)
    Corgi = Dog('小金', '柯基', 249, 251)
    Person.give(alex, Corgi)
    Dog.lick(Corgi, alex)

# class Dog:
#     # def dog(name, kind, hp, ad):
#     def __init__(self, name, kind, hp, ad):
#         self.name = name
#         self.kind = kind
#         self.hp = hp
#         self.ad = ad
#
#
# Teddy = Dog('小白', '泰迪', 5000, 249)
# print(Teddy.name)
# print(Teddy.__dict__)
# def person(name, sex, job, hp, weapon, ad, level=0):
#     def give(dog):
#         dog['hp'] -= dic['ad']
#         print(f'{dic["name"]}攻击了{dog["name"]},{dog["name"]}掉了{dic["ad"]}点血')
#
#     dic = {
#         'name': name,
#         'sex': sex,
#         'job': job,
#         'level': level,
#         'hp': hp,
#         'weapon': weapon,
#         'ad': ad,
#         'action': give
#     }
#     return dic
#
#
# def dog(name, kind, hp, ad):
#     def lick(person):
#         person['hp'] -= dic['ad']
#         print(f'{dic["name"]}舔了{person["name"]},{person["name"]}掉了{dic["ad"]}点血')
#
#     dic = {
#         'name': name,
#         'kind': kind,
#         'hp': hp,
#         'ad': ad,
#         'action': lick
#     }
#     return dic
#
#
# Alex = person('alex', '不详', '搓澡工', 250, '搓澡巾', 1)
# Wusir = person('wusir', 'male', '法师', 500, '打狗棒', 1000)
#
# Teddy = dog('小白', '泰迪', 5000, 249)
# Corgi = dog('小金', '柯基', 10000, 499)
#
# Teddy['action'](Alex)
# Wusir['action'](Alex)
