from weather_wrapper import WeatherWrapper
import json
import logging 
from requests import Timeout

from abc import ABC, abstractmethod

logger = logging.getLogger(__name__)


class WeatherStation(ABC):

    def __init__(self, weather_api_key=None):
        self._weather_api_key = weather_api_key
        self._weather_wrapper =None


    @abstractmethod   #定義抽象方法，註冊觀察者
    def register_observer(self , user , model):
        pass

    
    @abstractmethod   #定義抽象方法
    def notify(self):
        pass


    @property     #將weather_wrapper方法變成屬性(attribute)封裝起來
    def weather_wrapper(self):
        try:
            if not self._weather_wrapper:
                self._weather_wrapper = self._weather_api_key
        except Timeout as err:
            logger.error('WeatherStation owm fail with TimeOut error {}'.format(err))
        return self._weather_wrapper
    

    def get_data_by_locationName(self , locationName):
        observation = self.weather_wrapper
        weather = WeatherWrapper(observation ,locationName)
        return json.loads(weather.text)
    