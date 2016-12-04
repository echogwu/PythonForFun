#/usr/bin/python
import datetime
import random
import time
import threading

class Person:
    name = ""
    sensitive = False
    insecurity = False
    reasoningLevel = 0    #the scale is 1-10
    emotional = 0
    funny = 0
    serious = 0
    detail_oriented = 0
    planning = 0
    honesty = 0
    talkative = 0
    creativity = 0
    messyMinded = 0
    selfCentered = 0
    stubborn = 0
    libido = 0

    def __init__(self, name = "", sensitive = False, insecurity = False, reasoningLevel = 0, emotional = 0, funny = 0, serious = 0, detail_oriented = 0, planning = 0, honesty = 0, talkative = 0, creativity = 0, messyMinded = 0, selfCentered = 0, stubborn = 0):
        self.name = name
        self.sensitive = sensitive
        self.insecurity = insecurity
        self.reasoningLevel = reasoningLevel
        self.emotional = emotional
        self.funny = funny
        self.serious = serious
        self.detail_oriented = detail_oriented
        self.planning = planning
        self.honesty = honesty
        self.talkative = talkative
        self.creativity = creativity
        self.messyMinded = messyMinded
        self.selfCentered = selfCentered
        self.stubborn = stubborn


class Female(Person):

    def __init__(self, name, sensitive, insecurity, reasoningLevel, emotional, funny, serious, detail_oriented, planning, honesty, talkative, creativity, messyMinded, selfCentered, stubborn):
        Person.__init__(self, name, sensitive, insecurity, reasoningLevel, emotional, funny, serious, detail_oriented, planning, honesty, talkative, creativity, messyMinded, selfCentered, stubborn)
        print("==========Please note: %s is a BEAUTY DANGER==========" % self.name)
        print("the scale is 1 - 10")
        print("name: %s\nsensitive: %s\ninsecurity: %s\nreasoningLevel: %s\nemotional: %s\nfunny: %s\nserious: %s\ndetail_oriented: %s\nplanning: %s\nhonesty: %s\ntalkative: %s\ncreativity: %s\nmessyMinded: %s\nselfCentered: %s\nstubborn: %s" % 
            (self.name, self.sensitive, self.insecurity, self.reasoningLevel, self.emotional, self.funny, self.serious, self.detail_oriented, self.planning, self.honesty, self.talkative, self.creativity, self.messyMinded, self.selfCentered, self.stubborn))
        self.libido = 5

    def argue(self, lock):
        lock.acquire()
        print("==================================%s says:==================================" % self.name)
        for statement in range(0, int(round(random.uniform(10,15)))):
            state = "bla" * int(round(random.uniform(0,50)))
            print(state)
        print("SILENCE FOR FIVE SECONDS")
        time.sleep(5)
        lock.release()



class Male(Person):

    def __init__(self, name, sensitive, insecurity, reasoningLevel, emotional, funny, serious, detail_oriented, planning, honesty, talkative, creativity, messyMinded, selfCentered, stubborn):
        Person.__init__(self, name, sensitive, insecurity, reasoningLevel, emotional, funny, serious, detail_oriented, planning, honesty, talkative, creativity, messyMinded, selfCentered, stubborn)
        print("==========Please notice: %s is very stubborn and thinks himself a SmartyPants==========" % self.name)
        print("the scale is 1 - 10")
        print("name: %s\nsensitive: %s\ninsecurity: %s\nreasoningLevel: %s\nemotional: %s\nfunny: %s\nserious: %s\ndetail_oriented: %s\nplanning: %s\nhonesty: %s\ntalkative: %s\ncreativity: %s\nmessyMinded: %s\nselfCentered: %s\nstubborn: %s" %
            (self.name, self.sensitive, self.insecurity, self.reasoningLevel, self.emotional, self.funny, self.serious, self.detail_oriented, self.planning, self.honesty, self.talkative, self.creativity, self.messyMinded, self.selfCentered, self.stubborn))
        self.libido = 10

    def argue(self, lock):
        lock.acquire()
        print("==================================%s says:==================================" % self.name)
        print("Hmmmmm....")
        time.sleep(2)
        for statement in range(0, int(round(random.uniform(3, 5)))):
            state = "bla" * int(round(random.uniform(0,50)))
            print(state)
        lock.release()

seriousnessMatrix = {"minor" : 5, "medium": 10, "serious": 15}

class Fight:
    date = datetime.datetime.now()
    topic = ""
    starter = None
    winner = None
    duration = 0
    seriousness = 0
    
    
    def __init__(self, topic = "", date = datetime.datetime.now(), starter = None, winner = None, seriousness = seriousnessMatrix["minor"]):
        self.date = date
        self.topic = topic
        self.starter = starter
        self.winner = winner
        self.seriousness = seriousness

    def fight(self, personA, personB):
        print("************************************************************************************************************")
        print("***********************************TOPIC: %s, DATE: %s***********************************" % (self.topic, self.date))
        print("************************************************************************************************************")
        lock = threading.RLock()
        round = 0
        for round in range(1, self.seriousness):
            personA.argue(lock)
            personB.argue(lock)

    def printTheWinner(self):
        print("************************************************************************************************************")
        print("***********************************THE WINNER FOR THE \"%s\" is %s***********************************" % (self.topic, self.winner))
        print("************************************************************************************************************")

Echo = Female(name = "Echo", sensitive = True, insecurity = True, reasoningLevel = 8, emotional = 5, funny = 7, serious = 8, detail_oriented = 9, planning = 9, honesty = 9, talkative = 8, creativity = 6, messyMinded = 3, selfCentered = 7, stubborn = 6)
Neto = Male(name = "Neto", sensitive = False, insecurity = False, reasoningLevel = 6, emotional = 5, funny = 7, serious = 8, detail_oriented = 3, planning = 4, honesty = 9, talkative = 4, creativity = 8, messyMinded = 9, selfCentered = 6, stubborn = 8)
topics = ["PINK CEREMONY FANTASY", "HIGH THIGH", "FIRING DIMI", "RENT A HOUSE"]
dates = [datetime.date(2016, 11, 18), datetime.date(2016,11,19), datetime.date(2016,12, 1), datetime.date(2016,12, 3)]
starters = ["Echo", "Neto", "Echo", "Neto"]
seriousness = ["serious", "serious", "medium", "minor"]
for index in range(0, len(topics)):
    fight = Fight(topic = topics[index], date = dates[index], starter = starters[index], seriousness = seriousnessMatrix[seriousness[index]])
    fight.fight(Echo, Neto)
    fight.printTheWinner()



