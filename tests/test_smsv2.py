import os
import pytest
from dotenv import load_dotenv
from arkesel.smsV2 import SMSV2

load_dotenv()

ARKESEL_API_KEY = os.getenv("ARKESEL_API_KEY")

@pytest.fixture
def smsv2_instance(mocker):
    return SMSV2(api_key=ARKESEL_API_KEY)

def test_send_sms(smsv2_instance, mocker):
    sender = "SenderID"
    message = "This Is A Message"
    recipients = ['1234567890', '9876543210', '22354674948']

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

    # Mock the requests.post
    mocker.patch("requests.post", return_value=mocker.Mock(json=lambda: expected_response))

    # Call the send_sms method 
    response = smsv2_instance.send_sms(sender, message, recipients)
    assert response == expected_response

def test_schedule_sms(smsv2_instance, mocker):
    sender = "SenderID"
    message = "This Is A Scheduled Message"
    recipients = ['1234567890', '9876543210', '22354674948']
    scheduled_date = "2023-09-30 14:30:00 PM"

    expected_response = {
        "status": "success",
        "data": [
            {
                "recipient": "1234567890",
                "id": "9b752841-7ee7-4d40-b4fe-768bfb1da4f0",
                "scheduled_date": scheduled_date
            },
            {
                "recipient": "9876543210",
                "id": "7ea01acd-485c-4df3-b646-e9e24430e145",
                "scheduled_date": scheduled_date
            }
        ],
        "invalid numbers": ["22354674948"]
    }

    # Mock the requests.post 
    mock_post = mocker.patch("requests.post")
    mock_post.return_value.json.return_value = expected_response

    # Call the schedule_sms method 
    response = smsv2_instance.schedule_sms(sender, recipients, message, scheduled_date)
    assert response == expected_response

def test_check_balance(smsv2_instance, mocker):
    # Define the expected API response
    expected_response ={
        "status": "success",
        "data": {
            "sms_balance": "2003",
            "main_balance": "GHS 20.99"
        }
    }

    # Mock the requests.get call using mocker.patch
    mock_get = mocker.patch("requests.get")
    mock_get.return_value.json.return_value = expected_response

    # Call the check_balance method and assert the response
    response = smsv2_instance.check_balance()
    assert response == expected_response

def test_sms_details(smsv2_instance, mocker):
    sms_id = "SMS123"

    expected_response = {
        "status": "success",
        "data": {
            "ID": sms_id,
            "status": "DELIVERED",
            "sender": "Arkesel",
            "recipient": "233544919953",
            "message": "Welcome to version 2 of our API!",
            "message_count": 1,
            "sent_at_time": "2021-04-09 18:44:05"
        }
    }

    # Mock the requests.get call using mocker.patch
    mock_get = mocker.patch("requests.get")
    mock_get.return_value.json.return_value = expected_response

    # Call the sms_details method and assert the response
    response = smsv2_instance.sms_details(sms_id)
    assert response == expected_response
