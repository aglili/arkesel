import os,sys
import pytest
from unittest.mock import Mock
import unittest
from dotenv import load_dotenv

load_dotenv()


project_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_directory)


from arkesel.otp import OTP

ARKESEL_API_KEY = os.getenv("ARKESEL_API_KEY")

@pytest.fixture
def otp_instance():
    return OTP(api_key=ARKESEL_API_KEY)

def test_sms_otp(otp_instance):
    with unittest.mock.patch("requests.post") as mock_post:
        expected_response = {
            'code': '1000',
            'ussd_code': '*928*01#',
            'message': 'Successful, OTP is being processed for delivery'
        }
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = expected_response
        mock_post.return_value = mock_response

        # Call the sms_otp method
        response = otp_instance.sms_otp(5, '0557362859', 'Aglili')

        # Check if the API was called with the correct parameters
        mock_post.assert_called_with(
            url="https://sms.arkesel.com/api/otp/generate",
            headers={'api-key': ARKESEL_API_KEY},
            data={
                'expiry': 5,
                'length': 6,
                'medium': 'sms',
                'message': 'This is OTP for verification, %otp_code% and expires in %expiry%',
                'number': '0557362859',
                'sender_id': 'Aglili',
                'type': 'numeric'
            }
        )

        # Check the API response
        assert response == expected_response



def test_voice_otp(otp_instance):
    expected_response = {
        'code': '1000',
        'ussd_code': '*928*01#',
        'message': 'Successful, OTP is being processed for delivery'
    }

    with unittest.mock.patch("requests.post") as mock_post:
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = expected_response
        mock_post.return_value = mock_response

            # Call the voice_otp method
        response = otp_instance.voice_otp(5, '0557362859', 'Aglili')

            # Check if the API was called with the correct parameters
        mock_post.assert_called_with(
                url="https://sms.arkesel.com/api/otp/generate",
                headers={'api-key': ARKESEL_API_KEY},
                data={
                    'expiry': 5,
                    'length': 6,
                    'medium': 'voice',
                    'message': 'This is OTP for verification, %otp_code% and expires in %expiry%',
                    'number': '0557362859',
                    'sender_id': 'Aglili',
                    'type': 'numeric'
                }
            )

            # Check the API response
        assert response == expected_response

def test_verify_otp(otp_instance):
    expected_response = {
        "code": "1100",
        "message": "Successful"
    }

    with unittest.mock.patch("requests.post") as mock_post:
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = expected_response
        mock_post.return_value = mock_response

            # Call the verify_otp method
        response = otp_instance.verify_otp('123456', '0557362859')

            # Check if the API was called with the correct parameters
        mock_post.assert_called_with(
            url="https://sms.arkesel.com/api/otp/verify",
            headers={'api-key': ARKESEL_API_KEY},
            data={
                    'api-key': ARKESEL_API_KEY,
                    'code': '123456',
                    'number': '0557362859'
                }
            )

            # Check the API response
        assert response == expected_response