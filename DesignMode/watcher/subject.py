from .observer import Observer


class Subject:
    def __init__(self):
        self.__observers = []
        self.__changed = True

    def registerObserver(self, observer):
        self.__observers.append(observer)

    def removeObserver(self, observer):
        self.__observers.remove(observer)

    def notifyObservers(self):
        if self.__changed == True:
            for everyObserver in self.__observers:
                everyObserver.update(self)
            self.changed = False

    @property
    def changed(self):
        return self.__changed

    @changed.setter
    def changed(self, value):
        if isinstance(value, bool):
            self.__changed = value


class WeatherData(Subject):
    def __init__(self):
        Subject.__init__(self)
        self.__temperature = 0
        self.__humidity = 0

    @property
    def temperature(self):
        return self.__temperature

    @property
    def humidity(self):
        return self.__humidity

    @temperature.setter
    def temperature(self, value):
        if isinstance(value, int):
            self.__temperature = value

    @humidity.setter
    def humidity(self, value):
        if isinstance(value, int):
            self.__humidity = value

    def setMeasurements(self, temperature, humidity):
        self.temperature = temperature
        self.humidity = humidity
        self.changed = True
        self.notifyObservers()
