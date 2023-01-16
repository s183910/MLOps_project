from fastapi import FastAPI, UploadFile, File
from predict import APIModelHandler
from typing import List

app = FastAPI()

@app.get("/")
def root():
    """ Health check."""
    response = {
        "message": "OK",
        "status-code": 200,
    }
    return response

@app.get("/")
def read_root():
   return {"Hello": "World"}

@app.post("/upload_img/")
async def create_upload_file(files: List[UploadFile] = File(...)):
   

   model = APIModelHandler()
   clasifications = model.classify(files)

   return {"files": [file.filename for file in files], "classifications": clasifications}