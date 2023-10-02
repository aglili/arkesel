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



    def send_sms(self,sender:str,message:str,recipients:list)->dict:
        """
        Sends an SMS message to the specified recipients.

        Args:
            sender (str): The sender's phone number or name.
            message (str): The message content.
            recipients (List[str]): List of recipient phone numbers.

        Returns:
            response(dict): Returns Json Response
        """
        url = "https://sms.arkesel.com/api/v2/sms/send"
        data = {
        "sender": sender,
        "message": message,
        "recipients": recipients 
        }
        response = requests.post(url=url,data=data,headers=self.headers)
        return response



    def schedule_sms(self,sender:str,recipients:list,message:str,schedule_date:str)->dict:

        """
        Schedule an SMS message to be sent at a specific date and time.

        Args:
            sender (str): The sender's phone number or name.
            recipients (list): List of recipient phone numbers.
            message (str): The message content.
            schedule_date (str): The date and time to schedule the SMS (format: "YYYY-MM-DD HH:MM:SS").

        Returns:
            response(dict): Returns Json Response
        """
        url = "https://sms.arkesel.com/api/v2/sms/send"


        data = {
        "sender": sender,
        "message": message,
        "recipients": recipients,
        "scheduled_date": schedule_date
        }


        response = requests.post(url=url,data=data,headers=self.headers)

        return response
    

    def check_balance(self)->dict:
        """
        Retrieves the account balance and other related details.

        Returns:
            response(dict): Returns Json Response
        """
        url = "https://sms.arkesel.com/api/v2/clients/balance-details"
        response = requests.get(url=url,headers=self.headers).json()
        return response
    
    def sms_details(self,sms_id:str)->dict:
        """
        Retrieves details of a specific SMS using its ID.

        Args:
            sms_id (str): The ID of the SMS.

        Returns:
            response(dict): Returns Json Response
        """
        url = f"https://sms.arkesel.com/api/v2/sms{sms_id}"
        response = requests.get(url=url,headers=self.headers).json()
        return response
    

    def group_message(self,send_id:str,message:str,group_name:str)->dict:
        """
        Sends a message to a created group.

        Args:
            send_id (str): Id of the sender.
            message (str): Message to be sent to that particular group
            group_name (str): The Name of the group to which the message is being sent

        Returns:
            response(dict): Returns Json Response
        """

        url = "https://sms.arkesel.com/api/v2/sms/send/contact-group"

        data = {
            "sender": send_id,
            "group_name": group_name,
            "message": message
        }

        response = requests.post(url=url,data=data,headers=self.headers).json()

        return response


