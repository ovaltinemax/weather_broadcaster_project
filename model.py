from notifiactions import GeneralModelNotification
from notifiactions import PremiumlModelNotification



def get_notification_model(model_type):
    if model_type == "PremiumModelNotification":
        return PremiumlModelNotification
    
    else:
        return GeneralModelNotification