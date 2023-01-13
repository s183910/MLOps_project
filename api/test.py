from fastapi import FastAPI, UploadFile, File, FileResponse
from http import HTTPStatus
from enum import Enum
from typing import Optional
import cv2 

app = FastAPI()

@app.get("/")
def root():
    """ Health check."""
    response = {
        "message": HTTPStatus.OK.phrase,
        "status-code": HTTPStatus.OK,
    }
    return response

@app.get("/")
def read_root():
   return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
   return {"item_id": item_id}

class ItemEnum(Enum):
   alexnet = "alexnet"
   resnet = "resnet"
   lenet = "lenet"

@app.get("/restric_items/{item_id}")
def read_item(item_id: ItemEnum):
   return {"item_id": item_id}

@app.get("/query_items")
def read_item(item_id: int):
   return {"item_id": item_id}

@app.get("/query_model")
def read_item(item_id: ItemEnum):
   return {"item_id": item_id}


database = {'username': [ ], 'password': [ ]}

@app.post("/login/")
def login(username: str, password: str):
   username_db = database['username']
   password_db = database['password']
   if username not in username_db and password not in password_db:
      with open('api/database.csv', "a") as file:
            file.write(f"{username}, {password} \n")
      username_db.append(username)
      password_db.append(password)
   return "login saved"

@app.post("/cv_model/")
async def cv_model(data: UploadFile = File(...), w: Optional[int] = 28, h: Optional[int] = 28):
   
   img = await cv2.imread("api/sign_png/sign_test_i.png")
   img = cv2.resize(img, (h, w))
   cv2.imwrite('image_resize.jpg', img)
   
   FileResponse('api/sign_png/sign_test_i_resized.png')

   response = {
      "input": data,
      "message": HTTPStatus.OK.phrase,
      "status-code": HTTPStatus.OK,
   }
   return response