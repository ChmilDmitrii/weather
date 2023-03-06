from environs import Env

env = Env()
env.read_env()  # read .env file, if it exists

ACCESS_TOKEN = env('ACCESS_TOKEN')  # ipinfo access token
USE_ROUNDED_COORDS = env.bool('USE_ROUNDED_COORDS')
OPENWEATHER_API = env('OPENWEATHER_API')  # openweather api key
OPENWEATHER_URL = (
    "https://api.openweathermap.org/data/2.5/weather?"
    "lat={latitude}&lon={longitude}&"
    "appid=" + OPENWEATHER_API + "&lang=ru&"
    "units=metric"
)
# OPENWEATHER_URL = (
#     "https://api.openweathermap.org/data/3.0/onecall?"
#     "lat={latitude}&lon={longitude}&exclude=current&"
#     "appid=" + OPENWEATHER_API + "&units=metric"
# )
