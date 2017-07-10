from datetime import datetime#The datetime module provides classes for manipulating dates and times.
class Spy:#A class in simple words is a blueprint of an object . used to reuse our code without writing it again and again.
    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = int(age)
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None
class chat:
    def __init__(self,msg,msg_by_me):
        self.msg = msg
        self.time = datetime.now()#current date and time
        self.msg_by_me = msg_by_me
spy = Spy('Nabin', 'Mr.', 20, 4.2,)
f1 = Spy('Nitesh', 'Mr.', 4.5, 25)
f2 = Spy('Shreya', 'Ms.', 3.52, 22)
f3 = Spy('Avilash', 'Mr.', 3.02, 19)
f4 = Spy('Abishek', 'Mr.',4.3,18)
f5 = Spy('Pooja','Ms.',3.86,21)
friends = [f1,f2,f3,f4,f5]#a friend variable consists of details of all friends listed above