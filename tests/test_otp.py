import os
import pytest
from arkesel.otp import OTP

ARKESEL_API_KEY = os.getenv("ARKESEL_API_KEY")

@pytest.fixture
def mock_requests_post(mocker):
    return mocker.patch("requests.post")

@pytest.fixture
def otp_instance():
    return OTP(api_key=ARKESEL_API_KEY)

def test_sms_otp(mocker, mock_requests_post, otp_instance):
    expected_response = {
        'code': '1000',
        'ussd_code': '*928*01#',
        'message': 'Successful, OTP is being processed for delivery'
    }

    mock_requests_post.return_value.status_code = 200
    mock_requests_post.return_value.json.return_value = expected_response

    # Call the sms_otp method
    response = otp_instance.sms_otp(5, '0557362859', 'Aglili')

    # Check if the API was called with the correct parameters
    mock_requests_post.assert_called_once_with(
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

def test_voice_otp(mocker, mock_requests_post, otp_instance):
    expected_response = {
        'code': '1000',
        'ussd_code': '*928*01#',
        'message': 'Successful, OTP is being processed for delivery'
    }

    mock_requests_post.return_value.status_code = 200
    mock_requests_post.return_value.json.return_value = expected_response

    # Call the voice_otp method
    response = otp_instance.voice_otp(5, '0557362859', 'Aglili')

    # Check if the API was called with the correct parameters
    mock_requests_post.assert_called_once_with(
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

def test_verify_otp(mocker, mock_requests_post, otp_instance):
    expected_response = {
        "code": "1100",
        "message": "Successful"
    }

    mock_requests_post.return_value.status_code = 200
    mock_requests_post.return_value.json.return_value = expected_response

    # Call the verify_otp method
    response = otp_instance.verify_otp('123456', '0557362859')

    # Check if the API was called with the correct parameters
    mock_requests_post.assert_called_once_with(
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

