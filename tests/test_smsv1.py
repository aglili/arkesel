import os
import sys
import pytest
from unittest.mock import Mock
from arkesel.smsV1 import SMSV1
from arkesel.errors import MissingAPIKey
from dotenv import load_dotenv
import unittest

load_dotenv()

ARKESEL_API_KEY = os.getenv("ARKESEL_API_KEY")

project_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_directory)

@pytest.fixture
def sms_instance():
    return SMSV1(api_key=ARKESEL_API_KEY)

def test_send_sms(sms_instance):
    sender = "SenderID"
    message = "This Is A Message"
    recipient = "054xxxxxxx"

    expected_response = {
        "code": "ok",
        "message": "Successfully Sent",
        "balance": 1185,
        "main_balance": 2.974,
        "user": "Arkesel Dev"
    }

    with unittest.mock.patch("requests.get") as mock_get:
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = expected_response
        mock_get.return_value = mock_response

        response = sms_instance.send_sms(sender, message, recipient)

        mock_get.assert_called_with(
            url="https://sms.arkesel.com/sms/api?action=send-sms",
            params={
                "api_key": ARKESEL_API_KEY,
                "to": recipient,
                "from": sender,
                "sms": message
            }
        )

    assert response == expected_response

def test_schedule_sms(sms_instance):
    sender = "SenderID"
    message = "This Is A Scheduled Message"
    recipient = "054xxxxxxx"
    scheduled_time = "2023-09-30 14:30:00 PM"

    expected_response = {
            "code": "ok",
            "message": "Scheduled SMS created successfully",
            "scheduled_time": scheduled_time
        }
       

    with unittest.mock.patch("requests.get") as mock_get:
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = expected_response
        mock_get.return_value = mock_response

            # Call the schedule_sms method
        response = sms_instance.schedule_sms(recipient, sender, message, scheduled_time)

            # Check if the API was called with the correct parameters
        mock_get.assert_called_with(
            url=f"https://sms.arkesel.com/sms/api?action=send-sms&api_key={ARKESEL_API_KEY}&from={sender}&sms={message}&schedule={scheduled_time}"
        )


            # Check the API response
        assert response == expected_response

def test_save_contact(sms_instance):
    phonebook_name = "MyPhoneBook"
    phone_number = "1234567890"
    first_name = "John"
    last_name = "Doe"
    email = "john.doe@example.com"
    company = "Example Inc."

    expected_response = {
        "code": "ok",
        "message": "Contact saved successfully"
    }

    with unittest.mock.patch("requests.get") as mock_get:
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = expected_response
        mock_get.return_value = mock_response

        # Call the save_contact method
        response = sms_instance.save_contact(phonebook_name, phone_number, first_name, last_name, email, company)

        # Check if the API was called with the correct parameters
        mock_get.assert_called_with(
            url="https://sms.arkesel.com/contacts/api",
            params={
                "action": "subscribe-us",
                "api_key": ARKESEL_API_KEY,
                "phone_book": phonebook_name,
                "phone_number": phone_number,
                "first_name": first_name,
                "last_name": last_name,
                "email": email,
                "company": company
            }
        )

        # Check the API response
    assert response == expected_response




def test_check_balance(sms_instance):
    expected_response = {
        "balance": 1185,
        "user": "Arkesel Dev",
        "country": "Ghana"
    }

    with unittest.mock.patch("requests.get") as mock_get:
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = expected_response
        mock_get.return_value = mock_response

        # Call the check_balance method
        response = sms_instance.check_balance()

        # Check if the API was called with the correct parameters
        mock_get.assert_called_with(
            url="https://sms.arkesel.com/sms/api?action=check-balance",
            params={
                "api_key": ARKESEL_API_KEY,
                "response": "json"
            }
        )


        # Check the API response
        assert response == expected_response



