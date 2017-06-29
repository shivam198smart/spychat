from datetime import datetime

class Spy:


    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.total_words = 0
        self.current_status_message = None


class ChatMessage:

    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me

spy = Spy('Anonymous', 'Mr.', 24, 4.7)

friend_one = Spy('Doraemon', 'Mr.', 4.9, 27)
friend_two = Spy('Sizuka', 'Ms.', 4.39, 21)
friend_three = Spy('Nobita', 'Dr.', 4.95, 37)


friends = [friend_one, friend_two, friend_three]
