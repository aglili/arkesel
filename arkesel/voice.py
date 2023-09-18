import requests
from typing import List,Optional

class VOICE:
    """
    A class to interact with the Arkesel Voice API for sending voice messages.

    Attributes:
        api_key (str): The API key for authentication.
    """

    def __init__(self, api_key: str) -> None:
        """
        Initializes an instance of the VOICE class.

        Args:
            api_key (str): The API key for authentication.
        """
        self.headers = {"api-key": api_key}

    def send_voice_message(self, recipients: List[str], voice_file: str,voice_id:Optional[str]=None) -> dict:
        """
        Sends a voice message to the specified recipients.

        Args:
            recipients (List[str]): List of recipient phone numbers.
            voice_file (str): Path or URL to the voice file.
            voice_id (str): A Voice ID or DID number that can be used for the Voice SMS.Voice ID is optional and can be registered through Arkesel Support channel.

        Returns:
            dict: The API response in JSON format.
        """
        url = "https://sms.arkesel.com/api/v2/sms/voice/send"
        data = {
            "voice_file": voice_file,
            "recipients": recipients
        }
        if voice_id:
            data["voice_id"] = voice_id
        response = requests.post(url=url, headers=self.headers, data=data)
        return response.json()
