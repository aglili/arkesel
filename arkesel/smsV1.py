import requests


import requests
from typing import Optional

class SMSV1:
    """
    A class to interact with the Arkesel SMS API for sending SMS messages and retrieving account information.

    Attributes:
        api_key (str): The API key for authentication.
    """
    def __init__(self, api_key: str) -> None:
        """
        Initializes an instance of the SMSV1 class.

        Args:
            api_key (str): The API key for authentication.
        """
        self.api_key = api_key

    def send_sms(self, sender: str, message: str, recipient: str) -> dict:
        """
        Sends an SMS message to the specified recipient.

        Args:
            sender (str): The sender's phone number or name.
            message (str): The message content.
            recipient (str): The recipient's phone number.

        Returns:
            dict: The API response in JSON format.
        """
        url = "https://sms.arkesel.com/sms/api?action=send-sms"
        params = {
            "action": "send-sms",
            "api_key": self.api_key,
            "to": recipient,
            "from": sender,
            "sms": message
        }
        response = requests.get(url=url, params=params)
        return response.json()

    def schedule_sms(self, recipient: str, sender: str, message: str, time: str) -> dict:
        """
        Schedule an SMS message to be sent at a specific time.

        Args:
            recipient (str): The recipient's phone number.
            sender (str): The sender's phone number or name.
            message (str): The message content.
            time (str): The time to schedule the SMS (format: "YYYY-MM-DD HH:MM:SS AM/PM").

        Returns:
            dict: The API response in JSON format.
        """
        url = f"https://sms.arkesel.com/sms/api?action=send-sms&api_key={self.api_key}&from={sender}&sms={message}&schedule={time}"

        response = requests.get(url=url)
        return response.json()

    def check_balance(self) -> dict:
        """
        Retrieves the account balance.

        Returns:
            dict: The API response in JSON format containing balance information.
        """
        url = "https://sms.arkesel.com/sms/api?action=check-balance"
        params = {
            "action": "check-balance",
            "api_key": self.api_key,
            "response": "json"
        }
        response = requests.get(url=url, params=params)
        return response.json()

    def save_contact(self, phonebook_name: str, phone_number: str, first_name: Optional[str] = None,
                     last_name: Optional[str] = None, email: Optional[str] = None, company: Optional[str] = None) -> dict:
        """
        Saves a contact to the specified phone book.

        Args:
            phonebook_name (str): The name of the phone book.
            phone_number (str): The phone number of the contact.
            first_name (str, optional): The first name of the contact. Defaults to None.
            last_name (str, optional): The last name of the contact. Defaults to None.
            email (str, optional): The email address of the contact. Defaults to None.
            company (str, optional): The company name of the contact. Defaults to None.

        Returns:
            dict: The API response in JSON format.
        """
        url = "https://sms.arkesel.com/contacts/api"
        params = {
            "action": "subscribe-us",
            "api_key": self.api_key,
            "phone_book": phonebook_name,
            "phone_number": phone_number,
        }

        if first_name:
            params["first_name"] = first_name
        if last_name:
            params["last_name"] = last_name
        if email:
            params["email"] = email
        if company:
            params["company"] = company

        response = requests.get(url=url, params=params)
        return response.json()
