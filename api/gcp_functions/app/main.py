from fastapi import FastAPI, UploadFile, File
from predict import APIModelHandler
from typing import List
import uvicorn

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

def main():
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
   