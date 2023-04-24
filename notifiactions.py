import logging
from weather_wrapper import Temp, Humd, Wind , Weather_status 
from line_notification import LineNotification


logger = logging.getLogger(__name__)


class GeneralModelNotification(LineNotification):
    def __init__(self, weather_broadcaster , user_data):
        self.user_data = user_data
        weather_broadcaster.register_observer(user_data.get("user"), self)
        super().__init__(line_token=user_data.get("line_token"))


    def notify(self, msg):
        logger.info("user: {} GeneralModel notify message: {}".format(
            self.user_data.get("user" , "NAME_IS_NEEDED"), self._enrich_message(msg)
        ))
        return super().notify(self._enrich_message(msg))
    
    def _enrich_message(self ,msg):
        return str({
            "溫度": Temp(msg).get("TEMP","Null"),
            "相對濕度": Humd(msg),
            "天氣狀況": Weather_status(msg)
        })
    


class PremiumlModelNotification(LineNotification):
    def __init__(self, weather_broadcaster , user_data):
        self.user_data = user_data
        weather_broadcaster.register_observer(user_data.get("user"), self)
        super().__init__(line_token=user_data.get("line_token"))


    def notify(self, msg):
        logger.info("user: {} PremiumModel notify message: {}".format(
            self.user_data.get("user" , "NAME_IS_NEEDED"), self._enrich_message(msg)
        ))
        return super().notify(self._enrich_message(msg))
    
    def _enrich_message(self ,msg):
        return str({
            "溫度": Temp(msg).get("TEMP","Null"),
            "相對濕度": Humd(msg),
            "天氣狀況": Weather_status(msg),
            "風速": Wind(msg).get("WDSD","Null")
        })