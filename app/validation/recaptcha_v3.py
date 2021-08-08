import requests
import os

class RecaptchaV3():
    @staticmethod
    def check(token):
        secret_key = os.getenv("RECAPTCHA_SECRET_KEY")

        if (secret_key == None):
            return

        recaptcha_url = 'https://www.google.com/recaptcha/api/siteverify'
        data = {
           'secret': secret_key,
           'response': token,
        }

        response = requests.post(recaptcha_url, data)
        result = response.json()
        return result.get('success')