from fastapi import FastAPI, UploadFile, File
from http import HTTPStatus
from enum import Enum
from typing import Optional
from api.predict import APIModelHandler
from PIL import Image

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

@app.post("/upload_img/")
async def create_upload_file(file: UploadFile = File(...)):
   
   model = APIModelHandler()
   prediction = model.classify([file])

   return {"filename": file.filename, "prediction": prediction}