# -*- coding:utf-8 -*-
# Observer.py


from display import Display


class Observer:
    def __init__(self, observable):
        self.__observable = observable
        observable.registerObserver(self)
        self.__temperature = None
        self.__humidity = None

    def update(self, subject):
        pass


class CurrentConditionsDisplay(Observer, Display):
    def __init__(self, observable):
        Observer.__init__(self, observable)

    def update(self, subject):
        self.__humidity = subject.humidity
        self.__temperature = subject.temperature
        self.display()

    def display(self):
        print("temperature " + str(self.__temperature))
        print("humidity " + str(self.__humidity))


class StatisticsTempDisplay(Observer, Display):
    def __init__(self, observable):
        Observer.__init__(self, observable)
        self.__max = 0
        self.__min = 200
        self.__num = 0
        self.__sum = 0

    def update(self, subject):
        if self.__max < subject.temperature:
            self.__max = subject.temperature
        if self.__min > subject.temperature:
            self.__min = subject.temperature
        self.__num = self.__num + 1
        self.__sum = self.__sum + subject.temperature
        self.display()

    def display(self):
        print("max " + str(self.__max))
        print("min " + str(self.__min))
        print("avg " + str(float(self.__sum) / self.__num))
