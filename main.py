import os
import shutil
import time
import pathlib

from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Allows access to static files e.g. png
app.mount('/files', StaticFiles(directory='files'),'files')


@app.post('/upload')
def upload_file(uploaded_file: UploadFile = File(...)):
    path = f"files/{uploaded_file.filename}"
    with open(path, 'w+b') as file:
        shutil.copyfileobj(uploaded_file.file, file)

    return {
        'file': uploaded_file.filename,
        'content': uploaded_file.content_type,
        'path': path,
    }


@app.get('/download')
def download():
    test_xlsx = pathlib.Path(__file__).parent / "files" / "test.xlsx"
    return FileResponse(path=test_xlsx, media_type="application/octet-stream", filename=test_xlsx.name)