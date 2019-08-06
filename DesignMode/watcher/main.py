from .subject import WeatherData
from .observer import Observer


def main():
    weatherData = WeatherData()
    currentDisplay = Observer.CurrentConditionsDisplay(weatherData)
    statisticsTempDisplay = Observer.StatisticsTempDisplay(weatherData)
    weatherData.setMeasurements(25, 50)
    weatherData.setMeasurements(26, 70)
    weatherData.setMeasurements(12, 32)


if __name__ == "__main__":
    main()