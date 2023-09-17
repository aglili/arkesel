import requests



class SMSV1:
    def __init__(self,api_key) -> None:
        self.api_key = api_key


    def send_sms(self,sender:str,message:str,recipient:str):
        url = "https://sms.arkesel.com/sms/api?action=send-sms"
        params = {
            "action":"send-sms",
            "api_key":self.api_key,
            "to":recipient,
            "from":sender,
            "sms":message
        }
        response = requests.get(url=url,params=params)
        return response.json()
    

    def schedule_sms(self,recipeient:str,sender:str,message:str,time:str):
        url = "https://sms.arkesel.com/sms/api?schedule=####"
        params = {
            "action": "send-sms",
            "api_key": self.api_key,
            "to": recipeient,
            "from": sender,
            "sms": message,
            "schedule": time
        }
        response = requests.get(url=url,params=params)
        return response.json()
    

    def check_balance(self):
        url = "https://sms.arkesel.com/sms/api?action=check-balance"
        params = {
            "action": "check-balance",
            "api_key": self.api_key,
            "response": "json"
        }
        response = requests.get(url=url,params=params)
        return response.json()


    def save_contact(self,phonebook_name:str,phone_number:str,first_name:str=None,last_name:str=None,email:str=None,company:str=None):
        url = "https://sms.arkesel.com/contacts/api"
        params = {
            "action": "subscribe-us",
            "api_key": self.api_key,
            "phone_book": phonebook_name,
            "phone_number": phone_number,
        }

        if first_name:
            params["first_name"]=first_name
        if last_name:
            params['last_name']=last_name
        if email:
            params['email']=email
        if company:
            params['company']=company

        response = requests.get(url=url,params=params)

        return response.json()
