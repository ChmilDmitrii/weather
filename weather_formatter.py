from weather_api_service import Weather


def format_weather(weather: Weather) -> str:
    """ Форматирование данных погоды в строку """
    return (f'{weather.city}, температура {weather.temperature} град.C, '
            f'{weather.weather_type}\n'
            f'Восход: {weather.sunrise.strftime("%H:%M")}\n'
            f'Закат: {weather.sunset.strftime("%H:%M")}\n')
