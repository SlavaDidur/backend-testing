import requests
from services.base_services import absolute_url

class TestPositiveLogin:
    def test_01_positive_login(self):
        data = {
            "email": "vadym.stoilovskyi.cr+1@gmail.com",
            "password": "Qwerty11"
        }

        r = requests.post(url=absolute_url("/sessions"), json=data)
        response = r.json()
        assert r.status_code == 200
        assert response['data']['user']['email'] == data['email']
        assert response['data']['session']['accessToken']


class TestInvalidLogin:
    def test_01_empty_email(self):
        data = {
            "email": "",
            "password": "Qwerty11"
        }
        error = "\"email\" is not allowed to be empty"
        r = requests.post(url=absolute_url("/sessions"), json=data)
        response = r.json()
        assert r.status_code == 400
        assert response['error']['message'] == error


    def test_02_empty_password(self):
        data = {
            "email": "vadym.stoilovskyi.cr+1@gmail.com",
            "password": ""
        }
        error = "\"password\" is not allowed to be empty"
        r = requests.post(url=absolute_url("/sessions"), json=data)
        response = r.json()
        assert r.status_code == 400
        assert response['error']['message'] == error


    def test_03_invalid_email(self):
        data = {
            "email": "vyacheslav.didur.cr+1@gmail.com",
            "password": "Qwerty11"
        }
        error = "Incorrect email or password"
        r = requests.post(url=absolute_url("/sessions"), json=data)
        response = r.json()
        assert r.status_code == 400
        assert response['error']['message'] == error