from os import path
import logging
from time import sleep

from weather_wrapper import get_json_content
from weather_broadcaster import WeatherBroadcaster
from model import get_notification_model



logger = logging.getLogger(__name__)
Current_Path = path.dirname(path.abspath(__file__))  #當前路徑
Hour = 60*5


def main():
    user_data = get_json_content(path.join(Current_Path, "user_data.json"))
    weather_broadcaster = WeatherBroadcaster(weather_api_key=user_data.get("weather_api_key"))

    for user , user_info in user_data["users"].items():
        try:
            model = get_notification_model(user_info.get("model_type"))
            model(weather_broadcaster , user_info)
        except Exception as err :
            logger.error("fail with model {} error: {}".format(
                user_info.get("model_type"), err
            ))




    while True:
        try:
            weather_broadcaster.notify()
            sleep(Hour)
        except KeyboardInterrupt:
            logger.warning("keyboard interrupt\n")
            break
        except Exception as e :
            logger.error("main exception: {}".format(e))
            break



if __name__=="__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s"
    )
    main()