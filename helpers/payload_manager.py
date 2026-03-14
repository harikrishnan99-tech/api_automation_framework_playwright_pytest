import json

with open("data/data_payload.json", "r") as f:
    data = json.load(f)

def login_payload() -> dict:
    return {
        "username": data["login_payload"]["username"],
        "password": data["login_payload"]["password"]
    }

def add_user_payload() -> dict:
    return {
        "firstName": data["add_user_payload"]["firstName"],
        "lastName": data["add_user_payload"]["lastName"],
        "age": data["add_user_payload"]["age"]
    }

def update_user_payload() -> dict:
    return {
        "firstName": data["update_user_payload"]["firstName"],
        "lastName": data["update_user_payload"]["lastName"],
        "age": data["update_user_payload"]["age"],
        "height": data["update_user_payload"]["height"],
        "weight": data["update_user_payload"]["weight"]
    }