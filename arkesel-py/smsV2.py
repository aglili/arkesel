import requests

class ARKESELSMS_V1:
    def __init__(self,api_key) -> None:
        self.headers = {"api-key":api_key}



    def send_sms(self,sender:str,message:str,recipients:list):
        url = "https://sms.arkesel.com/api/v2/sms/send"
        data = {
        "sender": sender,
        "message": message,
        "recipients": recipients 
        }
        response = requests.post(url=url,data=data,headers=self.headers)
        return response.json()
    



    def schedule_sms(self,sender:str,recipients:list,message:str,schedule_date:str):

        url = "https://sms.arkesel.com/api/v2/sms/send"


        data = {
        "sender": sender,
        "message": message,
        "recipients": recipients,
        "scheduled_date": schedule_date
        }


        response = requests.post(url=url,data=data,headers=self.headers)

        return response.json()
    

    def check_balance(self):
        url = "https://sms.arkesel.com/api/v2/clients/balance-details"
        response = requests.get(url=url,headers=self.headers)
        return response.json()
    
    def sms_details(self,sms_id:str):
        url = f"https://sms.arkesel.com/api/v2/sms{sms_id}"
        response = requests.get(url=url,headers=self.headers)
        return response.json()
    

