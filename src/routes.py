from fastapi import FastAPI

from get_mac_user_name import get_mac_user_name

app = FastAPI()
 
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.get("/get_mac_user_name")
def get_mac_user_name_route():
    return get_mac_user_name()
