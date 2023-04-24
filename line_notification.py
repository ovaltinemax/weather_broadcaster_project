import requests
from abc import ABC,abstractmethod




# 抽象基底的Line_Notification
class LineNotification(ABC):
    Line_URL ="https://notify-api.line.me/api/notify"

    def __init__(self , line_token):
        self._line_token = line_token


    @abstractmethod
    def _enrich_message(msg):
        pass


    def notify(self , msg):
        headers = {"Authorization":"Bearer " + self._line_token}
        payload = {"message": str(msg)}
        response = requests.post(self.Line_URL, headers=headers , params=payload)
        return response.status_code



