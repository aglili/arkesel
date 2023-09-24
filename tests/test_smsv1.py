import os
import sys
import pytest
from arkesel.smsV1 import SMSV1
from dotenv import load_dotenv

load_dotenv()

ARKESEL_API_KEY = os.getenv("ARKESEL_API_KEY")

project_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_directory)

@pytest.fixture
def sms_instance():
    return SMSV1(api_key=ARKESEL_API_KEY)

def test_send_sms(sms_instance, mocker):
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

    mocker.patch("requests.get", return_value=MockResponse(200, expected_response))

    response = sms_instance.send_sms(sender, message, recipient)

    assert response == expected_response

@pytest.mark.parametrize("scheduled_time", ["2023-09-30 14:30:00 PM"])
def test_schedule_sms(sms_instance, scheduled_time, mocker):
    sender = "SenderID"
    message = "This Is A Scheduled Message"
    recipient = "054xxxxxxx"

    expected_response = {
        "code": "ok",
        "message": "Scheduled SMS created successfully",
        "scheduled_time": scheduled_time
    }

    mocker.patch("requests.get", return_value=MockResponse(200, expected_response))

    response = sms_instance.schedule_sms(recipient, sender, message, scheduled_time)

    assert response == expected_response

@pytest.mark.parametrize("phonebook_name, phone_number, first_name, last_name, email, company", [
    ("MyPhoneBook", "1234567890", "John", "Doe", "john.doe@example.com", "Example Inc.")
])
def test_save_contact(sms_instance, phonebook_name, phone_number, first_name, last_name, email, company, mocker):
    expected_response = {
        "code": "ok",
        "message": "Contact saved successfully"
    }

    mocker.patch("requests.get", return_value=MockResponse(200, expected_response))

    response = sms_instance.save_contact(phonebook_name, phone_number, first_name, last_name, email, company)

    assert response == expected_response

def test_check_balance(sms_instance, mocker):
    expected_response = {
        "balance": 1185,
        "user": "Arkesel Dev",
        "country": "Ghana"
    }

    mocker.patch("requests.get", return_value=MockResponse(200, expected_response))

    response = sms_instance.check_balance()

    assert response == expected_response

class MockResponse:
    def __init__(self, status_code, json_data):
        self.status_code = status_code
        self.json_data = json_data

    def json(self):
        return self.json_data
