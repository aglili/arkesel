import os
import sys
import pytest
from unittest.mock import Mock
from dotenv import load_dotenv
import unittest

load_dotenv()

project_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_directory)

from arkesel.voice import VOICE

ARKESEL_API_KEY = os.getenv("ARKESEL_API_KEY")

@pytest.fixture
def voice_instance():
    return VOICE(api_key=ARKESEL_API_KEY)

def test_send_voice_message(voice_instance):
    recipients = ['1234567890', '9876543210']
    voice_file = 'https://example.com/voice_file.mp3'
    voice_id = 'VOICE_ID123'

    expected_response = {
        'status': 'success',
        'message': 'Voice message sent successfully!'
    }

    with unittest.mock.patch("requests.post") as mock_post:
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = expected_response
        mock_post.return_value = mock_response

        # Call the send_voice_message method
        response = voice_instance.send_voice_message(recipients, voice_file, voice_id)

        # Check if the API was called with the correct parameters
        mock_post.assert_called_with(
            url="https://sms.arkesel.com/api/v2/sms/voice/send",
            headers={'api-key': ARKESEL_API_KEY},
            data={
                'voice_file': voice_file,
                'recipients': recipients,
                'voice_id': voice_id
            }
        )

        # Check the API response
        assert response == expected_response
