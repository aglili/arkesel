import os
import pytest
from requests import Response
from arkesel.voice import VOICE

ARKESEL_API_KEY = os.getenv("ARKESEL_API_KEY")

@pytest.fixture
def voice_instance():
    return VOICE(api_key=ARKESEL_API_KEY)

def test_send_voice_message(voice_instance, mocker):
    recipients = ['1234567890', '9876543210']
    voice_file = 'https://example.com/voice_file.mp3'
    voice_id = 'VOICE_ID123'

    expected_response = {
        'status': 'success',
        'message': 'Voice message sent successfully!'
    }

    def mock_requests_post(url, headers, json=None, data=None):
        assert url == "https://sms.arkesel.com/api/v2/sms/voice/send"
        assert headers['api-key'] == ARKESEL_API_KEY
        assert json is None  
        assert data == {
            'voice_file': voice_file,
            'recipients': recipients,
            'voice_id': voice_id
        }

        # Create Mock response object
        mock_response = Response()
        mock_response.status_code = 200
        mock_response.json = lambda: expected_response

        return mock_response

    mocker.patch("requests.post", side_effect=mock_requests_post)

    # Call the send_voice_message method
    response = voice_instance.send_voice_message(recipients, voice_file, voice_id)

    # Check if the API was called with the correct parameters
    assert response == expected_response
