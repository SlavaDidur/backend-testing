import requests
from services.base_services import absolute_url
from services.user_service import login_user

product_model = [{
    "subTypeId": 1,
    "name": "string",
    "brandName": "string",
    "description": "string",
    "location": "string",
    "size": 10,
    "sizeUnit": "mL",
    "stockAvail": 10,
    "stockAvailUnit": "lbs",
    "thc": 10,
    "cbd": 11,
    "isPublished": True,
    "isSendQuote": True,
    "isNeedEdit": False,
}]


def test_01_add_product():
    user_token = login_user("vadym.stoilovskyi.cr+1@gmail.com", "Qwerty11")["session"]["accessToken"]
    headers = {"Authorization": f"Bearer {user_token}"}
    r = requests.post(url=absolute_url("/products"), json=product_model, headers=headers)

    assert r.status_code == 201


product_model_edited = {
    "name": "string",
    "brandName": "string",
    "description": "string",
    "location": "string",
    "size": 15,
    "sizeUnit": "mL",
    "stockAvail": 15,
    "stockAvailUnit": "lbs",
    "thc": 15,
    "cbd": 21,
    "isPublished": True,
    "isSendQuote": True,
    "isNeedEdit": False,
}

def test_02_edit_product():
    user_token = login_user("vadym.stoilovskyi.cr+1@gmail.com", "Qwerty11")["session"]["accessToken"]
    headers = {"Authorization": f"Bearer {user_token}"}
    add_product = requests.post(url=absolute_url("/products"), json=product_model, headers=headers)
    response = add_product.json()
    product_id = response["data"][0]["id"]
    r = requests.put(url=absolute_url(f"/products/{product_id}"), json=product_model_edited, headers=headers)
    response = r.json()

    assert r.status_code == 200
    assert response['data']['size'] == 15
    assert response['data']['stockAvail'] == 15
    assert response['data']['thc'] == 15
    assert response['data']['cbd'] == 21


def test_03_delete_product():
    user_token = login_user("vadym.stoilovskyi.cr+1@gmail.com", "Qwerty11")["session"]["accessToken"]
    headers = {"Authorization": f"Bearer {user_token}"}
    add_product = requests.post(url=absolute_url("/products"), json=product_model, headers=headers)
    response = add_product.json()
    product_id = response["data"][0]["id"]
    r = requests.delete(url=absolute_url(f"/products/{product_id}"), headers=headers)

    assert r.status_code == 204
    product_details = requests.get(url=absolute_url(f"/products/{product_id}"), headers=headers)
    assert product_details.status_code == 404


