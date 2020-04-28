# Send mail

Console script for sending emails using the built in template.

## Getting Started

### Manual Installation

1. **Clone the repository:**

```bash
https://github.com/5p1K3-wq/sendMail.git
```
2. **Open directory:**

`cd sendMail/`

3. **We start the setup script setup.py.**

`python3 setup.py`

4. **Specify the values for the following variables:**

![](https://imgur.com/MO2c97s.png)

```bash
EMAIL_FROM=from@mail.com - Sender Email
EMAIL_FROM_LOGIN=user - Login email of the sender
EMAIL_FROM_PASS=P@$$w0rd - Password email of the sender
EMAIL_TO=to@mail.com - Recipient Email
```
5. Run a script that will send an email

```bash
python3 main.py
```

## Built With

[python-dotenv 0.13.0](https://pypi.org/project/python-dotenv/) - It allows you to load environment variables from the .env file in the root directory of the application.