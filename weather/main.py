import eel
from pyowm import OWM
from pyowm.utils.config import get_default_config
from config_import import TOKEN


config_dict = get_default_config()
config_dict['language'] = "ru"
owm = OWM(TOKEN)
mgr = owm.weather_manager()

@eel.expose
def weather(place):
    if place == "":
        return "Введіть місто"
    
    observation = mgr.weather_at_place(place)
    w = observation.weather
    
    status = w.detailed_status
    w.wind()
    humidity = w.humidity
    temp = w.temperature('celsius')['temp']

    
    return f"В місті {place} зараз {status}\nТемпература {round(temp)} градусів по цельсію" \
           f"Вологість складає {humidity}%\n Швидкість вітру {w.wind()['speed']} метрів в секунду"

eel.init("web")
eel.start("index.html", size=(400, 600))
