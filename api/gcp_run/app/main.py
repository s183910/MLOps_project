from typing import List

import uvicorn
from app.predict import APIModelHandler
from fastapi import FastAPI, File, UploadFile

app = FastAPI()


@app.get("/")
def root():
    """Health check."""
    response = {
        "message": "OK",
        "status-code": 200,
    }
    return response


@app.post("/upload_img/")
async def create_upload_file(files: List[UploadFile] = File(...)):

    model = APIModelHandler()
    clasifications = model.classify(files)

    results = [
        {"file": file.filename, "classification": classification}
        for file, classification in zip(files, clasifications)
    ]

    return results
