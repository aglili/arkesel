# Arkesel Python Package

A Python wrapper for  [https://arkesel.com] - an unofficial implementation.


## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)


## Installation

you can install the package using Pip

```bash
pip install arksel
```


## Usage

### Initialization

```
from arkesel.smsv1 import SMSV1

sms = SMSV1(api_key="ARKESEL-API-KEY")
```

look in documentation for full examples


## Examples

##### Example 1-Sending SMS with the V2 api

```python
from arkesel.smsV2 import SMSV2

sms = SMSV2(api_key="ARKESEL-API-KEY")

response = sms.send_sms(sender="Trial",message="Trial Message",recipient=["02xxxxxxy1","0232xxxxxx","050xxxxxxx"])

print(response) ## json is returned 
```

##### Output
```json
  {
  "status": "success",
  "data": [
    {
      "recipient": "02xxxxxxy1",
      "id": "9b752841-7ee7-4d40-b4fe-768bfb1da4f0"
    },
    {
      "recipient": "0232xxxxxx",
      "id": "7ea01acd-485c-4df3-b646-e9e24430e145"
    },
    {
      "invalid numbers": [
        "050xxxxxxx"
      ]
    }
  ]

}
```


##### Example 2-OTP Request

```python
from arksel.otp import OTP

otp = OTP(api_key="ARKESEL-API-KEY")

response = otp.sms_otp(expiry_minutes=6,recipient="027xxxxxxx",sender_id="Trial")

print(response) ## json is returned is returned

```

##### Output
```json
{
  "code": "1000",
  "ussd_code": "*928*01#",
  "message": "Successful, OTP is being processed for delivery"
}
```

Check full docs for more help[]


## Contributing

### Contributing Guidelines

We welcome contributions to improve the project! This guide will help you get started with contributing to our project.

## How to Contribute

1. Fork the repository.

2. Clone the forked repository to your local machine:
   ```bash
   git clone https://github.com/your_username/your_repository.git
    ```

3. Create a new branch for your feature or bugfix

    ```bash
    git checkout -b feature/your-feature   # For a new feature
    git checkout -b bugfix/your-bug-fix    # For a bug fix
    ```

4. Make your changes and commit them

    ```bash
    git add .
    git commit -m "Description of your changes"
    ```

5. Push your branch to GitHub
    ```bash
    git push origin your-branch-name
    ```

6. Open a pull request (PR) to the main repository's `main` branch. Provide a clear and descriptive title for your PR.



## License

This project is licensed under the [MIT License](LICENSE). See the [LICENSE](LICENSE) file for details.




