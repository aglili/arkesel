import requests


class OTP:
    """
    A class to interact with the Arkesel OTP API for generating and verifying OTPs.

    Attributes:
        api_key (str): The API key for authentication.
    """

    def __init__(self, api_key: str) -> None:
        """
        Initializes an instance of the OTP class.

        Args:
            api_key (str): The API key for authentication.
        """
        self.api_key = api_key
        self.headers = {"api-key": api_key}

    def sms_otp(self, expiry_minutes: int, recipient: str, sender_id: str):
        """
        Generates an OTP and sends it via SMS.

        Args:
            expiry_minutes (int): The expiry time for the OTP in minutes.
            recipient (str): The recipient's phone number.
            sender_id (str): The sender ID to display in the SMS.

        Raises:
            requests.exceptions.RequestException: If there is an error during the API request.
        """
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
        response = requests.post(url=url, headers=self.headers, data=data)
        if not response["code"] == "1000":
            raise requests.exceptions.RequestException(f"Failed: {response.text}")

        return None


    def voice_otp(self, expiry_minutes: int, recipient: str, sender_id: str):
        """
        Generates an OTP and sends it via voice call.

        Args:
            expiry_minutes (int): The expiry time for the OTP in minutes.
            recipient (str): The recipient's phone number.
            sender_id (str): The sender ID for the voice call.

        Raises:
            requests.exceptions.RequestException: If there is an error during the API request.
        """
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
        response = requests.post(url=url, headers=self.headers, data=data)
        if not response["code"] == "1000":
            raise requests.exceptions.RequestException(f"Failed: {response.text}")

        return None

    def verify_otp(self, code: str, number: str):
        """
        Verifies an OTP with the provided code and phone number.

        Args:
            code (str): The OTP code to verify.
            number (str): The phone number associated with the OTP.

        Raises:
            requests.exceptions.RequestException: If there is an error during the API request.
        """
        url = "https://sms.arkesel.com/api/otp/verify"
        data = {
            "api-key": self.api_key,
            "code": code,
            "number": number
        }
        response = requests.post(url=url, data=data, headers=self.headers)
        if not response["message"] == "Successful":
            raise requests.exceptions.RequestException(f"Failed: {response.text}")
        
        return None