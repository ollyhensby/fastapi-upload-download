# FastAPI Upload & Download Test

This is just a repository to test the upload and download of files using FastAPI.

Following this guide: https://python.plainenglish.io/file-uploads-and-downloads-in-fastapi-a-comprehensive-guide-06e0b18bb245

## How To Run?

Create the environment

```bash
mamba env create -f environment.yml
```

Activate the environment

```bash
conda activate fastapi-upload-download
```

Run the FastAPI server

```bash
uvicorn main:app --reload
```

## API Calls

### Upload File

In the FastAPI, you can upload a file using the endpoint `/upload`.

The file is saved to the `files` folder in the root directory.

For example, let's say we upload an image called `image.png`, then the file will be saved to `files/image.png`.

And as we have enabled static files, you can access the file using the URL `http://127.0.0.1:8000/files/image.png`.

### Download File

In the FastAPI, you can download a file using the endpoint `/download`.

Currently we just download a test excel file located in `files/test.xlsx`.

## UI Components

The UI components are built using ipywidgets and ipyautoui.

They utilise the API calls to allow users to upload and download files from the FastAPI server.

The UI components are located in the `download.ipynb` and `upload.ipynb` notebook.
