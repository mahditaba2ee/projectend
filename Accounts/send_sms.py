
from kavenegar import *

try:
    api = KavenegarAPI('72754F7553462B6E45756F4D79304964456C354F36754F69643041552F452B524A704463507775503379513D')
    param = {
        'sender':'100047778',
        'receptor':'09134303981',
        'message':'12457'
    }
    response = api.sms_send(param)
    print(response)
except APIException as e:
    print(e)
except HTTPException as e:
    print(e)


