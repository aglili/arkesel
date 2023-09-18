import os
import sys
import pytest
from unittest.mock import Mock
from dotenv import load_dotenv
import unittest

load_dotenv()

project_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_directory)

from arkesel.smsV2 import SMSV2

ARKESEL_API_KEY = os.getenv("ARKESEL_API_KEY")

@pytest.fixture
def smsv2_instance():
    return SMSV2(api_key=ARKESEL_API_KEY)

def test_send_sms(smsv2_instance):
    sender = "SenderID"
    message = "This Is A Message"
    recipients = ['1234567890', '9876543210','22354674948']

    expected_response = {
        "status": "success",
        "data": [
            {
            "recipient": "1234567890",
            "id": "9b752841-7ee7-4d40-b4fe-768bfb1da4f0"
            },
            {
            "recipient": "9876543210",
            "id": "7ea01acd-485c-4df3-b646-e9e24430e145"
            },
            {
            "invalid numbers": [
                "22354674948"
            ]
            }
        ]
    }

    with unittest.mock.patch("requests.post") as mock_post:
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = expected_response
        mock_post.return_value = mock_response

        # Call the send_sms method
        response = smsv2_instance.send_sms(sender, message, recipients)

        # Check if the API was called with the correct parameters
        mock_post.assert_called_with(
            url="https://sms.arkesel.com/api/v2/sms/send",
            headers={'api-key': ARKESEL_API_KEY},
            data={
                'sender': sender,
                'message': message,
                'recipients': recipients
            }
        )

        # Check the API response
        assert response == expected_response

def test_schedule_sms(smsv2_instance):
    sender = "SenderID"
    message = "This Is A Scheduled Message"
    recipients = ['1234567890', '9876543210','22354674948']
    scheduled_date = "2023-09-30 14:30:00 PM"

    expected_response = {
        "status": "success",
        "data": [
            {
            "recipient": "1234567890",
            "id": "9b752841-7ee7-4d40-b4fe-768bfb1da4f0"
            },
            {
            "recipient": "9876543210",
            "id": "7ea01acd-485c-4df3-b646-e9e24430e145"
            },
            {
            "invalid numbers": [
                "22354674948"
            ]
            }
        ]
    }

    with unittest.mock.patch("requests.post") as mock_post:
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = expected_response
        mock_post.return_value = mock_response

        # Call the schedule_sms method
        response = smsv2_instance.schedule_sms(sender, recipients, message, scheduled_date)

        # Check if the API was called with the correct parameters
        mock_post.assert_called_with(
            url="https://sms.arkesel.com/api/v2/sms/send",
            headers={'api-key': ARKESEL_API_KEY},
            data={
                'sender': sender,
                'message': message,
                'recipients': recipients,
                'scheduled_date': scheduled_date
            }
        )

        # Check the API response
    assert response == expected_response



def test_check_balance(smsv2_instance):
    expected_response ={
        "status": "success",
        "data": {
            "sms_balance": "2003",
            "main_balance": "GHS 20.99"
        }
    }

    with unittest.mock.patch("requests.get") as mock_get:
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = expected_response
        mock_get.return_value = mock_response

        response = smsv2_instance.check_balance()


        mock_get.assert_called_with(
            url="https://sms.arkesel.com/api/v2/clients/balance-details",
            headers={'api-key': ARKESEL_API_KEY}
        )


        assert response == expected_response


def test_sms_details(smsv2_instance):
    sms_id = "SMS123"
    expected_response = {
        "status": "success",
        "data": {
            "ID": "f3be70c1-3545-4677-b607-6b5f32202652",
            "status": "DELIVERED",
            "sender": "Arkesel",
            "recipient": "233544919953",
            "message": "Welcome to version 2 of our API!",
            "message_count": 1,
            "sent_at_time": "2021-04-09 18:44:05"
        }
    }

    with unittest.mock.patch("requests.get") as mock_get:
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = expected_response
        mock_get.return_value = mock_response

        response = smsv2_instance.sms_details(sms_id)

        mock_get.assert_called_with(
            url=f"https://sms.arkesel.com/api/v2/sms{sms_id}",
            headers={'api-key': ARKESEL_API_KEY}
        )

        assert response == expected_response






