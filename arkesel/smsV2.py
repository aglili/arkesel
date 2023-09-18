import requests
from .errors import MissingAPIKey

class SMSV2:

    """
    A class to send SMS messages using the Arkesel SMS API.

    This Uses Version 2 of the API

    Attributes:
        api_key (str): The API key for authentication.
    """
    def __init__(self,api_key:str) -> None:

        """
        Initializes an instance of the SMSV2 class.

        Args:
            api_key (str): The API key for authentication.
        """
        if not api_key:
            raise MissingAPIKey("Your API Key is missing")
        self.headers = {"api-key":api_key}



    def send_sms(self,sender:str,message:str,recipients:list):
        """
        Sends an SMS message to the specified recipients.

        Args:
            sender (str): The sender's phone number or name.
            message (str): The message content.
            recipients (List[str]): List of recipient phone numbers.

        Returns:
            dict: The API response in JSON format.
        """
        url = "https://sms.arkesel.com/api/v2/sms/send"
        data = {
        "sender": sender,
        "message": message,
        "recipients": recipients 
        }
        response = requests.post(url=url,data=data,headers=self.headers)
        return response.json()
    



    def schedule_sms(self,sender:str,recipients:list,message:str,schedule_date:str):

        """
        Schedule an SMS message to be sent at a specific date and time.

        Args:
            sender (str): The sender's phone number or name.
            recipients (list): List of recipient phone numbers.
            message (str): The message content.
            schedule_date (str): The date and time to schedule the SMS (format: "YYYY-MM-DD HH:MM:SS").

        Returns:
            dict: The API response in JSON format.
    """
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
        """
        Retrieves the account balance and other related details.

        Returns:
            dict: The API response in JSON format containing balance details.
        """
        url = "https://sms.arkesel.com/api/v2/clients/balance-details"
        response = requests.get(url=url,headers=self.headers)
        return response.json()
    
    def sms_details(self,sms_id:str):
        """
        Retrieves details of a specific SMS using its ID.

        Args:
            sms_id (str): The ID of the SMS.

        Returns:
            dict: The API response in JSON format containing SMS details.
        """
        url = f"https://sms.arkesel.com/api/v2/sms{sms_id}"
        response = requests.get(url=url,headers=self.headers)
        return response.json()
    

