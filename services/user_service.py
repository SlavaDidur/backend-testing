import requests
from services.base_services import absolute_url


def login_user(email: str, password: str):
    data = {
        "email": email,
        "password": password
    }
    r = requests.post(url=absolute_url('/sessions'), json=data)
    if r.status_code == 200:
        return r.json()['data']
    raise Exception(f"Login attempt was not success. Data: {data}")
