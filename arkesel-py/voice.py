import requests



class ARKESEL_VOICE:
    def __init__(self,api_key) -> None:
        self.headers = {"api-key":api_key}


    def send_voice_message(self,recipients:list,voice_file):
        url = "https://sms.arkesel.com/api/v2/sms/voice/send"
        data = {  
        "voice_file": voice_file,
        "recipients": recipients
        }
        response = requests.post(url=url,headers=self.headers,data=data)
        return response.json()