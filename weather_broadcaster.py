# import logging

from weather_station import WeatherStation


# logger = logging.getLogger(__name__)

#具象主題的子類別
class WeatherBroadcaster(WeatherStation):
    def __init__(self , weather_api_key = None):
        super().__init__(weather_api_key = weather_api_key)
        self.user_models = {}                                  #收集所有觀察者

    def register_observer(self, user, model):       #註冊觀察者
        self.user_models.setdefault(user , model)


    def notify(self):                   #向所有觀察者通知天氣資訊
        models = self.user_models.copy()
        for model in models.values():
            model.notify(self.get_data_by_locationName(locationName=model.user_data.get("locationName",None)))