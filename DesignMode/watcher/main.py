from subject import WeatherData
from observer import Observer, CurrentConditionsDisplay, StatisticsTempDisplay


def main():
    weatherData = WeatherData()
    currentDisplay = CurrentConditionsDisplay(weatherData)
    statisticsTempDisplay = StatisticsTempDisplay(weatherData)
    weatherData.setMeasurements(25, 50)
    weatherData.setMeasurements(26, 70)
    weatherData.setMeasurements(12, 32)


if __name__ == "__main__":
    main()
