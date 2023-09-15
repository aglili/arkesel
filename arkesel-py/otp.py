import requests


class OTP:
    def __init__(self,api_key) -> None:
        self.api_key = api_key
        self.headers = {"api-key":api_key}

    def sms_otp(self,expiry_minutes:int,recipient,sender_id:str):

        url = "https://sms.arkesel.com/api/otp/generate"

        data = {
            "expiry": expiry_minutes,
            "length": 6,
            "medium": "sms",
            "message": 'This is OTP for verification, %otp_code% and expires in %expiry%',
            "number": recipient,
            "sender_id": sender_id,
            "type": "numeric"
        }


        response = requests.post(url=url,headers=self.headers,data=data)

        return response.json()
    

    def voice_otp(self,expiry_minutes:int,recipient,sender_id:str):

        url = "https://sms.arkesel.com/api/otp/generate"

        data = {
            "expiry": expiry_minutes,
            "length": 6,
            "medium": "voice",
            "message": 'This is OTP for verification, %otp_code% and expires in %expiry%',
            "number": recipient,
            "sender_id": sender_id,
            "type": "numeric"
        }


        response = requests.post(url=url,headers=self.headers,data=data)

        return response.json()
    


    def verify_otp(self,code:str,number:str):
        url = "https://sms.arkesel.com/api/otp/verify"

        data = {
            "api-key":self.api_key,
            "code":code,
            "number":number
        }

        response = requests.post(url=url,data=data,headers=self.headers)
    

    


